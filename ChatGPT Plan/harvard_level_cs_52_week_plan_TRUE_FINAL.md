# CS Bachelor‑Level Self‑Study — **52‑Week Plan + Week 0 (Onboarding)**

A rigorous, self‑paced path to a bachelor’s‑level understanding of Computer Science, optimized for ~**10–15 hours/week** on macOS with terminal‑friendly tools and GitHub.

- **Starting level:** comfortable with Python/JavaScript (variables, conditionals, loops, functions).
- **Primary texts/courses (anchors):**
  - **Computer Organization and Design** (Patterson & Hennessy, RISC‑V ed.).
  - **Operating Systems: Design and Implementation** (Tanenbaum, Bos, MINIX‑3).
  - **Nand2Tetris** (Parts I–II).
  - **CS50** (for breadth refreshers and C foundations).

> ✅ *Clarity notes*: This plan intentionally includes **Week 0** as optional onboarding **outside** the 52‑week clock. Weeks **1–52** constitute the full year. Nand2Tetris weeks are **sequentially correct** (no regressions/duplication). Networking **Week 19** covers **HTTP/HTTPS/TLS** (not a TCP repeat). Databases **Week 21** is **transactions, isolation, and recovery** (not a repeat of Week 20).

---

## How to use this syllabus

Each week follows the same template:
- **Learning objectives** (3–5 bullets)
- **Read/watch** (core chapters/lectures; ~h estimates)
- **Exercises** (step‑by‑step tasks or problem sets)
- **Project milestone** (spec + acceptance criteria + stretch)
- **Quick check** (3 short self‑quiz prompts)

**What to submit each week (checklist):**
- [ ] A short **lab report** (≤1 page) noting what you tried, evidence (cmd output, screenshots, or test logs), and what you learned.
- [ ] **Repo link** (GitHub) with code, README, and a `TESTING.md` or usage instructions.
- [ ] **1–2 paragraph reflection** on failures and next steps.

**Assessment rubric (lightweight):**
- Completeness (40%), Correctness (40%), Clarity/Reflection (20%).

---

## Core references (top‑level links)

- CS50x (free): https://cs50.harvard.edu/x/
- Nand2Tetris (course book/website): https://www.nand2tetris.org/
- Nand2Tetris Part I (Coursera): https://www.coursera.org/learn/build-a-computer
- Nand2Tetris Part II (Coursera): https://www.coursera.org/learn/nand2tetris2
- OSTEP (Operating Systems: Three Easy Pieces — free): https://pages.cs.wisc.edu/~remzi/OSTEP/
- Minix 3 (for Tanenbaum OS book context): https://www.minix3.org/
- Patterson & Hennessy (COD, RISC‑V ed. — publisher page): https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/9780128203316
- CMU 15‑445/645 (Intro to DB Systems): https://15445.courses.cs.cmu.edu/
- PostgreSQL Docs (Transactions/Isolation): https://www.postgresql.org/docs/current/transaction-iso.html
- MDN Web Docs (HTTP): https://developer.mozilla.org/docs/Web/HTTP
- RFC 8446 (TLS 1.3): https://www.rfc-editor.org/rfc/rfc8446

> You will **not** read every page of every text; weekly sections specify exact chapters/sections.

---

## At‑a‑Glance (themes by week)

**Week 0 (Onboarding)** · environment, Git/GitHub, tooling  
**1** Programming foundations in C & Python · **2** Testing & CLI tools · **3** Discrete Math I (logic, sets) · **4** Discrete Math II (proofs, combinatorics)  
**5** Data Structures I · **6** Data Structures II · **7** Algorithms I (asymptotics) · **8** Algorithms II (graphs)  
**9** N2T P1–P2 (logic gates & ALU) · **10** N2T P3 (sequential logic / memory) · **11** N2T P4 (+ start P5 CPU) · **12** Finish P5 CPU (+ optional P6 assembler)  
**13** Architecture w/ COD (datapath/ISA) · **14** Architecture (memory/cache) · **15** OS I (processes, syscalls) · **16** OS II (scheduling, sync)  
**17** OS III (virtual memory & files) · **18** Networking I (sockets, TCP intro) · **19** HTTP/HTTPS/TLS & APIs · **20** Databases I (SQL, schema, indexing)  
**21** Databases II (**transactions, isolation, recovery**) · **22** Software Eng I (requirements, design) · **23** Tooling & Git internals · **24** HCI & accessibility  
**25** Security I (crypto basics) · **26** Security II (web/app sec) · **27** Theory I (automata, regex) · **28** Theory II (CFGs, TMs, decidability)  
**29** Compilers I (lexing/parsing) · **30** Compilers II (semantic/IR) · **31** Compilers III (opt/codegen) · **32** Distributed I (RPC, time)  
**33** Distributed II (consistency, CAP) · **34** Cloud & DevOps (containers, CI/CD) · **35** ML I (foundations) · **36** ML II (practice)  
**37** Graphics I (raster pipeline) · **38** Graphics II (shaders) · **39** Net perf & observability · **40** Advanced DB (NoSQL, planning)  
**41** Security III (applied crypto) · **42** HCI II (usability studies) · **43** Software Eng II (architecture patterns)  
**44** Capstone: proposal & design doc · **45** Capstone sprint 1 · **46** Capstone sprint 2 · **47** Capstone sprint 3 · **48** Capstone sprint 4  
**49** Capstone hardening (testing, perf) · **50** Capstone packaging & deploy · **51** Capstone docs & demo · **52** Capstone defense & retrospective

---

# Week‑by‑Week

### Week 0 — Onboarding (optional; outside the 52‑week clock)
**Objectives**
- Prepare macOS dev environment (Homebrew, VS Code, terminals, shells).
- Configure Git, GitHub, SSH keys; set up Python, Node, and C toolchains.
- Establish a clean repo template with CI test workflow.

