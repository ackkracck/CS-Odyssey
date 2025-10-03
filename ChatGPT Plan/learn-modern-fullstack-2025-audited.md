# Learn the 2025 Full‑Stack (Audited): **TypeScript + Next.js 15 (App Router) + tRPC + TanStack Query v5 + Prisma + PostgreSQL + Auth.js + shadcn/ui**

This guide is a **step‑by‑step, source‑linked roadmap** you can follow to learn and ship with the most popular web stack in 2025. It’s audited against the **official docs** and uses **correct, current APIs**.

---

## What you’ll build mentally as you go
- **UI:** React components via **Next.js 15 (App Router)**, styled with **Tailwind + shadcn/ui**  
- **Data fetching:** **tRPC** procedures consumed with **TanStack Query v5**  
- **DB layer:** **Prisma ORM** over **PostgreSQL** (local via Docker or managed like Neon/Supabase)  
- **Auth:** **Auth.js (NextAuth v5)** using Route Handlers and the `auth()` helper  
- **Caching mental model:** Next 15’s **opt‑in** data caching for `fetch()` + **static HTML prerender** nuance

> **Prereqs**: Install Node **18.17+** (Node **20/22 LTS** recommended), Git, and Docker (optional).

**Official docs (keep open):**
- Next.js App Router & caching: <https://nextjs.org/docs/app> and <https://nextjs.org/docs/app/getting-started/caching-and-revalidating>  
- tRPC (v11) + TanStack Query client: <https://trpc.io/docs/client/tanstack-react-query/setup>  
- TanStack Query v5 (React): <https://tanstack.com/query/v5/docs/framework/react/quick-start>  
- Auth.js (NextAuth v5) + Route Handlers: <https://authjs.dev/getting-started/installation?framework=next-js>  
- Prisma + Next.js: <https://www.prisma.io/docs/guides/nextjs>

---

## 0) Scaffold & baseline (30–60 min)

```bash
# Create a Next.js 15 app (non-interactive; App Router + TS + Tailwind + src/ directory)
pnpm dlx create-next-app@latest my-app \
  --ts --tailwind --app --src-dir --turbopack --eslint --use-pnpm --yes
cd my-app

# UI kit (shadcn/ui)
pnpm dlx shadcn@latest init
pnpm dlx shadcn@latest add button card input textarea

# TanStack Query + tRPC (new client) + validation + serialization
pnpm add @tanstack/react-query @trpc/server @trpc/client @trpc/tanstack-react-query zod superjson

# Auth.js (NextAuth v5)
pnpm add next-auth

# Prisma + PostgreSQL
pnpm add -D prisma
pnpm add @prisma/client
pnpm dlx prisma init --datasource-provider postgresql
```

Create **`.env.local`**:
```ini
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/myapp?schema=public"
NEXTAUTH_SECRET="replace-with-a-strong-random-string"
NEXTAUTH_URL="http://localhost:3000"
```

Local Postgres (optional):
```bash
docker run --name myapp-pg -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
```

---

## 1) Minimal wiring you’ll reuse in real apps

### 1a) Prisma schema (start tiny, migrate)
**`prisma/schema.prisma`**
```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String?
  createdAt DateTime @default(now())
}

model Post {
  id        String   @id @default(cuid())
  title     String
  content   String?
  published Boolean  @default(false)
  authorId  String?
  author    User?    @relation(fields: [authorId], references: [id])
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```
Run:
```bash
pnpm dlx prisma migrate dev --name init
pnpm dlx prisma generate
```

### 1b) tRPC server (App Router via **fetch adapter**)
**`app/api/trpc/[trpc]/route.ts`**
```ts
import { fetchRequestHandler } from '@trpc/server/adapters/fetch'
import { appRouter } from '@/server/trpc/router'
import { createContext } from '@/server/trpc/context'

const handler = (req: Request) =>
  fetchRequestHandler({
    endpoint: '/api/trpc',
    req,
    router: appRouter,
    createContext,
  })

export { handler as GET, handler as POST }
```

**`src/server/trpc/router/index.ts`**
```ts
import { initTRPC } from '@trpc/server'
import superjson from 'superjson'
import { z } from 'zod'
import { prisma } from '@/server/db'

const t = initTRPC.create({
  transformer: superjson,
})

export const router = t.router
export const publicProcedure = t.procedure

export const appRouter = router({
  post: router({
    list: publicProcedure.query(async () => {
      return prisma.post.findMany({ orderBy: { createdAt: 'desc' } })
    }),
    create: publicProcedure
      .input(z.object({ title: z.string().min(1), content: z.string().optional() }))
      .mutation(async ({ input }) => {
        return prisma.post.create({ data: { title: input.title, content: input.content } })
      }),
  }),
})

export type AppRouter = typeof appRouter
```

