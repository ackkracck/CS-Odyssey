# Beginner → Intermediate Roadmap: JavaScript/TypeScript · React/Next.js · Node.js · PostgreSQL

_A correctness-audited, production-minded path you can follow and upload to GitHub._

> **Outcome**  
> By the end, you’ll model data in PostgreSQL, build typed APIs in Node.js, ship accessible React UIs with Next.js, validate inputs at boundaries, test your code (unit → e2e), and deploy with confidence.

---

## Contents

- [What “Intermediate” Means](#what-intermediate-means)
- [Week 0 — Prerequisites & Setup](#week-0--prerequisites--setup)
- [Phases 1–9 — The Learning Path](#phases-1–9--the-learning-path)
- [Projects (Portfolio-Ready)](#projects-portfolio-ready)
- [Reference Stack (Minimal, Proven)](#reference-stack-minimal-proven)
- [Daily Workflow: Scripts, Layout, Env](#daily-workflow-scripts-layout-env)
- [Common Footguns (and Fixes)](#common-footguns-and-fixes)
- [Example 12-Week Plan](#example-12week-plan)
- [Mini Cheat Sheets](#mini-cheat-sheets)
- [Capstone Checklist](#capstone-checklist)
- [Self-Assessment Rubric](#selfassessment-rubric)
- [Official Resources](#official-resources)
- [Double-Audit Notes (for Absolute Correctness)](#doubleaudit-notes-for-absolute-correctness)

---

## What “Intermediate” Means

You can:

- **PostgreSQL**: design normalized schemas, use constraints & indexes, write joins/aggregations, and read `EXPLAIN ANALYZE`.
- **Node.js**: design RESTful (or RPC) APIs with input validation, typed responses, error handling, logging, and tests.
- **React/Next.js**: build accessible, responsive UIs; know when to use **Server Components** vs **Client Components**; understand routing & data fetching.
- **TypeScript**: keep `"strict": true`, use unions/generics/narrowing, and let types flow across layers.
- **Operations**: configure envs & secrets, run migrations, set up CI, and deploy without breaking prod.

---

## Week 0 — Prerequisites & Setup

- **OS & Tools**: Terminal, Git, GitHub account.
- **Node LTS**: Install **Node.js 20 LTS or 22 LTS** (use a version manager like `nvm`).  
- **Editor**: VS Code + extensions: ESLint, Prettier, TypeScript, EditorConfig, Markdown.
- **Package manager**: `npm` (bundled with Node).  
- **Docker (recommended)** for DB locally.
- **PostgreSQL**:  
  - Docker quickstart:
    ```bash
    docker run --name pg -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
    ```
  - Verify:
    ```bash
    docker exec -it pg psql -U postgres -c "select version();"
    ```

---

## Phases 1–9 — The Learning Path

Each phase has **Target → Core Study → Do It → Checkpoint**. Move on only when you pass the checkpoint.

### Phase 1 — Modern JavaScript (ES202x)

**Target**: Write correct, idiomatic JS without googling basics.

**Core Study**
- Scope & closures; `let/const`; objects/arrays/maps/sets; destructuring/spread.
- Modules (ESM `import/export`), npm scripts.
- Async: Promises, `async/await`, **event loop & microtasks**.
- Errors: `try/catch`, error types, stack traces.

**Do It**
- Build a tiny **CSV→JSON CLI** using `fs/promises`.  
- Implement `debounce`, `throttle`, `memoize` with tests.

**Checkpoint**
- Explain why `await` inside `Array.prototype.forEach` is a trap and fix with `for...of` or `Promise.all`.
- Use Node inspector breakpoints to diagnose an async race.

---

### Phase 2 — TypeScript Essentials

**Target**: Use types to prevent classes of bugs, not to fight them.

**Core Study**
- Basic types, union/intersection, **narrowing** (`typeof`, `in`, discriminated unions).
- Functions & **generics**; utility types (`Partial`, `Pick`, `Record`).
- `tsconfig.json` with `"strict": true`.
- Typing async code and external data.

**Do It**
- Convert your CLI to TS (`tsc --init`).
- Add a small **domain model** (`User`, `Task`) with typed helpers.

**Checkpoint**
- Replace an `any` with an inferred generic and keep type inference ergonomic.
- Explain structural typing and when to use branded/nominal patterns.

---

### Phase 3 — React Fundamentals

**Target**: Build accessible, stateful UIs and reason about re-renders.

**Core Study**
- Function components; hooks: `useState`, `useEffect`, `useMemo`, `useCallback`, `useRef`.
- Controlled forms; lifting/deriving state; context (sparingly).
- Accessibility (labels, focus management, landmarks).
- Styling: CSS Modules or Tailwind (utility-first).

**Do It**
- **Task Tracker (client-only)**: CRUD in memory, filters/search, keyboard navigation, screen reader friendly.

**Checkpoint**
- Demonstrate why **list keys** must be stable/unique and show a bug caused by bad keys.

---

### Phase 4 — Next.js Fundamentals

**Target**: File-based routing, data fetching, server vs client components.

**Core Study**
- App Router: routes, layouts, nested routes, route groups.
- **Data fetching** in Server Components; when to opt into Client Components.
- **Route Handlers** (`app/api/*`) for server endpoints; **Server Actions** if available in your version.
- Rendering & caching: static vs dynamic; revalidation; `fetch` cache controls.
- Metadata, env vars, and deployment basics.

**Do It**
- Port Task Tracker to **Next.js**: server-render list; client component for edits.

**Checkpoint**
- Justify choosing a Client Component (e.g., interactive form) and disable caching for a must-be-fresh fetch.

---

### Phase 5 — Node.js APIs & Services

**Target**: Design robust APIs and understand the runtime.

**Core Study**
- Node runtime model; ESM vs CJS; `fs`, `http`; high-level understanding of streams.
- API design: resources, status codes, pagination, error shapes.
- **Validation** (`zod`/similar), configuration (`dotenv`), structured logging.

**Do It**
- **Tasks API**: `GET/POST/PATCH/DELETE /tasks` with validation and error middleware; produce JSON with consistent error shapes.

**Checkpoint**
- Explain the event loop and why CPU-bound work blocks it; outline offloading (worker threads/queues).

---

### Phase 6 — PostgreSQL Fundamentals

**Target**: Model data, enforce invariants, and read query plans.

**Core Study**
- DDL/DML: `CREATE/INSERT/SELECT/UPDATE/DELETE`.
- Modeling: normalization; foreign keys; **constraints**; when to denormalize.
- Indexes (btree), partial/composite; `EXPLAIN ANALYZE`.
- Transactions, isolation levels; ACID.
- Migrations & seed data; roles & least privilege.

**Do It**
- Schema: `users`, `tasks`, `task_labels`, `sessions`.
- Write 5 non-trivial queries (joins, aggregates, filtered sorts).
- Improve a slow query using an index and confirm via `EXPLAIN ANALYZE`.

**Checkpoint**
- Enforce “unique email per user” with a **unique constraint** (not only app code).
- Explain why `%term%` can’t use a btree index and alternatives (trigram/full-text).

---

### Phase 7 — Integrate Next.js + Node.js + PostgreSQL

**Target**: A type-safe full-stack app with validated boundaries.

**Core Study**
- DB access from Node with `pg` **or** ORM/Query builder. Pick one and stick to it:  
  - **Prisma** (schema-first DX, migrations, strong types)  
  - **Drizzle** (SQL-first, lightweight, explicit)
- Validation at API boundary; infer TS types from validation schemas.
- AuthN/AuthZ: session cookies vs JWT; password hashing (Argon2id/bcrypt); role checks.

**Do It (Capstone v1 — “TaskForge”)**
- Sign up/login (session-based, httpOnly cookie).
- CRUD tasks with labels, search, filters; optimistic UI for edits.
- Server-render task lists; Client Components for forms/inline edits.
- Route protection & simple roles (user/admin).

**Checkpoint**
- Trace a flow end-to-end: **Form → Validation → DB → Response → UI update**, preserving types across layers.

---

### Phase 8 — Quality: Testing, Linting, Security, Observability

**Target**: Confidence to change code quickly and safely.

**Core Study**
- **ESLint + TypeScript-ESLint**, Prettier; EditorConfig; CI (GitHub Actions).
- **Testing**:  
  - Unit (Vitest/Jest) for pure logic.  
  - React Testing Library for components.  
  - Playwright/Cypress for e2e.
- **Security**:
  - Validate all untrusted input; parameterized queries.
  - Password hashing (Argon2id/bcrypt).
  - Cookie flags: `Secure`, `HttpOnly`, `SameSite=Lax` (or `Strict` when appropriate).
  - CSRF: required for cookie-based state changes when SameSite posture doesn’t prevent cross-site posting; use tokens on forms.
  - Rate limit login; set security headers (CSP tailored to your app, HSTS in prod).
- **Observability**: structured logs, request IDs, basic latency/error dashboards.

**Do It**
- Add unit + component + e2e tests to TaskForge.
- Add rate limiting to auth; verify headers with an automated check.

**Checkpoint**
- Break a flow intentionally, watch an e2e test fail, fix it, and see it pass.

---

### Phase 9 — Deployment & Operations

**Target**: Ship updates safely; manage environments.

**Core Study**
- Next.js hosting (platform or custom Node server).
- Managed Postgres vs self-hosted; connection pooling.
- Migrations on deploy; seed data for non-prod; feature flags.
- Backups & restore drills; env promotion (dev → staging → prod); secret rotation.

**Do It**
- Deploy TaskForge (web + managed Postgres).
- GitHub Actions: lint, typecheck, tests → deploy.
- Schedule automatic DB backups; document restore steps.

**Checkpoint**
- Rotate DB credentials with minimal downtime; run a forward migration and its rollback.

---

## Projects (Portfolio-Ready)

1. **CSV→JSON CLI** (TS, Node) — single-file utility with tests.  
2. **React Task Tracker** — a11y, keyboard nav, filters, controlled forms.  
3. **Tasks API** — typed, validated Node service with logs & error middleware.  
4. **SQL Lab Book** — schemas, queries, and `EXPLAIN ANALYZE` notes.  
5. **TaskForge (Capstone)** — auth, tasks+labels, search, optimistic UI, tests, deployment.

Each repo includes: a clear **README**, `package.json` scripts, and **screenshots** (or GIFs).

---

## Reference Stack (Minimal, Proven)

- **Runtime**: Node.js **20 or 22 LTS**  
- **Types**: TypeScript with `"strict": true`  
- **Web**: Next.js (App Router) + React  
- **UI**: CSS Modules or Tailwind  
- **Validation**: `zod` (or similar) at every boundary  
- **DB**: PostgreSQL **15/16** locally via Docker, managed in prod  
- **DB Access**: Prisma **or** Drizzle (choose one; consistency beats choice)  
- **Testing**: Vitest/Jest + React Testing Library + Playwright/Cypress  
- **Quality**: ESLint + Prettier + EditorConfig  
- **Auth**: Session cookies (httpOnly, Secure in prod), Argon2id/bcrypt  
- **CI/CD**: GitHub Actions

> These choices emphasize fundamentals and stability while staying modern.

---

## Daily Workflow: Scripts, Layout, Env

**Example scripts (`package.json`)**
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "typecheck": "tsc --noEmit",
    "lint": "eslint .",
    "test": "vitest run",
    "test:watch": "vitest",
    "e2e": "playwright test",
    "migrate": "prisma migrate deploy",
    "db:push": "prisma db push"
  }
}
```

**Repo layout**
```
/src
  /app            # Next.js routes (App Router)
  /components
  /lib            # db client, logger, config
  /server         # validation schemas, route handlers/server actions
  /types
/tests
/prisma or /drizzle
```

**Environment**
- `.env` (local; never commit secrets): `DATABASE_URL=...`, `SESSION_SECRET=...`
- Use your host’s secret manager in production.

---

## Common Footguns (and Fixes)

- **Skipping runtime validation** → Validate every entry point (API, route handler, Server Action). Derive TS types from schemas.
- **Overusing Client Components** → Prefer Server Components for data fetching/static UI; opt into client only for interactivity/state.
- **App-only invariants** → Enforce with **DB constraints** (FKs, unique, check). App code can err; constraints don’t.
- **Unbounded queries** → Always `LIMIT`/paginate; create appropriate indexes; verify with `EXPLAIN ANALYZE`.
- **Leaking secrets** → Never log secrets; rotate; use least-privilege DB roles.
- **Premature optimization** → Measure first; optimize hot paths with evidence.

---

## Example 12-Week Plan

| Week | Focus | Output |
|---|---|---|
| 0 | Setup, Node LTS, Docker Postgres | System ready; hello-world CLI |
| 1 | JS fundamentals | CSV→JSON CLI with tests |
| 2 | Async + modules | CLI with streaming & error handling |
| 3 | TypeScript | Convert CLI; strict types |
| 4 | React basics | Task Tracker (client-only) |
| 5 | React a11y + perf | Polished Task Tracker |
| 6 | Next.js routing & data fetching | Task Tracker in Next.js |
| 7 | Node API design + validation | Tasks API service |
| 8 | PostgreSQL modeling + queries | Schema + 5 complex queries |
| 9 | Integrate API + DB | API backed by Postgres |
| 10 | Auth + roles | Sessions; protected routes |
| 11 | Testing (unit/component/e2e) | Test suite green |
| 12 | Deployment + CI | Deployed capstone; README polish |

Scale to 16–20 weeks by adding deeper DB practice, performance work, and more e2e coverage.

---

## Mini Cheat Sheets

**HTTP Status (CRUD)**
- Create: **201**; Read: **200**; Update: **200/204**; Delete: **204**;  
  Bad input: **400**; Unauthorized/Forbidden: **401/403**; Not found: **404**; Server error: **500**.

**SQL Index Tips**
- Index order matters (WHERE columns before ORDER BY).  
- Composite indexes help when queries use the **leftmost prefix**.  
- Text search: trigram or full-text; don’t expect `%term%` to use btree.

**React Re-renders**
- Triggered by state/props/context changes.  
- Use `useMemo`/`useCallback` only when identity stability prevents real work.  
- **Keys** must be stable, unique, minimal.

---

## Capstone Checklist

- [ ] Sign up/login with session cookie (`Secure`, `HttpOnly`, `SameSite=Lax/Strict`)  
- [ ] Users CRUD tasks; labels, search, filters; optimistic UI  
- [ ] Server-render lists; Client Components for forms & inline edits  
- [ ] Validation at every boundary; types inferred from schemas  
- [ ] DB: FKs, unique constraints, specific indexes  
- [ ] Tests: unit + component + e2e; all green in CI  
- [ ] Security: rate limit auth; CSP tuned; no secrets in logs  
- [ ] Observability: structured logs, request IDs  
- [ ] Deployment: automated migrations; backups scheduled & restore drill documented  
- [ ] README with architecture diagram & trade-offs

---

## Self-Assessment Rubric

**TypeScript**
- [ ] `tsc --noEmit` passes with `"strict": true`  
- [ ] You can write a generic function and a discriminated union with safe narrowing

**React/Next.js**
- [ ] You can add a route with correct data-fetching & caching semantics  
- [ ] You can justify Client vs Server Component trade-offs

**Node/API**
- [ ] You can add an endpoint with validation, typed responses, proper status codes  
- [ ] You can trace a request with structured logs & a request ID

**PostgreSQL**
- [ ] You can add a table with constraints and a safe migration/rollback  
- [ ] You can speed up a slow query and prove it with `EXPLAIN ANALYZE`

**Quality/DevOps**
- [ ] CI runs lint, typecheck, tests; main branch is protected  
- [ ] You can rotate secrets and restore a production backup in a sandbox

---

## Official Resources

- **JavaScript** — MDN Web Docs (Guides & References)  
- **TypeScript** — typescriptlang.org (Handbook, TSConfig Reference)  
- **React** — react.dev (Learn React)  
- **Next.js** — nextjs.org (Docs; App Router)  
- **Node.js** — nodejs.org (API Docs)  
- **PostgreSQL** — postgresql.org (Manual), `psql` reference

> Prefer official docs. Supplement with reputable tutorials for practice—not as a substitute.

---

## Double-Audit Notes (for Absolute Correctness)

**Audit Pass #1 (structural & scope):**
- Emphasizes **fundamentals** (JS/TS, HTTP, SQL, ACID, event loop) that are stable across minor tool versions.  
- Avoids brittle version promises; uses **LTS Node 20/22** and **Postgres 15/16** which are widely available.  
- Presents **checkpoints** to self-verify competence independent of library churn.

**Audit Pass #2 (footguns & operations):**
- Reinforces **runtime validation** + **DB constraints** to enforce invariants.  
- Clarifies **Server vs Client components** and **route handlers**; suggests **Server Actions only if available** in your version; otherwise use route handlers or traditional API routes.  
- Specifies cookie flags, CSRF posture, rate limiting, and migration/rollback expectations.  
- Testing pyramid includes unit, component, and **e2e with CI**.

**Risk Controls & Portability:**
- ORM choice (Prisma/Drizzle) is abstracted behind SQL fundamentals; switching remains feasible.  
- Hosting specifics are intentionally generic; any modern provider with Node + Postgres fits.  
- All commands are standard (Docker, npm) and avoid provider-specific lock-in.

---

### Quickstart Appendix (Optional, Copy/Paste Friendly)

**Create Next.js app (TypeScript)**
```bash
npx create-next-app@latest taskforge --ts
cd taskforge
npm run dev
```

**Add ESLint/Prettier (if not included)**
```bash
npm i -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin prettier eslint-config-prettier
```

**Add Zod + a DB tool**
```bash
npm i zod
# choose ONE of:
npm i -D prisma && npm i @prisma/client
# or
npm i drizzle-orm pg && npm i -D drizzle-kit
```

**Spin up Postgres (Docker)**
```bash
docker run --name pg -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
```

**Basic test stacks**
```bash
npm i -D vitest @testing-library/react @testing-library/jest-dom jsdom
npm i -D playwright && npx playwright install
```