**Read/Watch (~3h)**
- CS50x “C” intro (selected lectures) — 1.5h  
- GitHub Docs: SSH keys & README conventions — 0.5h  
- VS Code + Terminal shortcuts — 1h

**Exercises**
- Install: `brew`, `python3`, `pipx`, `node`, `clang`, `cmake`, `make`.
- Create a **mono‑repo** with `src/`, `labs/`, `projects/`, `docs/`, `scripts/`.
- Add GitHub Actions runner that runs unit tests on push.

**Project milestone**
- “Hello, toolchain”: C “hello”, Python script, and simple CLI with `argparse`, all tested via a single `make test` target.  
**Accept:** CI green on PR; README explains build/run; `pre-commit` hooks lint.  
**Stretch:** Devcontainer or Nix flake for reproducible env.

**Quick check**
- What does `-Wall -Wextra -O2` do for `clang`?  
- Why use SSH over HTTPS for Git pushes?  
- Show a minimal Makefile target that compiles `main.c` to `main`.

---

### Week 1 — Foundations in C & Python (CS50 refreshers)
**Objectives**
- Write small programs in C and Python; understand compilation vs interpretation.
- Manage memory in C at a basic level; practice debugging.
- Build command‑line apps with arguments and tests.

**Read/Watch (~6–8h)**
- CS50x Weeks on **C**, **Memory**, **Python** (selected) — 5–6h  
- “The C Programming Language” (K&R) ch.1–2 (skim) — 1–2h

**Exercises**
- C: implement `atoi`, `strdup`, and a bounded `getline` clone (tests).
- Python: build `csv_inspect.py` supporting `--head`/`--stats` subcommands.

**Project milestone**
- **Mini utilities pack** (`binutils/`): a C `wc`‑like tool and Python CSV inspector with tests.  
**Accept:** All unit tests pass; no leaks under **Valgrind** (Linux) or **AddressSanitizer/LeakSanitizer** (macOS).  
**Stretch:** Package Python tool with `pipx` entry point.

**Quick check**
- Difference between stack and heap?  
- Why are C strings NUL‑terminated?  
- What does `-fsanitize=address` catch?

---

### Week 2 — Testing, Debugging & CLI ergonomics
**Objectives**
- Apply TDD to small programs; write reproducible tests.
- Use sanitizers, coverage, and linters.
- Design ergonomic CLI UX (subcommands, help, exit codes).

**Read/Watch (~4–5h)**
- CS50x “Testing” resources — 1–2h  
- Google C++ Testing Guide (concepts apply) — 1h  
- Python `unittest`/`pytest` intro — 1–2h

**Exercises**
- Add CI coverage gate (e.g., ≥80%).  
- Introduce `-fsanitize` and fail builds on UB.  
- Write property‑based tests for a pure function.

**Project milestone**
- Convert Week 1 utilities to **TDD workflow**; integrate `--verbose` and `--json`.  
**Accept:** Coverage gate enforced; helpful `--help`.  
**Stretch:** Golden‑file tests for CLI output.

**Quick check**
- What’s a flaky test and how to avoid it?  
- Exit code conventions for Unix CLIs?  
- One benefit of property‑based testing?

---

### Week 3 — Discrete Math I (logic, sets, functions)
**Objectives**
- Propositional logic, predicates, basic set theory, functions/relations.
- Translate English statements into logic formulas.
- Use logic to reason about code.

**Read/Watch (~5–6h)**
- Discrete Math notes (logic/sets basics) — 3h  
- CS50 probability/logic recap — 2–3h

**Exercises**
- Truth tables for tricky conditions; simplify with De Morgan’s laws.
- Prove correctness of a simple loop invariant.

**Project milestone**
- **Predicate checker**: parse a subset of logical formulas and evaluate on assignments.  
**Accept:** Handles ∧, ∨, ¬, →, ↔ with parentheses.  
**Stretch:** CNF/DNF conversion.

**Quick check**
- Difference: implication vs equivalence?  
- Define injective vs surjective functions.  
- Example invariant for a sum loop?

---

### Week 4 — Discrete Math II (proofs, combinatorics)
**Objectives**
- Proof techniques: direct, contrapositive, contradiction, induction.
- Counting, permutations, combinations; Pigeonhole principle.
- Apply to algorithm analysis.

**Read/Watch (~5–6h)**
- Induction & combinatorics notes — 3h  
- Selected MIT OCW videos — 2–3h

**Exercises**
- Prove correctness by induction on input size.  
- Derive a closed‑form count for a simple combinatorial problem.

**Project milestone**
- **Binomial toolkit** with exact and approximate (Stirling) calculations.  
**Accept:** Cross‑checks match within error bounds.  
**Stretch:** Visualize growth vs factorial.

**Quick check**
- Weak vs strong induction?  
- Stars‑and‑bars use case?  
- Pigeonhole principle example in hashing?

---

### Week 5 — Data Structures I
**Objectives**
- Arrays, linked lists, stacks, queues; amortized analysis for dynamic arrays.
- Implement generic containers with tests.
- Big‑O for common operations.

**Read/Watch (~4–6h)**
- Standard DS lectures/notes — 3–4h  
- CS50 DS segments — 1–2h

**Exercises**
- Implement `vector`, `stack`, `queue` in C; Python wrappers for benchmarking.

**Project milestone**
- **Containers lib** with benchmarks for push/pop/enqueue/dequeue.  
**Accept:** Asymptotic behavior demonstrated; tests pass.  
**Stretch:** Circular buffer queue.

**Quick check**
- Why amortized O(1) append?  
- Tradeoffs: array vs linked list?  
- Sentinel nodes?