**`src/server/trpc/context.ts`**
```ts
export async function createContext() {
  return {}
}
```

**`src/server/db.ts`**
```ts
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient }

export const prisma =
  globalForPrisma.prisma ??
  new PrismaClient({
    log: process.env.NODE_ENV === 'development' ? ['query', 'error', 'warn'] : ['error'],
  })

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
```

### 1c) tRPC client + TanStack Query v5
> Use the **new** `@trpc/tanstack-react-query` integration.

**`src/lib/trpc.tsx`**
```tsx
'use client'

import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { createTRPCClient, httpBatchLink } from '@trpc/client'
import { createTRPCContext } from '@trpc/tanstack-react-query'
import type { AppRouter } from '@/server/trpc/router'
import React from 'react'

export const { TRPCProvider, useTRPC, useTRPCClient } = createTRPCContext<AppRouter>()

function makeQueryClient() {
  return new QueryClient()
}
let browserQueryClient: QueryClient | undefined

function getQueryClient() {
  if (typeof window === 'undefined') return makeQueryClient()
  return (browserQueryClient ??= makeQueryClient())
}

export function Providers({ children }: { children: React.ReactNode }) {
  const queryClient = getQueryClient()

  const trpcClient = React.useMemo(
    () =>
      createTRPCClient<AppRouter>({
        links: [
          httpBatchLink({
            url: '/api/trpc',
          }),
        ],
      }),
    []
  )

  return (
    <QueryClientProvider client={queryClient}>
      <TRPCProvider trpcClient={trpcClient} queryClient={queryClient}>
        {children}
      </TRPCProvider>
    </QueryClientProvider>
  )
}
```

Wrap your root layout:
**`app/layout.tsx`**
```tsx
import { Providers } from '@/lib/trpc'
import './globals.css'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
```

### 1d) Minimal feature (list + create)
**`app/page.tsx`**
```tsx
'use client'

import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useTRPC } from '@/lib/trpc'
import { useState } from 'react'

export default function Page() {
  const trpc = useTRPC()
  const qc = useQueryClient()

  const posts = useQuery(trpc.post.list.queryOptions())
  const create = useMutation(trpc.post.create.mutationOptions(), {
    onSuccess: () => qc.invalidateQueries({ queryKey: trpc.post.list.queryKey() }),
  })

  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')

  return (
    <section className="space-y-4 max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-semibold">Posts</h1>

      <form
        onSubmit={(e) => {
          e.preventDefault()
          create.mutate({ title, content: content || undefined })
          setTitle('')
          setContent('')
        }}
        className="grid gap-2 rounded-xl border p-4"
      >
        <input
          className="rounded-md border px-3 py-2"
          placeholder="Title"
          required
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          className="rounded-md border px-3 py-2"
          placeholder="Content (optional)"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <button
          disabled={create.isPending}
          className="w-fit rounded-xl bg-black px-4 py-2 text-white disabled:opacity-50 dark:bg-white dark:text-black"
        >
          {create.isPending ? 'Saving…' : 'Create'}
        </button>
      </form>

      <ul className="space-y-2">
        {posts.data?.map((p) => (
          <li key={p.id} className="rounded-xl border p-4">
            <div className="font-medium">{p.title}</div>
            {p.content && <p className="opacity-80">{p.content}</p>}
          </li>
        ))}
      </ul>
    </section>
  )
}
```

### 1e) Auth.js (NextAuth v5) — add later
**`src/auth.ts`**
```ts
import NextAuth from "next-auth"
import GitHub from "next-auth/providers/github"

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [GitHub],
})
```

**`app/api/auth/[...nextauth]/route.ts`**
```ts
export { GET, POST } from "@/auth"
```

Use `await auth()` in Server Components / Route Handlers to read the session (protect mutations, etc.).

---

## 2) The **14‑Day** learning path (follow precisely)

Each day has **goals, drills, and an exit criterion** so you know when to move on.

### **Day 1–2: Next.js App Router fundamentals**
- Read: App Router pages, layouts, Route Handlers; create a few routes.  
- Drill: Build `/customers` and `/invoices/[id]` with a shared layout.  
- **Exit:** You can explain when to use **Server vs Client Components** and add a Route Handler.