---

### Week 6 — Data Structures II
**Objectives**
- Trees, heaps, hash tables; collisions & load factor.
- Balanced BSTs: AVL or Red–Black (overview + library use).
- Priority queues and uses.

**Read/Watch (~4–6h)**
- Heaps & hashing lectures — 2–3h  
- Balanced trees overview — 2–3h

**Exercises**
- Implement binary heap; open addressing hash table with tests.

**Project milestone**
- **Task scheduler** using a heap‑based priority queue.  
**Accept:** Stable ordering; O(log n) operations.  
**Stretch:** Calendar import/export.

**Quick check**
- Heap vs binary search tree difference?  
- Hash table load factor impact?  
- Why tree rotations?

---

### Week 7 — Algorithms I (asymptotics, sorting, recursion)
**Objectives**
- Analyze time/space; master method basics.
- Sorting (merge/quick/heap); stability vs in‑place.
- Recursion vs iteration; tail recursion.

**Read/Watch (~5–6h)**
- Algorithms notes/lectures — 3–4h  
- CS50 algorithms week — 2h

**Exercises**
- Implement and benchmark sorts; visualize comparisons.  
- Solve 3–4 recursion problems with proofs of correctness.

**Project milestone**
- **Sort suite** CLI benchmarking tool with CSV output.  
**Accept:** Clear charts for n up to 1e6 (where practical).  
**Stretch:** External/streaming sort.

**Quick check**
- Define Θ, O, Ω.  
- QuickSort worst case and fix?  
- Stability: why care?

---

### Week 8 — Algorithms II (graphs)
**Objectives**
- Graph representations; BFS/DFS; shortest paths; MSTs.
- Topological sort; cycle detection.
- Practical uses (dependency resolution).

**Read/Watch (~4–6h)**
- Graph algorithms lectures — 3–4h  
- Toposort notes — 1–2h

**Exercises**
- Implement BFS/DFS/Dijkstra/Kruskal; compare adjacency list vs matrix.

**Project milestone**
- **Dependency resolver** for a small package graph.  
**Accept:** Detects cycles, outputs build order.  
**Stretch:** Visualize with DOT.

**Quick check**
- When use BFS over Dijkstra?  
- MST vs shortest path differences?  
- DAG definition?

---

### Week 9 — Nand2Tetris **P1–P2** (Logic Gates & **ALU**)
**Objectives**
- Build logic chips from NAND; design & verify an ALU.
- Boolean algebra & hardware description language (HDL) testing.
- Two’s complement basics & ALU flags.

**Read/Watch (~6–8h)**
- N2T Part I: Chapters 1–2 (Projects 1–2).

**Exercises**
- Implement chips up through ALU; pass provided test scripts.

**Project milestone**
- **Working ALU** with correct zero/negative flags.  
**Accept:** All N2T tests pass.  
**Stretch:** Extend ALU with bitwise ops and status flags visualization.

**Quick check**
- Prove De Morgan’s on your chip library.  
- Role of multiplexers?  
- Why two’s complement?

---

### Week 10 — Nand2Tetris **P3** (Sequential Logic / **Memory**)
**Objectives**
- Flip‑flops, registers, and RAM hierarchy.
- Timing & clocked storage; program counter.
- HDL testing methodology for sequential circuits.

**Read/Watch (~6–8h)**
- N2T Part I: Chapter 3 (Project 3).

**Exercises**
- Implement bit/register/RAM/PC; verify with supplied tests.

**Project milestone**
- **RAM & PC** pass full test suite.  
**Accept:** All P3 tests pass.  
**Stretch:** Simple memory visualizer.

**Quick check**
- Latches vs flip‑flops?  
- Why synchronous design?  
- PC role in fetch‑execute?

---

### Week 11 — Nand2Tetris **P4** (Machine Language) + start **P5** (CPU)
**Objectives**
- Hack assembly language and instruction formats.
- CPU control logic; instruction decoding.
- Testing programs on the CPU simulator.

**Read/Watch (~6–8h)**
- N2T Part I: Chapter 4 (Project 4) and begin Chapter 5.

**Exercises**
- Write small ASM programs; start wiring CPU control path.

**Project milestone**
- **Complete P4** and **partial P5** with instruction decode.  
**Accept:** P4 tests pass; P5 passes unit tests for ALU/control integration.  
**Stretch:** Add simple tracing of executed instructions.

**Quick check**
- C‑instruction fields?  
- ROM vs RAM usage?  
- Fetch–decode–execute overview?

---

### Week 12 — Finish **P5** (CPU) + optional **P6** (Assembler)
**Objectives**
- Complete CPU integration; optional assembler translation pipeline.
- End‑to‑end run: program counter, control, ALU, memory.
- Test, debug, and measure cycle counts.

**Read/Watch (~6–8h)**
- N2T Part I: finish Chapter 5; optional Chapter 6 (assembler).

**Exercises**
- Finalize CPU; optionally implement a two‑pass assembler.

**Project milestone**
- **Working CPU** (P5) and, if time, **assembler** (P6).  
**Accept:** All N2T tests pass.  
**Stretch:** Micro‑benchmark your CPU (cycles per program).

**Quick check**
- Instruction decode signals you added?  
- Two‑pass assembler rationale?  
- What’s the reset vector?

---

### Week 13 — Architecture with **COD** (ISA & datapath)
**Objectives**
- Map N2T concepts to a real RISC‑V ISA.
- Understand datapath, control, and pipelines (overview).
- Relate assembly to compiled C.

**Read/Watch (~5–7h)**
- COD (RISC‑V): selected chapters on ISA & datapath — 4–5h  
- Short RISC‑V assembly primer — 1–2h

**Exercises**
- Disassemble simple C functions and explain instruction sequences.

**Project milestone**
- **RISC‑V lab**: write a few functions in assembly; verify via tests.  
**Accept:** Matches C outputs & calling conventions.  
**Stretch:** Inline asm in a C function.

**Quick check**
- RISC vs CISC tradeoffs?  
- Calling convention basics?  
- Pipeline hazards (high level)?

---

### Week 14 — Architecture (memory hierarchy & performance)
**Objectives**
- Caches (direct, assoc., set‑assoc.), locality, prefetching.
- Memory hierarchy & performance tuning.
- Basic profiling.

**Read/Watch (~5–6h)**
- COD memory hierarchy chapter — 3–4h  
- Cache simulation notes — 1–2h

**Exercises**
- Write cache‑friendly vs cache‑hostile loops; measure differences.

**Project milestone**
- **Cache simulator** exploring policies/associativity.  
**Accept:** Reproduces known patterns (e.g., stride effects).  
**Stretch:** Prefetch experiment.

**Quick check**
- Spatial vs temporal locality?  
- Why write‑back vs write‑through?  
- Cache thrashing example?

---

### Week 15 — Operating Systems I (processes & syscalls)
**Objectives**
- Process model; fork/exec; file descriptors & pipes.
- Syscall boundary; user vs kernel mode.
- Build simple shell utilities.

**Read/Watch (~6–8h)**
- Tanenbaum OS (MINIX3) chapters on processes/syscalls — 3–4h  
- OSTEP processes/syscalls chapters — 3–4h

**Exercises**
- Implement `ps-small`:
  - **macOS**: use `libproc` / `proc_pidinfo` or `sysctl` to enumerate processes (no `/proc` exists).
  - **Linux**: read from `/proc` (e.g., `/proc/<pid>/stat`).  
- Build a tiny `myshell` with piping and redirection.

**Project milestone**
- **Mini shell** supporting `|`, `>`, `<`, and background `&`.  
**Accept:** Correct parsing & exit codes; robust to Ctrl‑C.  
**Stretch:** Job control (fg/bg).

**Quick check**
- Difference between process and thread?  
- What’s a file descriptor?  
- Blocking vs non‑blocking I/O?

---

### Week 16 — Operating Systems II (scheduling & synchronization)
**Objectives**
- CPU scheduling (FCFS, RR, MLFQ).  
- Mutexes, semaphores, deadlock basics.
- Measuring latency vs throughput.

**Read/Watch (~5–7h)**
- OSTEP scheduling & concurrency chapters — 4–5h  
- Minimal POSIX threads intro — 1–2h

**Exercises**
- Simulate schedulers; write a producer‑consumer with a bounded buffer.

**Project milestone**
- **Thread pool** library with work queue and tests.  
**Accept:** Correctness under load; clean shutdown.  
**Stretch:** Priority scheduling.

**Quick check**
- Convoy effect?  
- Necessary conditions for deadlock?  
- Preemptive vs cooperative scheduling?

---

### Week 17 — Operating Systems III (virtual memory & files)
**Objectives**
- Paging, TLBs, page faults; address translation.
- Filesystems basics; inodes, allocation, journaling (high level).
- Memory‑mapped files.

**Read/Watch (~5–7h)**
- OSTEP VM and filesystem chapters — 5–7h

**Exercises**
- Page table walk exercise; mmap a file and scan quickly.

**Project milestone**
- **KV store** backed by memory‑mapped file.  
**Accept:** Crash‑safe write path; unit tests.  
**Stretch:** Simple WAL with checksums.

**Quick check**
- Page vs frame?  
- TLB role?  
- Why journaling?

---

### Week 18 — Networking I (sockets & TCP intro)
**Objectives**
- OSI vs TCP/IP; ports & sockets.
- TCP handshake, flow control; blocking vs non‑blocking sockets.
- Concurrent servers (process, thread, evented).

**Read/Watch (~5–6h)**
- Intro networking lectures — 3–4h  
- Socket programming guide — 2h

**Exercises**
- Build a concurrent **echo** server (thread pool or epoll/kqueue).

**Project milestone**
- **Echo server** handling thousands of clients in tests.  
**Accept:** Measured throughput & latency; clean shutdown.  
**Stretch:** TLS‑terminating proxy (placeholder for Week 19).

**Quick check**
- SYN backlog purpose?  
- Why Nagle’s algorithm?  
- Blocking vs non‑blocking accept?

---

### Week 19 — **HTTP/HTTPS/TLS** & Web APIs (corrected)
**Objectives**
- HTTP request/response semantics (methods, status codes, headers, caching).
- HTTPS/TLS: certificates, handshake (TLS 1.3 overview), hostname verification.
- Robust client behaviors: timeouts, retries, redirects; idempotency & safety.

**Read/Watch (~5–7h)**
- MDN HTTP overview & caching — 2–3h  
- TLS 1.3 (RFC 8446 high‑level sections) — 1–2h  
- REST & pagination patterns — 1–2h

**Exercises**
- Implement an **HTTP client** that:
  - Validates TLS certs & hostnames.
  - Follows redirects (limit depth).
  - Applies exponential backoff **only** for idempotent methods (GET, HEAD, PUT, DELETE, OPTIONS, TRACE).
  - Enforces timeouts and surfaces structured errors.


**Note:** Although **TRACE** is specified as idempotent, many servers disable it for security reasons (request echo can expose sensitive headers). Do not rely on TRACE being available, and avoid enabling it in production.

**Project milestone**
- **Resilient HTTP client** CLI with `GET/HEAD/PUT` and `--retry`/`--timeout`/`--cacert`.  
**Accept:** Integration tests against a local test server.  
**Stretch:** Conditional requests with `ETag`/`If‑None‑Match` and cache.