### **Day 3–4: TanStack Query v5 essentials**
- Read: Quick Start; queries, mutations, invalidation.  
- Drill: Convert a plain `fetch()` component to **useQuery/useMutation** + **invalidate** on success.  
- **Exit:** You can wire QueryClientProvider and invalidate by `queryKey` without guessing.

### **Day 5–6: tRPC v11 + App Router**
- Read: tRPC **TanStack React Query** setup + **fetch adapter**.  
- Drill: Create `post.list` + `post.create` with **Zod** validation; consume via `useTRPC()` and TanStack Query; handle failure states.  
- **Exit:** You can add a procedure + UI end‑to‑end in under an hour **with type safety**.

### **Day 7–8: Prisma + PostgreSQL**
- Read: Prisma Next.js guide; run `migrate dev`, add indexes/uniques; try Prisma Studio.  
- Drill: Add `User` and relate `Post.authorId`. Handle a unique email violation gracefully in your UI.  
- **Exit:** You can design a 3–4 table schema and run safe migrations confidently.

### **Day 9–10: Auth.js v5**
- Read: Auth.js Next.js install + `auth()` session guide.  
- Drill: GitHub OAuth; protect `post.create` server‑side using session user id; show/hide client UI by session.  
- **Exit:** Logged‑out users cannot perform protected mutations; you can read session in server code.

### **Day 11–12: UI polish with shadcn/ui**
- Add button/input/card; extract a modal form; embrace Tailwind utilities.  
- **Exit:** You can assemble clean UI quickly with reusable components.

### **Day 13: Caching & performance (Next 15)**
- Read: **Caching & Revalidating**. Understand that **`fetch()` is _not_ cached by default**, but **route HTML can still be prerendered & cached**; opt in with `cache:'force-cache'` or `revalidate`, or static route config.  
- Drill: Add `revalidate` to a list page and verify behavior via logs.  
- **Exit:** You can explain **data cache vs HTML prerender cache** and opt in/out deliberately.

### **Day 14: Ship**
- Deploy to **Vercel** (Node 22 runtime OK). Add `postinstall: prisma generate`.  
- Seed your DB and share a live URL.  
- **Exit:** A working app with CRUD, auth, and tests pushed to GitHub.

---

## 3) “Absolutely correct” checklists

### Tooling versions that matter
- **Node:** ≥ **18.17** (Next v14 raised the minimum). Prefer **20/22 LTS**.  
- **TanStack Query:** v5 (single‑object APIs).  
- **tRPC:** v11 with `@trpc/tanstack-react-query` client.  
- **Next.js data cache:** **opt‑in** for `fetch()`; prerendered HTML may be cached.

### Common footguns (and fixes)
- **Nothing shows after create:** Ensure `app/layout.tsx` renders children and **Providers** wrap the app.  
- **tRPC 404:** Check `app/api/trpc/[trpc]/route.ts` path + exported `GET`/`POST`.  
- **DB errors on deploy:** Add `"postinstall": "prisma generate"` and ensure the runtime can reach your Postgres.  
- **“Why didn’t my GET cache?”** In Next 15, caching is opt‑in for fetch/data; configure `revalidate`/`cache` or static route settings.

---

## 4) Extension tasks (weeks 3–4)

- **Pagination & search** (server‑driven), optimistic updates, toasts, error boundaries.  
- **File uploads** (Route Handler + signed URLs).  
- **RBAC** with Auth.js callbacks & session augmentation.  
- **Testing:** Vitest (units) + Playwright (happy‑path e2e).  
- **Prod DB:** Move from local Docker to Neon/Supabase/Railway; add DB backups and a staging env.

---

## Appendix: why these sources matter

- **Next.js App Router & caching** (learn the new defaults):  
  <https://nextjs.org/docs/app/getting-started/caching-and-revalidating>  
- **tRPC with Route Handlers** (fetch adapter) + the new TanStack Query integration:  
  <https://trpc.io/docs/server/adapters/fetch> • <https://trpc.io/docs/client/tanstack-react-query/setup>  
- **TanStack Query v5** quick start:  
  <https://tanstack.com/query/v5/docs/framework/react/quick-start>  
- **Auth.js (NextAuth v5)** Route Handlers & `auth()` helper:  
  <https://authjs.dev/getting-started/installation?framework=next-js> • <https://authjs.dev/getting-started/session-management/protecting?framework=Next.js>  
- **Prisma + Next.js** setup & best practices:  
  <https://www.prisma.io/docs/guides/nextjs>

---

### License
MIT — copy/adapt freely.