**Quick check**
- Difference between **301** and **308**?  
- What makes a method **idempotent**?  
- Outline the server‑auth step in TLS.

---

### Week 20 — Databases I (relational model, SQL, indexing)
**Objectives**
- Relational model & schema design; normalization.
- Query planning basics; B‑trees & indexes.
- ACID (high level).

**Read/Watch (~5–7h)**
- CMU 15‑445: Intro/relational/SQL/indexing lectures — 4–5h  
- PostgreSQL: indexes overview — 1–2h

**Exercises**
- Design a normalized schema; index critical queries; measure with `EXPLAIN ANALYZE`.

**Project milestone**
- **Mini app** with CRUD + proper constraints & indexes.  
**Accept:** Measured speedups from indexes; no obvious anomalies.  
**Stretch:** Partial and composite indexes comparison.

**Quick check**
- Normal forms overview?  
- Covering index definition?  
- Tradeoff: normalization vs query performance?

---

### Week 21 — Databases II (**transactions, isolation, recovery**) — *corrected*
**Objectives**
- Transactions & **ACID** guarantees in depth.
- Isolation levels: read committed, repeatable read, serializable.
- Concurrency control (2PL vs **MVCC**), write‑ahead logging (**WAL**) & recovery.

**Read/Watch (~5–7h)**
- CMU 15‑445: Transactions, Concurrency Control, Logging/Recovery — 4–5h  
- PostgreSQL docs: transactions & isolation — 1–2h

**Exercises**
- Demonstrate **lost update**, **non‑repeatable read**, **phantoms**; then eliminate by changing isolation or adding indexes.  
- Simulate a crash and verify **WAL‑style** recovery on a tiny prototype.

**Project milestone**
- **TXN lab** with harness reproducing anomalies and fixes; short report.  
**Accept:** Reproducible anomalies + explanation of fixes.  
**Stretch:** Serializable snapshot isolation demo.

**Quick check**
- Define **serializability**.  
- Compare 2PL vs MVCC.  
- What property does WAL ensure?

---

### Week 22 — Software Engineering I (requirements & design)
**Objectives**
- Requirements elicitation; use cases; user stories.
- Architecture drivers; tradeoff analysis.
- Testing strategy & CI/CD setup.

**Read/Watch (~4–6h)**
- Classic SE notes on requirements & design — 3–4h  
- Testing strategy overviews — 1–2h

**Exercises**
- Write a concise **design doc** template; adopt ADRs.

**Project milestone**
- **Design doc** for your capstone candidate (choose domain).  
**Accept:** Clear goals, risks, MVP scope, and test plan.  
**Stretch:** Lightweight cost/benefit analysis.

**Quick check**
- Non‑functional requirement examples?  
- What is an ADR?  
- Test pyramid idea?

---

### Week 23 — Tooling Deep Dive & Git Internals
**Objectives**
- Git object model (blobs, trees, commits); refs and `rebase` safely.
- Packaging & dependency management (Python, Node).
- Build systems & reproducibility basics.

**Read/Watch (~4–6h)**
- Git internals notes/videos — 2–3h  
- Packaging best practices — 2–3h

**Exercises**
- Inspect `.git/objects`; manually craft a commit.  
- Build & publish a small Python package locally.

**Project milestone**
- **Release pipeline** for an earlier project with semantic versioning.  
**Accept:** Tagged releases with changelog; reproducible builds.  
**Stretch:** SBOM generation.

**Quick check**
- Detached HEAD?  
- When to rebase vs merge?  
- Lockfile purpose?

---

### Week 24 — HCI & Accessibility
**Objectives**
- Principles of usable interfaces; heuristics evaluation.
- Accessibility (WCAG); keyboard navigation; color contrast.
- User testing basics.

**Read/Watch (~4–5h)**
- Nielsen heuristics & WCAG intro — 3–4h  
- Short videos on usability tests — 1h

**Exercises**
- Heuristic eval of a small app; add a11y fixes.

**Project milestone**
- **Accessible UI** for your mini app (Week 20).  
**Accept:** Passes basic a11y checks; keyboard‑only flow works.  
**Stretch:** Screen‑reader friendly ARIA landmarks.

**Quick check**
- Contrast ratio target?  
- Focus management basics?  
- Example of a common a11y pitfall?

---

### Week 25 — Security I (crypto basics)
**Objectives**
- Threat modeling; symmetric vs asymmetric crypto.
- Hashes, MACs, signatures; key exchange (high level).
- Secure storage basics.

**Read/Watch (~4–6h)**
- Applied crypto intro lectures — 3–4h  
- Practical key management docs — 1–2h

**Exercises**
- HMAC vs raw hash experiment; tamper detection.

**Project milestone**
- **Secrets manager** skeleton with envelope encryption.  
**Accept:** Keys never stored plaintext; tests cover misuse.  
**Stretch:** Hardware‑backed keys if available.

**Quick check**
- Hash vs MAC?  
- What is forward secrecy?  
- Salt vs pepper?

---

### Week 26 — Security II (web/app sec)
**Objectives**
- OWASP Top 10; input validation, authn/z, CSRF, SSRF.
- Secure session handling & cookies.
- Dependency risk management.

**Read/Watch (~4–6h)**
- OWASP Top 10 — 2–3h  
- Secure coding guidelines — 2–3h

**Exercises**
- Exploit then patch a small vulnerable web app.

**Project milestone**
- **Hardened app** with CSP, CSRF tokens, and safe secrets use.  
**Accept:** Automated security tests pass.  
**Stretch:** SAST/DAST in CI.

**Quick check**
- CSRF vs XSS?  
- Why SameSite cookies?  
- SSRF prevention?

---

### Week 27 — Theory of Computation I (automata, regex)
**Objectives**
- DFAs/NFAs; regular expressions; closure properties.
- Limits of regular languages.
- Practical regex engine behavior.

**Read/Watch (~4–5h)**
- Automata basics lectures — 3–4h  
- Regex pitfalls reading — 1h

**Exercises**
- Convert NFA↔DFA; build a tiny regex matcher.

**Project milestone**
- **Regex engine** subset with Thompson’s construction.  
**Accept:** Passes suite of patterns.  
**Stretch:** Backtracking vs NFA comparison.

**Quick check**
- Pumping lemma (intuition)?  
- Greedy vs lazy quantifiers?  
- Character classes vs alternation?

---

### Week 28 — Theory of Computation II (CFGs, TMs, decidability)
**Objectives**
- Context‑free grammars & pushdown automata (overview).
- Turing machines; decidability; reductions.
- Complexity classes (P, NP) at a high level.

**Read/Watch (~4–6h)**
- Theory lectures — 4–5h  
- Short NP‑completeness overview — 1h

**Exercises**
- Design CFGs for simple languages; prove a problem undecidable by reduction (outline).

**Project milestone**
- **Parser** for a small CFG (pairs with Week 29 compiler).  
**Accept:** Passes grammar tests.  
**Stretch:** Ambiguity resolution.

**Quick check**
- Why CFGs for programming languages?  
- Halting problem statement?  
- Reduction intuition?

---

### Week 29 — Compilers I (lexing & parsing)
**Objectives**
- Lexical analysis; tokenization.
- Parsing (LL/LR basics); AST construction.
- Error reporting and recovery.

**Read/Watch (~5–7h)**
- Compiler lectures on lexing/parsing — 4–5h  
- Parsing tool docs — 1–2h

**Exercises**
- Build a lexer and parser for the Week 28 grammar.

**Project milestone**
- **Front‑end** that outputs an AST for a tiny language.  
**Accept:** Robust error messages.  
**Stretch:** Pretty printer.

**Quick check**
- FIRST/FOLLOW sets (intuition)?  
- Shift/reduce conflict?  
- Token vs lexeme?

---

### Week 30 — Compilers II (semantic analysis & IR)
**Objectives**
- Scopes, symbol tables, and type checking.
- Intermediate representations (CFG, SSA overview).
- Simple optimizations (constant folding).

**Read/Watch (~4–6h)**
- Semantic analysis lectures — 3–4h  
- IR & optimization overview — 1–2h

**Exercises**
- Type checker for your AST; emit a simple IR.

**Project milestone**
- **Semantic pass** + IR generator; constant folding.  
**Accept:** Catches type errors; tests pass.  
**Stretch:** Liveness analysis sketch.

**Quick check**
- Static vs dynamic typing?  
- Purpose of SSA?  
- Why separate front‑end/IR/back‑end?

---

### Week 31 — Compilers III (codegen & opt)
**Objectives**
- Code generation to a VM or native (simplified).
- Register allocation (high level).
- Peephole optimizations.

**Read/Watch (~4–6h)**
- Backend/codegen lectures — 3–4h  
- Register allocation overview — 1–2h

**Exercises**
- Emit bytecode for a tiny VM; write an interpreter.

**Project milestone**
- **Runnable programs** for your tiny language.  
**Accept:** End‑to‑end from source to execution.  
**Stretch:** Bytecode JIT (toy).

**Quick check**
- Calling convention role?  
- Why IR before codegen?  
- Constant folding vs CSE?

---

### Week 32 — Distributed Systems I (RPC, time, failure)
**Objectives**
- RPC and service boundaries; time & clocks (NTP, logical clocks).
- Failure modes; retries; idempotency.
- Health checks & timeouts.

**Read/Watch (~4–6h)**
- Distributed basics lectures — 3–4h  
**Note:** For timeouts, backoff timers, and latency measurements, use a **monotonic clock** (e.g., `clock_gettime(CLOCK_MONOTONIC)` or language equivalent). Avoid wall‑clock time, which can jump.

- Time & clocks notes — 1–2h

**Exercises**
- Implement RPC over HTTP with clear timeouts and tracing IDs.

**Project milestone**
- **Two‑service demo** with request IDs and retry policies.  
**Accept:** Observability (logs/metrics/traces).  
**Stretch:** Exponential backoff with jitter and circuit breaker.

**Quick check**
- Why monotonic clocks?  
- Retry storm risk?  
- Heartbeat vs health probe?

---

### Week 33 — Distributed Systems II (consistency & CAP)
**Objectives**
- Replication; leader election concepts.
- Consistency models; CAP theorem.
- Eventual consistency tradeoffs.

**Read/Watch (~4–6h)**
- Consistency lectures — 3–4h  
- CAP deep dive — 1–2h

**Exercises**
- Build a replicated log (toy) with leader election (mock).

**Project milestone**
- **Toy consensus** (simplified Raft) for a key/value service.  
**Accept:** Handles leader failover in tests.  
**Stretch:** Log compaction sketch.

**Quick check**
- Linearizability (intuition)?  
- Partition tolerance consequence?  
- Quorum reads/writes?

---

### Week 34 — Cloud & DevOps
**Objectives**
- Containers & images; orchestration concepts.
- CI/CD pipelines; blue‑green vs canary.
- Observability: logs, metrics, tracing.

**Read/Watch (~4–6h)**
- Docker fundamentals — 2–3h  
- CI/CD patterns — 2–3h

**Exercises**
- Containerize an app; add a pipeline with tests and rollout.

**Project milestone**
- **Deployable service** with health checks and dashboards.  
**Accept:** Rollback path documented.  
**Stretch:** IaC for dev environment.

**Quick check**
- Image layers?  
- Canary vs blue‑green?  
- SLO vs SLI?

---

### Week 35 — Machine Learning I (foundations)
**Objectives**
- Supervised learning basics; data splits; evaluation metrics.
- Linear/logistic regression; regularization.
- Feature engineering basics.

**Read/Watch (~5–7h)**
- ML crash course/video series — 4–5h  
- Metrics & validation notes — 1–2h

**Exercises**
- Train and evaluate baseline models; avoid leakage.

**Project milestone**
- **ML baseline** for a tabular dataset; report metrics.  
**Accept:** Proper CV; reproducible training.  
**Stretch:** Hyperparameter search script.

**Quick check**
- Bias–variance tradeoff?  
- Precision vs recall?  
- Regularization purpose?

---

### Week 36 — Machine Learning II (practice)
**Objectives**
- Trees/ensembles; simple neural nets.
- Data pipelines; reproducibility.
- Model serving basics.

**Read/Watch (~4–6h)**
- Trees/ensembles lectures — 2–3h  
- Intro NN videos — 2–3h

**Exercises**
- Train tree‑based models; compare to Week 35 baselines.

**Project milestone**
- **Model service** with REST endpoint and input validation.  
**Accept:** Deterministic inference; latency measured.  
**Stretch:** Model versioning & A/B test.

**Quick check**
- Overfitting signs?  
- Why a hold‑out set?  
- Feature drift?

---

### Week 37 — Computer Graphics I (raster pipeline)
**Objectives**
- 2D/3D pipeline overview; transformations.
- Rasterization and depth buffering.
- Image formats & gamma.

**Read/Watch (~4–6h)**
- Graphics pipeline lectures — 3–4h  
- Rasterization notes — 1–2h

**Exercises**
- Implement triangle rasterizer (software).

**Project milestone**
- **Mini renderer** drawing transformed meshes.  
**Accept:** Depth buffering & simple shading.  
**Stretch:** Texture mapping.

**Quick check**
- Model–view–projection?  
- Why depth buffer?  
- Aliasing vs antialiasing?

---

### Week 38 — Computer Graphics II (shaders)
**Objectives**
- Shaders & programmable pipeline.
- Lighting models.
- GPU vs CPU compute basics.

**Read/Watch (~4–6h)**
- Shader programming intro — 2–3h  
- Lighting models overview — 1–2h

**Exercises**
- Write simple vertex & fragment shaders.

**Project milestone**
- **Shader demo** with interactive controls.  
**Accept:** Stable FPS; documented effects.  
**Stretch:** Post‑processing pass.

**Quick check**
- Vertex vs fragment shader?  
- Phong vs Lambertian?  
- GPU parallelism idea?

---

### Week 39 — Networking: performance & observability
**Objectives**
- Throughput vs latency; head‑of‑line blocking; HTTP/2 basics.
- Measuring with `tcpdump`/`wireshark`/`curl` timings.
- Capacity planning.

**Read/Watch (~4–6h)**
- HTTP/2 overview — 1–2h  
**Note:** HTTP/2 multiplexes streams over a single TCP connection and can still suffer **transport-level head-of-line (HOL) blocking**. **HTTP/3 (QUIC)** moves multiplexing to UDP and mitigates transport HOL. If your stack allows it, try an HTTP/3 run as an optional experiment.

- Network profiling notes — 3–4h

**Exercises**
- Measure performance of your HTTP client/server.

**Project milestone**
- **Perf report** with flamegraphs or pprof‑style profiles.  
**Accept:** Identifies bottlenecks; proposed fixes.  
**Stretch:** HTTP/2 experiment.

**Quick check**
- HOL blocking?  
- P95 vs P99?  
- Why keep‑alive?

---

### Week 40 — Advanced Databases (NoSQL, OLAP, planning)
**Objectives**
- NoSQL models (KV, document, column, graph).
- Query planners; cost‑based decisions.
- OLAP basics; denormalization tradeoffs.

**Read/Watch (~4–6h)**
- NoSQL survey — 2–3h  
- Query planning notes — 2–3h

**Exercises**
- Compare query plans on star vs snowflake schemas.

**Project milestone**
- **Reporting pipeline** generating an analytic dashboard.  
**Accept:** Clear ETL steps & indexes.  
**Stretch:** Columnar storage experiment.

**Quick check**
- Star vs snowflake?  
- Why statistics in planners?  
- Graph DB suitable cases?

---

### Week 41 — Security III (applied crypto)
**Objectives**
- TLS in practice; certificates, PKI.
- Token‑based auth (JWT pitfalls).
- Secrets rotation & audit.

**Read/Watch (~4–6h)**
- TLS operations notes — 2–3h  
- JWT best practices — 1–2h

**Exercises**
- Rotate keys and invalidate tokens in a demo service.

**Project milestone**
- **Secure session** layer for earlier app.  
**Accept:** Short‑lived tokens; refresh flow.  
**Stretch:** mTLS between services.

**Quick check**
- Why short token lifetimes?  
- mTLS benefit?  
- Certificate pinning risks?

---

### Week 42 — HCI II (usability studies & data ethics)
**Objectives**
- Plan and run lightweight usability tests.
- Analyze findings; iterate designs.
- Data ethics & privacy considerations.

**Read/Watch (~3–5h)**
- Usability testing guides — 2–3h  
- Privacy by design primer — 1–2h

**Exercises**
- Conduct 3 quick tests; synthesize issues and fixes.

**Project milestone**
- **Usability report** and revised UI.  
**Accept:** Fixes verified by repeat test.  
**Stretch:** Accessibility audit redo.

**Quick check**
- Qual vs quant UX data?  
- Consent in user studies?  
- Example of dark pattern?

---

### Week 43 — Software Engineering II (architecture patterns)
**Objectives**
- Layered, modular, microservices vs monolith tradeoffs.
- Domain‑driven design (lightweight).
- Observability and operability as design drivers.

**Read/Watch (~4–6h)**
- Architecture pattern notes — 3–4h  
- DDD intro — 1–2h

**Exercises**
- Decompose a monolith into modules; define interfaces.

**Project milestone**
- **Architecture sketch** for capstone implementation.  
**Accept:** Clear boundaries & ownership.  
**Stretch:** ADRs for key decisions.

**Quick check**
- Bounded context?  
- Shared DB anti‑pattern?  
- Backwards compatibility strategy?

---

### Week 44 — Capstone: proposal & design doc (freeze scope)
**Objectives**
- Select capstone; finalize problem statement & constraints.
- Write comprehensive design doc & roadmap.
- Define MVP and 4 sprints.

**Read/Watch (~2–3h)**
- Review Weeks 22 & 43 materials as needed.

**Exercises**
- Risk matrix; metrics for success; data model sketch.

**Project milestone**
- **Final design doc** committed; issue tracker seeded.  
**Accept:** Team‑of‑one plan is realistic in 8 weeks.  
**Stretch:** Lightweight cost estimate.

**Quick check**
- Three biggest risks?  
- MVP acceptance test?  
- What will you deliberately **not** do?

---

### Week 45 — Capstone: Sprint 1
**Objectives**
- Implement core skeleton; pick the riskiest part first.
- Continuous integration & smoke tests.
- Tracing/logging foundation.

**Read/Watch (~1–2h)** as needed.

**Exercises**
- Spike risky component; define clear exit criteria.

**Project milestone**
- **Sprint 1 demo** with basic end‑to‑end flow.  
**Accept:** “Walking skeleton” runs in CI.  
**Stretch:** Feature flags.

**Quick check**
- What risk burned down this sprint?  
- New risk discovered?  
- Is scope still realistic?

---

### Week 46 — Capstone: Sprint 2
**Objectives**
- Implement major features; harden storage & APIs.
- Expand tests; load test baseline.
- Keep docs updated.

**Project milestone**
- **Sprint 2 demo** with 60–70% feature completion.  
**Accept:** Load test reaches target P95.  
**Stretch:** Chaos test of a dependency.

**Quick check**
- What’s your P95 latency?  
- Which tests guard the riskiest code?  
- What’s the rollback plan?

---

### Week 47 — Capstone: Sprint 3
**Objectives**
- Fill gaps; improve UX/a11y; tackle performance bugs.
- Security review & threat model update.

**Project milestone**
- **Sprint 3 demo** covering all MVP features.  
**Accept:** Security checklist completed.  
**Stretch:** Observability dashboards.

**Quick check**
- Top perf bottleneck now?  
- Any unauthenticated endpoints?  
- a11y gaps?

---

### Week 48 — Capstone: Sprint 4
**Objectives**
- Final features & polish; reduce tech debt.
- Documentation & onboarding guide.
- Prepare release candidate.

**Project milestone**
- **RC build**; release checklist complete.  
**Accept:** No P1 bugs open.  
**Stretch:** Canary rollout in staging.

**Quick check**
- What would break a release today?  
- Any single‑points of failure?  
- What’s left to de‑risk?

---

### Week 49 — Capstone: Hardening (testing, security, perf)
**Objectives**
- End‑to‑end tests; fuzzing (where relevant).
- Security pass (authn/z, secrets, dependencies).
- Performance tuning.

**Project milestone**
- **Hardening report** with evidence and fixes.  
**Accept:** P95/P99 meet targets; security tests pass.  
**Stretch:** SLOs & alerts defined.

**Quick check**
- Fuzz target chosen?  
- Strongest remaining risk?  
- Perf improvement quantified?

---

### Week 50 — Capstone: Packaging & Deploy
**Objectives**
- Reproducible builds; container image.
- One‑click (scripted) deploy.
- Backups & recovery drill.

**Project milestone**
- **Release** with version tag, changelog, and artifacts.  
**Accept:** Fresh clone → build → deploy works.  
**Stretch:** Automated rollback script.

**Quick check**
- What’s your RTO/RPO?  
- Immutable build advantages?  
- Backup restore proven?

---

### Week 51 — Capstone: Docs & Demo
**Objectives**
- Polish docs (README, ARCHITECTURE, OPERATIONS).
- Prepare recorded demo & slides.
- Gather and incorporate feedback.

**Project milestone**
- **Demo video** (≤10 min) + docs.  
**Accept:** A new user can run it in 10 minutes.  
**Stretch:** Public website or landing page.

**Quick check**
- Docs gap a newcomer will hit?  
- Demo flow timeboxed?  
- Next steps after release?

---

### Week 52 — Capstone: Defense & Retrospective; Career prep
**Objectives**
- Defend design & tradeoffs; reflect on the year.
- Map skills to a portfolio and CV.
- Plan continued learning.

**Read/Watch (~2–3h)**
- Interview prep overview; portfolio advice.

**Exercises**
- Write a retrospective; choose 2 areas to go deeper next year.

**Project milestone**
- **Final presentation** + portfolio page linking key repos.  
**Accept:** Clear narrative of problem, approach, and results.  
**Stretch:** Publish a technical blog post.

**Quick check**
- Strongest piece of evidence of skill?  
- What would you re‑sequence in hindsight?  
- Two goals for the next 6 months?

---

## Appendix: Weekly time budget

- Reading/lectures: 3–6h  
- Exercises/labs: 4–6h  
- Project milestone: 2–4h  
- Reflection/report: 0.5–1h

**Total:** ~9.5–17h (target 10–15h; trim stretch goals when busy).

---

## License & attribution

This plan cites and relies on open educational resources, textbooks, and course materials credited in the **Core references**. Use within fair use and the licenses of the respective resources.