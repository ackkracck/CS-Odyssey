# Harvard‑Level CS Self‑Study: 52‑Week Plan (10–15 hrs/week)

*Generated on 2025-09-07.*

> Assumptions: macOS, terminal‑friendly tools, GitHub. Pace: 10–15 hrs/week for 52 weeks. This syllabus integrates **Computer Organization and Design (Patterson & Hennessy)** and **Operating Systems: Design and Implementation (Tanenbaum)** alongside open courses and free texts.

## Table of Contents
- [At‑a‑Glance 52‑Week Table](#at‑a‑glance-52‑week-table)
- [Weekly Plan](#weekly-plan)
- [Rubrics](#rubrics-04-scale)
- [Consolidated Reading List](#consolidated-reading-list-canonical-links)
- [Skills Map](#skills-map-topic--objectives--artifacts)
- [Capstone Specification](#capstone-specification-weeks-4952)

## At‑a‑Glance 52‑Week Table
| Week | Topic | Est. Hours | Major Deliverable |
|---:|---|---:|---|
| 0 | Diagnostic & Setup | 4.5 | Diagnostics & repo scaffolding |
| 1 | Software Construction I (Python) | 12 | Tested CLI utility |
| 2 | Software Construction II (JS) | 11 | Node CLI + tests |
| 3 | Testing & Code Reading | 10 | PR with expanded tests |
| 4 | Software Design & APIs | 12 | HTTP API + tests |
| 5 | DS: Lists/Stacks/Queues | 12 | DS library v1 |
| 6 | DS: Hash Tables | 12 | Hash map |
| 7 | DS: Trees | 12 | Balanced BST |
| 8 | Algorithms: Sorting/Search | 12 | Sorting lib + benchmarks |
| 9 | Arch: Logic | 12 | N2T P1–2 |
| 10 | Arch: ALU | 12 | N2T ALU |
| 11 | Arch: CPU | 12 | N2T CPU |
| 12 | Arch: Memory | 12 | N2T memory |
| 13 | Checkpoint #1 | 8 | Mock exam + refactor |
| 14 | OS: Processes | 12 | Syscall demos |
| 15 | OS: Concurrency | 12 | Threaded lab |
| 16 | OS: Scheduling | 12 | Scheduling lab |
| 17 | OS: Memory | 12 | VM lab |
| 18 | Networking: TCP | 12 | Concurrent echo server |
| 19 | Networking: HTTP/TLS | 12 | HTTP client |
| 20 | DB: Modeling/SQL | 12 | SQL scripts + report |
| 21 | DB: TX/Indexes/Plans | 12 | TX + plans report |
| 22 | SE: Design/Docs | 10 | Docs + review checklist |
| 23 | SE: CI/CD | 11 | CI + container + release |
| 24 | Theory: Automata | 11 | Regex engine + proofs |
| 25 | Theory: Computability/Complexity | 8.5 | Reductions writeup |
| 26 | Checkpoint #2 | 6 | Mock + audit |
| 27 | Security: Crypto | 10.5 | Cryptopals Set 1 |
| 28 | Security: Software/Web | 11 | Threat model + hardening |
| 29 | HCI/UX | 9.5 | Prototype + usability report |
| 30 | Elective A: Compilers I | 11 | Scanner + parser |
| 31 | Elective A: Compilers II | 12 | Interpreter + resolver |
| 32 | Elective A: Compilers III | 12 | Bytecode VM |
| 33 | Elective A: Compilers IV | 10.5 | Optimisations + tools |
| 34 | Elective B: Distributed I | 12 | MapReduce lab |
| 35 | Elective B: Distributed II | 12 | Replicated KV |
| 36 | Elective B: Distributed III | 10.5 | Chaos tests |
| 37 | Elective B: Distributed IV | 10 | Observability suite |
| 38 | Performance & Profiling | 9.5 | Perf report |
| 39 | Checkpoint #3 | 6.5 | Essays + doc polish |
| 40 | Integration: APIs | 10.5 | Compose services |
| 41 | Integration: Deploy | 9.5 | Pipelines |
| 42 | Integration: SRE | 8.5 | SLOs + postmortem |
| 43 | Capstone Proposal & Literature Review | 10.5 | Approved proposal + lit review |
| 44 | Design Doc & Architecture | 10.5 | Design doc + diagrams |
| 45 | Prototype 1: Core Path | 10.5 | Walking skeleton |
| 46 | Prototype 2: Data & Auth | 10.5 | Data model + auth working |
| 47 | Prototype 3: Scale & Resilience | 10.5 | Load test + resilience plan |
| 48 | Final Capstone Plan | 9.5 | Feature-complete plan + test matrix |
| 49 | Capstone Build I | 12 | MVP feature set |
| 50 | Capstone Build II | 12 | Feature complete + tests |
| 51 | Capstone Stabilize | 11 | Perf hardening + docs |
| 52 | Capstone Deliver & Defend | 12 | Deployed app + report + oral defense |

## Weekly Plan

### Week 0: Diagnostic & Setup
**Topic tag:** Onboarding • **Estimated hours:** 4.5h • **Major deliverable:** Completed diagnostics + personalized adjustments

**Learning objectives**
- Verify toolchain on macOS (CLI, Git, Python/Node)
- Demonstrate basic coding fluency with small katas
- Adopt a consistent doc + style workflow


**Read / watch**
- **Pro Git** — Ch. 1–2; init/clone/commit/branch (2h). [Pro Git](https://git-scm.com/book/en/v2)
- **Google Doc Style** — Overview + Accessibility (1h). [Google Doc Style](https://developers.google.com/style/)
- **ACM Code of Ethics** — Read principles (0.5h). [ACM Code of Ethics](https://www.acm.org/code-of-ethics)


**Exercises & problem sets (with solutions/rubric)**
- Install Xcode CLT/Homebrew, Python 3.11+, Node LTS, Git; create `~/cs-portfolio`.
- Set up GitHub SSH keys; create a private repo `cs-portfolio`.
- Run coding diagnostic: implement `fizzbuzz`, `two-sum`, `anagram-check` with `pytest` tests (solutions included).
- Write a 1-page learning plan (hours, risks, mitigation).


**Project milestone**
- **Spec:** Create `cs-portfolio` meta-repo with subfolders per module. Include a top-level README, CONTRIBUTING, and Code of Conduct.
- **Acceptance criteria & tests:** CI passes: lint + unit tests. README lists environment and a 'getting started' section.
- **Repo structure**
```text
onboarding/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Automate dev container with Docker
- Set up GitHub Actions CI pipeline

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is the purpose of a branch in Git?
1. Name two benefits of a style guide for technical docs.
1. State one principle from the ACM Code relevant to student work.


<details>
<summary>Answer key</summary>

1. To isolate changes and enable parallel development/experimentation before merging.
1. Consistency and clarity; reduces ambiguity and cognitive load for readers.
1. Avoid harm / be honest and trustworthy / respect privacy — any valid principle earns credit.


</details>

**Deliverables**
- Diagnostic code + passing tests
- Personal study contract (PDF/MD)
- Repo with CI badge screenshot


---


### Week 1: Software Construction I: Python Craft
**Topic tag:** Programming Foundations • **Estimated hours:** 12h • **Major deliverable:** Tested CLI utility (args, logging, packaging)

**Learning objectives**
- Package Python code; write tests
- Apply formatting & linting
- Use argparse/logging sensibly


**Read / watch**
- **CS50** — Weeks on C/Python for style inspiration; focus on testing & style (2h). [CS50](https://cs50.harvard.edu/x/)
- **pytest** — Quickstart + fixtures (1h). [pytest](https://docs.pytest.org/)
- **Black** — Usage & config (0.5h). [Black](https://black.readthedocs.io/)
- **flake8** — Usage & common rules (0.5h). [flake8](https://flake8.pycqa.org/)


**Exercises & problem sets (with solutions/rubric)**
- Refactor a script into a package with `__main__` entrypoint.
- Add unit tests (≥10) and coverage (≥80%).
- Publish to TestPyPI (optional).


**Project milestone**
- **Spec:** CLI `imgcat` that prints image metadata (size, mode, format) and optional ASCII preview.
- **Acceptance criteria & tests:** `imgcat --help` works; handles errors; tests pass; meets coverage target.
- **Repo structure**
```text
programming-foundations/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add parallel processing for batch files
- Support web images via `requests`

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What’s the difference between unit and integration tests?
1. Why pin dependencies?
1. What’s the purpose of code coverage?


<details>
<summary>Answer key</summary>

1. Unit tests isolate functions; integration tests exercise multiple components.
1. Reproducible builds and fewer surprise upgrades.
1. Rough measure of tested code paths; not a guarantee of quality.


</details>

**Deliverables**
- Source + tests
- Coverage report
- README with usage


---


### Week 2: Software Construction II: JavaScript & Tooling
**Topic tag:** Programming Foundations • **Estimated hours:** 11h • **Major deliverable:** Node CLI with ESLint/Prettier + tests

**Learning objectives**
- Use Node modules; write tests
- Apply JS lint/format
- Parity across languages


**Read / watch**
- **CS50** — JS/Python style & problem-solving patterns (1h). [CS50](https://cs50.harvard.edu/x/)
- **ESLint** — Getting started (0.5h). [ESLint](https://eslint.org/)
- **Prettier** — Getting started (0.5h). [Prettier](https://prettier.io/)


**Exercises & problem sets (with solutions/rubric)**
- Port Week 1 CLI to Node; maintain behavior parity.
- Set up `mocha`/`chai` tests (≥10); configure ESLint + Prettier.


**Project milestone**
- **Spec:** `imgcat-js` mirroring Week 1; streaming file I/O with backpressure.
- **Acceptance criteria & tests:** Same outputs as Python version; lint passes; tests pass.
- **Repo structure**
```text
programming-foundations/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add progress bar for large files
- Add watch mode for directories

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is semantic versioning?
1. Explain event loop vs threads.
1. What’s the role of a linter?


<details>
<summary>Answer key</summary>

1. MAJOR.MINOR.PATCH with breaking changes on MAJOR.
1. Event loop handles async callbacks; threads run in parallel.
1. Enforces code quality rules; catches common errors.


</details>

**Deliverables**
- Node CLI + tests
- Parity test matrix
- README


---


### Week 3: Testing, Debugging, and Code Reading
**Topic tag:** Programming Foundations • **Estimated hours:** 10h • **Major deliverable:** Test suite & bug reports for an existing open-source repo (fork)

**Learning objectives**
- Read unfamiliar code
- Design tests from requirements
- Write good PRs & reviews


**Read / watch**
- **Pro Git** — Ch. on branching/PRs (1h). [Pro Git](https://git-scm.com/book/en/v2)
- **Google Eng Practices (Code Review)** — Standards + How to do a review (1h). [Google Eng Practices (Code Review)](https://google.github.io/eng-practices/review/)


**Exercises & problem sets (with solutions/rubric)**
- Choose a small OSS repo; read code and write a 1–2 page architecture note.
- Add tests to increase coverage by 10–20%; open a PR in your fork.


**Project milestone**
- **Spec:** Increase coverage; write clear PR description; attach before/after test reports.
- **Acceptance criteria & tests:** Tests pass; CI green in your fork; review checklist completed.
- **Repo structure**
```text
programming-foundations/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Open a PR upstream
- Add property-based tests

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Name two strategies for debugging complex code.
1. What is code smell?
1. Why write a minimal reproducible example?


<details>
<summary>Answer key</summary>

1. Binary search logging; hypothesis-driven tests; simplifying assumptions.
1. A symptom of deeper design issues (e.g., long methods).
1. To isolate issues and make fixes clear & reviewable.


</details>

**Deliverables**
- Architecture note
- PR link/screenshot
- Coverage delta


---


### Week 4: Software Design & APIs
**Topic tag:** Programming Foundations • **Estimated hours:** 12h • **Major deliverable:** HTTP JSON API service with docs & tests

**Learning objectives**
- Design small web APIs
- Write docs that unblock users
- Automate tests in CI


**Read / watch**
- **Pro Git** — Workflows for collaboration (0.5h). [Pro Git](https://git-scm.com/book/en/v2)
- **Google Doc Style** — API reference & samples tone (0.5h). [Google Doc Style](https://developers.google.com/style/)


**Exercises & problem sets (with solutions/rubric)**
- Design a small REST API (OpenAPI spec).
- Implement endpoints; write integration tests; publish docs.


**Project milestone**
- **Spec:** `imgsvc` with `/info`, `/thumb`, `/health` endpoints.
- **Acceptance criteria & tests:** OpenAPI spec validates; tests cover success/error; README has curl examples.
- **Repo structure**
```text
programming-foundations/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Containerize with Docker
- Add rate limiting

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is idempotence?
1. What are 3 common HTTP status families?
1. Why provide curl examples?


<details>
<summary>Answer key</summary>

1. Repeated calls have same effect.
1. 2xx success, 4xx client error, 5xx server error.
1. They’re copy-pasteable and unambiguous.


</details>

**Deliverables**
- API code + tests
- OpenAPI YAML
- Deployed container (local)


---


### Week 5: Arrays, Linked Lists, Stacks, Queues
**Topic tag:** DS&A • **Estimated hours:** 12h • **Major deliverable:** DS library v1

**Learning objectives**
- Explain and analyze Lists/Stacks/Queues
- Implement core operations with tested code
- Compare tradeoffs with alternatives


**Read / watch**
- **CS61B (DS)** — Lectures on Lists/Stacks/Queues (2h). [CS61B (DS)](https://sp25.datastructur.es/)
- **MCS (MIT 6.042J)** — relevant chapters on logic/proofs/recurrences (1.5h). [MCS (MIT 6.042J)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)


**Exercises & problem sets (with solutions/rubric)**
- Implement Lists/Stacks/Queues in Python (`src/Lists/Stacks/Queues.py`); write ≥10 unit tests.
- Do 5 custom problems analyzing time/space; include tight Big-O and brief proofs.
- Solve 5 interview-style problems (document approach + complexity).


**Project milestone**
- **Spec:** Library module exposing clean API for Lists/Stacks/Queues with docstrings and examples.
- **Acceptance criteria & tests:** All tests pass; functions meet O() targets documented in README; code reviewed (self-checklist).
- **Repo structure**
```text
ds&a/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add benchmarks and plots
- Implement optional generic typing

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. State the average and worst-case time for core Lists/Stacks/Queues ops.
1. Define Θ, O, and Ω.
1. Prove that f(n)=3n^2+2n is Θ(n^2).


<details>
<summary>Answer key</summary>

1. Answers vary by DS; e.g., hash table: average O(1) lookup/insert/delete; worst-case O(n).
1. Θ: tight bound; O: upper bound; Ω: lower bound.
1. Find c1,c2,n0 such that c1 n^2 ≤ f(n) ≤ c2 n^2 for n≥n0; e.g., 3n^2 ≤ f(n) ≤ 5n^2 for n≥1.


</details>

**Deliverables**
- Lists/Stacks/Queues module + tests
- Analysis writeup (1–2 pages)
- Benchmarks CSV + brief summary


---


### Week 6: Hashing & Hash Tables
**Topic tag:** DS&A • **Estimated hours:** 12h • **Major deliverable:** Hash map with open addressing

**Learning objectives**
- Explain and analyze Hash Tables
- Implement core operations with tested code
- Compare tradeoffs with alternatives


**Read / watch**
- **CS61B (DS)** — Lectures on Hash Tables (2h). [CS61B (DS)](https://sp25.datastructur.es/)
- **MCS (MIT 6.042J)** — relevant chapters on logic/proofs/recurrences (1.5h). [MCS (MIT 6.042J)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)


**Exercises & problem sets (with solutions/rubric)**
- Implement Hash Tables in Python (`src/Hash_Tables.py`); write ≥10 unit tests.
- Do 5 custom problems analyzing time/space; include tight Big-O and brief proofs.
- Solve 5 interview-style problems (document approach + complexity).


**Project milestone**
- **Spec:** Library module exposing clean API for Hash Tables with docstrings and examples.
- **Acceptance criteria & tests:** All tests pass; functions meet O() targets documented in README; code reviewed (self-checklist).
- **Repo structure**
```text
ds&a/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add benchmarks and plots
- Implement optional generic typing

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. State the average and worst-case time for core Hash Tables ops.
1. Define Θ, O, and Ω.
1. Prove that f(n)=3n^2+2n is Θ(n^2).


<details>
<summary>Answer key</summary>

1. Answers vary by DS; e.g., hash table: average O(1) lookup/insert/delete; worst-case O(n).
1. Θ: tight bound; O: upper bound; Ω: lower bound.
1. Find c1,c2,n0 such that c1 n^2 ≤ f(n) ≤ c2 n^2 for n≥n0; e.g., 3n^2 ≤ f(n) ≤ 5n^2 for n≥1.


</details>

**Deliverables**
- Hash Tables module + tests
- Analysis writeup (1–2 pages)
- Benchmarks CSV + brief summary


---


### Week 7: Trees & Balanced Trees
**Topic tag:** DS&A • **Estimated hours:** 12h • **Major deliverable:** Balanced BST implementation

**Learning objectives**
- Explain and analyze BST/AVL/Red-Black
- Implement core operations with tested code
- Compare tradeoffs with alternatives


**Read / watch**
- **CS61B (DS)** — Lectures on BST/AVL/Red-Black (2h). [CS61B (DS)](https://sp25.datastructur.es/)
- **MCS (MIT 6.042J)** — relevant chapters on logic/proofs/recurrences (1.5h). [MCS (MIT 6.042J)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)


**Exercises & problem sets (with solutions/rubric)**
- Implement BST/AVL/Red-Black in Python (`src/BST/AVL/Red-Black.py`); write ≥10 unit tests.
- Do 5 custom problems analyzing time/space; include tight Big-O and brief proofs.
- Solve 5 interview-style problems (document approach + complexity).


**Project milestone**
- **Spec:** Library module exposing clean API for BST/AVL/Red-Black with docstrings and examples.
- **Acceptance criteria & tests:** All tests pass; functions meet O() targets documented in README; code reviewed (self-checklist).
- **Repo structure**
```text
ds&a/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add benchmarks and plots
- Implement optional generic typing

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. State the average and worst-case time for core BST/AVL/Red-Black ops.
1. Define Θ, O, and Ω.
1. Prove that f(n)=3n^2+2n is Θ(n^2).


<details>
<summary>Answer key</summary>

1. Answers vary by DS; e.g., hash table: average O(1) lookup/insert/delete; worst-case O(n).
1. Θ: tight bound; O: upper bound; Ω: lower bound.
1. Find c1,c2,n0 such that c1 n^2 ≤ f(n) ≤ c2 n^2 for n≥n0; e.g., 3n^2 ≤ f(n) ≤ 5n^2 for n≥1.


</details>

**Deliverables**
- BST/AVL/Red-Black module + tests
- Analysis writeup (1–2 pages)
- Benchmarks CSV + brief summary


---


### Week 8: Sorting & Searching
**Topic tag:** DS&A • **Estimated hours:** 12h • **Major deliverable:** Sorting library + benchmarks

**Learning objectives**
- Explain and analyze Binary Search/Merge Sort/Quick Sort
- Implement core operations with tested code
- Compare tradeoffs with alternatives


**Read / watch**
- **CS61B (DS)** — Lectures on Binary Search/Merge Sort/Quick Sort (2h). [CS61B (DS)](https://sp25.datastructur.es/)
- **MCS (MIT 6.042J)** — relevant chapters on logic/proofs/recurrences (1.5h). [MCS (MIT 6.042J)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)


**Exercises & problem sets (with solutions/rubric)**
- Implement Binary Search/Merge Sort/Quick Sort in Python (`src/Binary_Search/Merge_Sort/Quick_Sort.py`); write ≥10 unit tests.
- Do 5 custom problems analyzing time/space; include tight Big-O and brief proofs.
- Solve 5 interview-style problems (document approach + complexity).


**Project milestone**
- **Spec:** Library module exposing clean API for Binary Search/Merge Sort/Quick Sort with docstrings and examples.
- **Acceptance criteria & tests:** All tests pass; functions meet O() targets documented in README; code reviewed (self-checklist).
- **Repo structure**
```text
ds&a/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add benchmarks and plots
- Implement optional generic typing

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. State the average and worst-case time for core Binary Search/Merge Sort/Quick Sort ops.
1. Define Θ, O, and Ω.
1. Prove that f(n)=3n^2+2n is Θ(n^2).


<details>
<summary>Answer key</summary>

1. Answers vary by DS; e.g., hash table: average O(1) lookup/insert/delete; worst-case O(n).
1. Θ: tight bound; O: upper bound; Ω: lower bound.
1. Find c1,c2,n0 such that c1 n^2 ≤ f(n) ≤ c2 n^2 for n≥n0; e.g., 3n^2 ≤ f(n) ≤ 5n^2 for n≥1.


</details>

**Deliverables**
- Binary Search/Merge Sort/Quick Sort module + tests
- Analysis writeup (1–2 pages)
- Benchmarks CSV + brief summary


---


### Week 9: Boolean Logic & Gate-Level Design
**Topic tag:** Architecture • **Estimated hours:** 12h • **Major deliverable:** N2T Projects 1–2

**Learning objectives**
- Relate digital logic to CPU organization
- Build working components in HDL and verify via test scripts
- Explain datapath/control tradeoffs at a high level


**Read / watch**
- **Nand2Tetris** — Ch. 1–2 (3h). [Nand2Tetris](https://www.nand2tetris.org/)
- **Patterson & Hennessy (COD)** — corresponding COD chapters/sections (2h). [Patterson & Hennessy (COD)](https://books.google.com/books/about/Computer_Organization_and_Design.html?id=1lD9LZRcIZ8C)


**Exercises & problem sets (with solutions/rubric)**
- Complete Nand2Tetris project(s) for this week; commit hardware HDL files and test outputs.
- Answer 5 written questions tying COD concepts to your N2T implementation.


**Project milestone**
- **Spec:** Working HDL components + short explainer with diagrams (ASCII or embedded images).
- **Acceptance criteria & tests:** All N2T provided tests pass; explanations link behavior to COD readings.
- **Repo structure**
```text
architecture/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Implement optional ALU flags or optimizations
- Write a tiny assembly demo

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What does two’s complement represent and why is it useful?
1. Define instruction set architecture (ISA).
1. What’s the role of a clock in synchronous designs?


<details>
<summary>Answer key</summary>

1. It encodes signed integers; simplifies addition/subtraction circuits.
1. The interface between software and hardware: machine instructions, registers, etc.
1. It coordinates state updates across flip-flops so circuits change in lockstep.


</details>

**Deliverables**
- HDL projects + passing tests
- Explainer (1–2 pages)


---


### Week 10: Arithmetic & the ALU
**Topic tag:** Architecture • **Estimated hours:** 12h • **Major deliverable:** N2T Project 2/ALU

**Learning objectives**
- Relate digital logic to CPU organization
- Build working components in HDL and verify via test scripts
- Explain datapath/control tradeoffs at a high level


**Read / watch**
- **Nand2Tetris** — Ch. 2–3 (3h). [Nand2Tetris](https://www.nand2tetris.org/)
- **Patterson & Hennessy (COD)** — corresponding COD chapters/sections (2h). [Patterson & Hennessy (COD)](https://books.google.com/books/about/Computer_Organization_and_Design.html?id=1lD9LZRcIZ8C)


**Exercises & problem sets (with solutions/rubric)**
- Complete Nand2Tetris project(s) for this week; commit hardware HDL files and test outputs.
- Answer 5 written questions tying COD concepts to your N2T implementation.


**Project milestone**
- **Spec:** Working HDL components + short explainer with diagrams (ASCII or embedded images).
- **Acceptance criteria & tests:** All N2T provided tests pass; explanations link behavior to COD readings.
- **Repo structure**
```text
architecture/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Implement optional ALU flags or optimizations
- Write a tiny assembly demo

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What does two’s complement represent and why is it useful?
1. Define instruction set architecture (ISA).
1. What’s the role of a clock in synchronous designs?


<details>
<summary>Answer key</summary>

1. It encodes signed integers; simplifies addition/subtraction circuits.
1. The interface between software and hardware: machine instructions, registers, etc.
1. It coordinates state updates across flip-flops so circuits change in lockstep.


</details>

**Deliverables**
- HDL projects + passing tests
- Explainer (1–2 pages)


---


### Week 11: Machine Language & CPU
**Topic tag:** Architecture • **Estimated hours:** 12h • **Major deliverable:** N2T Projects 5–6

**Learning objectives**
- Relate digital logic to CPU organization
- Build working components in HDL and verify via test scripts
- Explain datapath/control tradeoffs at a high level


**Read / watch**
- **Nand2Tetris** — Ch. 4–5 (3h). [Nand2Tetris](https://www.nand2tetris.org/)
- **Patterson & Hennessy (COD)** — corresponding COD chapters/sections (2h). [Patterson & Hennessy (COD)](https://books.google.com/books/about/Computer_Organization_and_Design.html?id=1lD9LZRcIZ8C)


**Exercises & problem sets (with solutions/rubric)**
- Complete Nand2Tetris project(s) for this week; commit hardware HDL files and test outputs.
- Answer 5 written questions tying COD concepts to your N2T implementation.


**Project milestone**
- **Spec:** Working HDL components + short explainer with diagrams (ASCII or embedded images).
- **Acceptance criteria & tests:** All N2T provided tests pass; explanations link behavior to COD readings.
- **Repo structure**
```text
architecture/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Implement optional ALU flags or optimizations
- Write a tiny assembly demo

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What does two’s complement represent and why is it useful?
1. Define instruction set architecture (ISA).
1. What’s the role of a clock in synchronous designs?


<details>
<summary>Answer key</summary>

1. It encodes signed integers; simplifies addition/subtraction circuits.
1. The interface between software and hardware: machine instructions, registers, etc.
1. It coordinates state updates across flip-flops so circuits change in lockstep.


</details>

**Deliverables**
- HDL projects + passing tests
- Explainer (1–2 pages)


---


### Week 12: Memory & Computer Architecture
**Topic tag:** Architecture • **Estimated hours:** 12h • **Major deliverable:** N2T Projects 3–5

**Learning objectives**
- Relate digital logic to CPU organization
- Build working components in HDL and verify via test scripts
- Explain datapath/control tradeoffs at a high level


**Read / watch**
- **Nand2Tetris** — Ch. 3–5 (3h). [Nand2Tetris](https://www.nand2tetris.org/)
- **Patterson & Hennessy (COD)** — corresponding COD chapters/sections (2h). [Patterson & Hennessy (COD)](https://books.google.com/books/about/Computer_Organization_and_Design.html?id=1lD9LZRcIZ8C)


**Exercises & problem sets (with solutions/rubric)**
- Complete Nand2Tetris project(s) for this week; commit hardware HDL files and test outputs.
- Answer 5 written questions tying COD concepts to your N2T implementation.


**Project milestone**
- **Spec:** Working HDL components + short explainer with diagrams (ASCII or embedded images).
- **Acceptance criteria & tests:** All N2T provided tests pass; explanations link behavior to COD readings.
- **Repo structure**
```text
architecture/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Implement optional ALU flags or optimizations
- Write a tiny assembly demo

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What does two’s complement represent and why is it useful?
1. Define instruction set architecture (ISA).
1. What’s the role of a clock in synchronous designs?


<details>
<summary>Answer key</summary>

1. It encodes signed integers; simplifies addition/subtraction circuits.
1. The interface between software and hardware: machine instructions, registers, etc.
1. It coordinates state updates across flip-flops so circuits change in lockstep.


</details>

**Deliverables**
- HDL projects + passing tests
- Explainer (1–2 pages)


---


### Week 13: Checkpoint #1: Review & Refactor
**Topic tag:** Meta • **Estimated hours:** 8h • **Major deliverable:** Refactor DS/Arch code + mock exam

**Learning objectives**
- Consolidate knowledge
- Practice exam-style questions
- Improve code quality via refactor


**Read / watch**
- **Pro Git** — Rewriting history safely (interactive rebase) (0.5h). [Pro Git](https://git-scm.com/book/en/v2)


**Exercises & problem sets (with solutions/rubric)**
- Write a 2-hour mock exam covering Weeks 1–12 (included) and take it.
- Refactor 1–2 modules for readability/performance; document changes.


**Project milestone**
- **Spec:** Refactor PRs with before/after benchmarks and notes.
- **Acceptance criteria & tests:** No functionality regressions; tests pass; improved metrics documented.
- **Repo structure**
```text
meta/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Automate benchmarks in CI
- Add perf regression guard

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What did you find hardest so far and why?
1. Which refactor yielded the largest benefit?
1. What will you change next quarter?


<details>
<summary>Answer key</summary>

1. Free-form reflection.
1. Measure and report.
1. Set 1–2 concrete study adjustments.


</details>

**Deliverables**
- Mock exam + answers
- Refactor PRs
- Retrospective writeup


---


### Week 14: Processes & System Calls
**Topic tag:** Operating Systems • **Estimated hours:** 12h • **Major deliverable:** Mini `fork/exec/wait` demos

**Learning objectives**
- Explain processes & system calls at the conceptual + API level
- Write/modify code that demonstrates the concept
- Assess pitfalls (race conditions, deadlocks, etc.)


**Read / watch**
- **OSTEP** — Ch. Processes/Virtualization (3h). [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- **Tanenbaum OS (OSDI)** — parallel chapters for context (2h). [Tanenbaum OS (OSDI)](https://archive.org/details/operating-systems-design-and-implementation-tanenbaum-2006)


**Exercises & problem sets (with solutions/rubric)**
- Run/modify a small C program illustrating this week’s concept (provided skeleton).
- Complete 2–3 OSTEP homework questions; include answers.


**Project milestone**
- **Spec:** Mini-lab demonstrating processes & system calls with a Makefile and README.
- **Acceptance criteria & tests:** Reproducible on macOS (or Linux container); tests exercise edge cases.
- **Repo structure**
```text
operating-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Port to Linux container and compare behavior
- Add extra experiments and measurements

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define a process vs. thread.
1. What’s a race condition?
1. Explain the role of a scheduler.


<details>
<summary>Answer key</summary>

1. Process: isolated address space; thread: lighter-weight execution unit within a process.
1. A bug due to unsynchronized access to shared state causing nondeterministic outcomes.
1. Decides which runnable entity gets CPU time to meet goals (throughput/latency/fairness).


</details>

**Deliverables**
- Processes & System Calls mini-lab
- Answers to OSTEP questions
- Short reflection


---


### Week 15: Threads & Concurrency
**Topic tag:** Operating Systems • **Estimated hours:** 12h • **Major deliverable:** Threaded workload + race demo

**Learning objectives**
- Explain threads & concurrency at the conceptual + API level
- Write/modify code that demonstrates the concept
- Assess pitfalls (race conditions, deadlocks, etc.)


**Read / watch**
- **OSTEP** — Ch. Concurrency/Locks (3h). [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- **Tanenbaum OS (OSDI)** — parallel chapters for context (2h). [Tanenbaum OS (OSDI)](https://archive.org/details/operating-systems-design-and-implementation-tanenbaum-2006)


**Exercises & problem sets (with solutions/rubric)**
- Run/modify a small C program illustrating this week’s concept (provided skeleton).
- Complete 2–3 OSTEP homework questions; include answers.


**Project milestone**
- **Spec:** Mini-lab demonstrating threads & concurrency with a Makefile and README.
- **Acceptance criteria & tests:** Reproducible on macOS (or Linux container); tests exercise edge cases.
- **Repo structure**
```text
operating-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Port to Linux container and compare behavior
- Add extra experiments and measurements

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define a process vs. thread.
1. What’s a race condition?
1. Explain the role of a scheduler.


<details>
<summary>Answer key</summary>

1. Process: isolated address space; thread: lighter-weight execution unit within a process.
1. A bug due to unsynchronized access to shared state causing nondeterministic outcomes.
1. Decides which runnable entity gets CPU time to meet goals (throughput/latency/fairness).


</details>

**Deliverables**
- Threads & Concurrency mini-lab
- Answers to OSTEP questions
- Short reflection


---


### Week 16: Scheduling & Deadlocks
**Topic tag:** Operating Systems • **Estimated hours:** 12h • **Major deliverable:** Scheduler experiments

**Learning objectives**
- Explain scheduling & deadlocks at the conceptual + API level
- Write/modify code that demonstrates the concept
- Assess pitfalls (race conditions, deadlocks, etc.)


**Read / watch**
- **OSTEP** — Ch. Scheduling/Deadlock (3h). [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- **Tanenbaum OS (OSDI)** — parallel chapters for context (2h). [Tanenbaum OS (OSDI)](https://archive.org/details/operating-systems-design-and-implementation-tanenbaum-2006)


**Exercises & problem sets (with solutions/rubric)**
- Run/modify a small C program illustrating this week’s concept (provided skeleton).
- Complete 2–3 OSTEP homework questions; include answers.


**Project milestone**
- **Spec:** Mini-lab demonstrating scheduling & deadlocks with a Makefile and README.
- **Acceptance criteria & tests:** Reproducible on macOS (or Linux container); tests exercise edge cases.
- **Repo structure**
```text
operating-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Port to Linux container and compare behavior
- Add extra experiments and measurements

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define a process vs. thread.
1. What’s a race condition?
1. Explain the role of a scheduler.


<details>
<summary>Answer key</summary>

1. Process: isolated address space; thread: lighter-weight execution unit within a process.
1. A bug due to unsynchronized access to shared state causing nondeterministic outcomes.
1. Decides which runnable entity gets CPU time to meet goals (throughput/latency/fairness).


</details>

**Deliverables**
- Scheduling & Deadlocks mini-lab
- Answers to OSTEP questions
- Short reflection


---


### Week 17: Memory Management
**Topic tag:** Operating Systems • **Estimated hours:** 12h • **Major deliverable:** Paging/allocator lab

**Learning objectives**
- Explain memory management at the conceptual + API level
- Write/modify code that demonstrates the concept
- Assess pitfalls (race conditions, deadlocks, etc.)


**Read / watch**
- **OSTEP** — Ch. Address Spaces/VM (3h). [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- **Tanenbaum OS (OSDI)** — parallel chapters for context (2h). [Tanenbaum OS (OSDI)](https://archive.org/details/operating-systems-design-and-implementation-tanenbaum-2006)


**Exercises & problem sets (with solutions/rubric)**
- Run/modify a small C program illustrating this week’s concept (provided skeleton).
- Complete 2–3 OSTEP homework questions; include answers.


**Project milestone**
- **Spec:** Mini-lab demonstrating memory management with a Makefile and README.
- **Acceptance criteria & tests:** Reproducible on macOS (or Linux container); tests exercise edge cases.
- **Repo structure**
```text
operating-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Port to Linux container and compare behavior
- Add extra experiments and measurements

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define a process vs. thread.
1. What’s a race condition?
1. Explain the role of a scheduler.


<details>
<summary>Answer key</summary>

1. Process: isolated address space; thread: lighter-weight execution unit within a process.
1. A bug due to unsynchronized access to shared state causing nondeterministic outcomes.
1. Decides which runnable entity gets CPU time to meet goals (throughput/latency/fairness).


</details>

**Deliverables**
- Memory Management mini-lab
- Answers to OSTEP questions
- Short reflection


---


### Week 18: Sockets & TCP
**Topic tag:** Networking • **Estimated hours:** 12h • **Major deliverable:** Concurrent echo server + client

**Learning objectives**
- Use sockets API (connect/bind/listen/accept)
- Explain TCP vs UDP tradeoffs
- Trace a TCP handshake in Wireshark


**Read / watch**
- **Beej Sockets** — Ch. on TCP sockets (2h). [Beej Sockets](https://beej.us/guide/bgnet/)
- **Stanford CS144** — Transport + TCP lectures/notes (2h). [Stanford CS144](https://cs144.github.io/)


**Exercises & problem sets (with solutions/rubric)**
- Packet-handling warmup: parse IPv4/TCP headers from hex dump; verify fields.
- Socket lab: build a blocking echo server & client; then add timeouts.


**Project milestone**
- **Spec:** CLI client/server with arguments (host, port); handles SIGINT and timeouts.
- **Acceptance criteria & tests:** Passes provided integration tests; handles concurrent clients (select/threads).
- **Repo structure**
```text
networking/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - TLS via `ssl` in Python
- HTTP/1.1 persistent connections

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Which flags appear in the TCP handshake?
1. What is MTU?
1. Define idempotent HTTP method and give an example.


<details>
<summary>Answer key</summary>

1. SYN, SYN-ACK, ACK.
1. Max Transmission Unit: largest payload per L2 frame.
1. A request with no side effects when repeated, e.g., GET.


</details>

**Deliverables**
- Client/server code + tests
- pcap + analysis notes


---


### Week 19: HTTP/HTTPS & APIs
**Topic tag:** Networking • **Estimated hours:** 12h • **Major deliverable:** HTTP client with retries + TLS

**Learning objectives**
- Use sockets API (connect/bind/listen/accept)
- Explain TCP vs UDP tradeoffs
- Trace a TCP handshake in Wireshark


**Read / watch**
- **Beej Sockets** — Ch. on TCP sockets (2h). [Beej Sockets](https://beej.us/guide/bgnet/)
- **Stanford CS144** — Transport + TCP lectures/notes (2h). [Stanford CS144](https://cs144.github.io/)


**Exercises & problem sets (with solutions/rubric)**
- Packet-handling warmup: parse IPv4/TCP headers from hex dump; verify fields.
- Socket lab: build a blocking echo server & client; then add timeouts.


**Project milestone**
- **Spec:** CLI client/server with arguments (host, port); handles SIGINT and timeouts.
- **Acceptance criteria & tests:** Passes provided integration tests; handles concurrent clients (select/threads).
- **Repo structure**
```text
networking/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - TLS via `ssl` in Python
- HTTP/1.1 persistent connections

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Which flags appear in the TCP handshake?
1. What is MTU?
1. Define idempotent HTTP method and give an example.


<details>
<summary>Answer key</summary>

1. SYN, SYN-ACK, ACK.
1. Max Transmission Unit: largest payload per L2 frame.
1. A request with no side effects when repeated, e.g., GET.


</details>

**Deliverables**
- Client/server code + tests
- pcap + analysis notes


---


### Week 20: Relational Modeling & SQL
**Topic tag:** Databases • **Estimated hours:** 12h • **Major deliverable:** Schema + queries + constraints

**Learning objectives**
- Normalize to 3NF
- Write non-trivial SQL queries
- Explain how indexes change query plans


**Read / watch**
- **CMU 15-445 (DB)** — Intro + Storage + Indexes lectures (3h). [CMU 15-445 (DB)](https://15445.courses.cs.cmu.edu/fall2025/syllabus.html)
- **PostgreSQL** — Tutorial: psql, schemas, indexes (1.5h). [PostgreSQL](https://www.postgresql.org/docs/)


**Exercises & problem sets (with solutions/rubric)**
- Design a schema for a simple app; write 10 queries including 2 JOINs and 2 aggregations.
- Create indexes; measure query plans with `EXPLAIN ANALYZE`.


**Project milestone**
- **Spec:** SQL scripts and a short report with screenshots of plans.
- **Acceptance criteria & tests:** All scripts run idempotently; report interprets plan nodes correctly.
- **Repo structure**
```text
databases/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add a trigger and a transaction demo
- Implement a simple ORM layer

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is a B+ tree?
1. Define ACID.
1. When is a hash index preferable to a btree?


<details>
<summary>Answer key</summary>

1. A balanced tree index with all records in leaves and linked leaf nodes.
1. Atomicity, Consistency, Isolation, Durability.
1. For equality lookups with low range queries and good hash distribution.


</details>

**Deliverables**
- DDL/DML scripts
- Plan analysis report


---


### Week 21: Transactions, Indexing & Query Plans
**Topic tag:** Databases • **Estimated hours:** 12h • **Major deliverable:** TX demo + index experiments

**Learning objectives**
- Normalize to 3NF
- Write non-trivial SQL queries
- Explain how indexes change query plans


**Read / watch**
- **CMU 15-445 (DB)** — Intro + Storage + Indexes lectures (3h). [CMU 15-445 (DB)](https://15445.courses.cs.cmu.edu/fall2025/syllabus.html)
- **PostgreSQL** — Tutorial: psql, schemas, indexes (1.5h). [PostgreSQL](https://www.postgresql.org/docs/)


**Exercises & problem sets (with solutions/rubric)**
- Design a schema for a simple app; write 10 queries including 2 JOINs and 2 aggregations.
- Create indexes; measure query plans with `EXPLAIN ANALYZE`.


**Project milestone**
- **Spec:** SQL scripts and a short report with screenshots of plans.
- **Acceptance criteria & tests:** All scripts run idempotently; report interprets plan nodes correctly.
- **Repo structure**
```text
databases/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add a trigger and a transaction demo
- Implement a simple ORM layer

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is a B+ tree?
1. Define ACID.
1. When is a hash index preferable to a btree?


<details>
<summary>Answer key</summary>

1. A balanced tree index with all records in leaves and linked leaf nodes.
1. Atomicity, Consistency, Isolation, Durability.
1. For equality lookups with low range queries and good hash distribution.


</details>

**Deliverables**
- DDL/DML scripts
- Plan analysis report


---


### Week 22: Design, Docs, and Reviews
**Topic tag:** Software Engineering • **Estimated hours:** 10h • **Major deliverable:** Docs + review system

**Learning objectives**
- Apply code review best practices
- Set up CI (lint+test)
- Write clear developer docs


**Read / watch**
- **Google Eng Practices (Code Review)** — How to do a code review + standards (1.5h). [Google Eng Practices (Code Review)](https://google.github.io/eng-practices/review/)
- **Pro Git** — Branching workflows, PRs (1h). [Pro Git](https://git-scm.com/book/en/v2)
- **Google Doc Style** — Voice & tone, inclusive language (0.5h). [Google Doc Style](https://developers.google.com/style/)


**Exercises & problem sets (with solutions/rubric)**
- Perform a structured self-review using the Google checklist; open issues in your repo.
- Write/extend project docs using the style guide; run a linter for Markdown links.


**Project milestone**
- **Spec:** Create a CONTRIBUTING.md, CODE_OF_CONDUCT.md, and a CI workflow.
- **Acceptance criteria & tests:** CI status badge green; docs pass link-check; PR template in place.
- **Repo structure**
```text
software-engineering/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add pre-commit hooks
- Adopt semantic versioning + CHANGELOG

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What should a reviewer prioritize first?
1. Name 2 traits of good documentation.
1. Why run tests in CI for PRs?


<details>
<summary>Answer key</summary>

1. Correctness and design fundamentals.
1. Audience-appropriate, task-oriented; concise and consistent.
1. Prevents regressions and ensures changes integrate safely.


</details>

**Deliverables**
- Docs PR merged
- CI workflow yaml
- Review notes


---


### Week 23: CI/CD & Project Health
**Topic tag:** Software Engineering • **Estimated hours:** 11h • **Major deliverable:** CI pipeline + release v0.1.0

**Learning objectives**
- Automate build/test
- Version and release software
- Publish artifacts


**Read / watch**
- **GitHub Actions** — Workflows quickstart (1h). [GitHub Actions](https://docs.github.com/actions)
- **Docker** — Get started (containers 101) (1h). [Docker](https://docs.docker.com/get-started/)


**Exercises & problem sets (with solutions/rubric)**
- Add CI jobs: lint, test, build container.
- Publish a release v0.1.0 with changelog and version tags.


**Project milestone**
- **Spec:** CI pipeline (`.github/workflows/ci.yml`) + containerized service.
- **Acceptance criteria & tests:** Green pipeline on PRs; image builds locally; tagged release produced.
- **Repo structure**
```text
software-engineering/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add CodeQL or SAST
- Add release notes automation

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is a matrix build?
1. Why pin base images?
1. What should trigger a release?


<details>
<summary>Answer key</summary>

1. Run jobs across versions/platforms.
1. Security & reproducibility.
1. Feature completion, fixes; semantic versioning rules.


</details>

**Deliverables**
- CI yaml
- Containerfile
- Release link/screenshot


---


### Week 24: Automata & Regular Languages
**Topic tag:** Theory • **Estimated hours:** 11h • **Major deliverable:** Regex engine (subset) + proofs

**Learning objectives**
- Explain DFAs/NFAs/regex equivalence
- Construct proofs by induction
- Implement a tiny regex engine


**Read / watch**
- **MCS (MIT 6.042J)** — Chapters on induction + regular languages (selected) (2h). [MCS (MIT 6.042J)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)


**Exercises & problem sets (with solutions/rubric)**
- Prove closure properties for regular languages (union, concat, star).
- Convert 2 regexes to NFAs by construction.


**Project milestone**
- **Spec:** Implement Thompson NFA construction + simulation for literals, ., |, *, +, ?.
- **Acceptance criteria & tests:** Passes provided regex tests; includes complexity analysis.
- **Repo structure**
```text
theory/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add character classes and anchors
- Visualize NFAs

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is the pumping lemma for regular languages?
1. Are regular languages closed under reversal?
1. Give a non-regular language example.


<details>
<summary>Answer key</summary>

1. A tool to show a language isn’t regular via pumping property.
1. Yes; reverse each DFA transition accordingly.
1. {a^n b^n | n≥0}


</details>

**Deliverables**
- Regex engine + tests
- Proof writeups


---


### Week 25: Computability & Complexity
**Topic tag:** Theory • **Estimated hours:** 8.5h • **Major deliverable:** Reductions writeup + P vs NP survey

**Learning objectives**
- Distinguish decidable/semidecidable
- Use reductions to compare problems
- Explain P, NP, NP-complete


**Read / watch**
- **MCS (MIT 6.042J)** — Chapters on computability + complexity (selected) (2h). [MCS (MIT 6.042J)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)


**Exercises & problem sets (with solutions/rubric)**
- Show HALT is undecidable (outline proof).
- Reduce 3-SAT to CLIQUE at high level.


**Project milestone**
- **Spec:** Short essays with diagrams of reductions; cite sources.
- **Acceptance criteria & tests:** Correct definitions; coherent reduction steps; clear writing.
- **Repo structure**
```text
theory/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Explore PCP theorem summary
- Implement SAT solver toy

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define decidable.
1. What’s NP-complete?
1. State Church–Turing thesis.


<details>
<summary>Answer key</summary>

1. There exists a TM that halts and accepts/rejects for all inputs.
1. In NP and NP-hard; every NP problem reduces to it in poly time.
1. Effectively computable equals computable by Turing machine.


</details>

**Deliverables**
- 2–3 page writeup
- Self-check rubric


---


### Week 26: Checkpoint #2: Review & Mock
**Topic tag:** Meta • **Estimated hours:** 6h • **Major deliverable:** Mock exam + portfolio audit

**Learning objectives**
- Assess gaps
- Plan remediation
- Polish artifacts


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- 2-hour mock exam (Weeks 14–25) included.
- Audit repo health (issues, docs, tests, CI); open and close issues.


**Project milestone**
- **Spec:** Exam with answer key; repo health report.
- **Acceptance criteria & tests:** Action items tracked and assigned to weeks.
- **Repo structure**
```text
meta/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Automate contributors docs site
- Add project badges

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Which 2 topics need the most review?
1. What concrete actions will you take?
1. What metrics will show improvement?


<details>
<summary>Answer key</summary>

1. Self-assessment.
1. List actions with dates.
1. Coverage %, performance, correctness, doc quality.


</details>

**Deliverables**
- Mock exam + answers
- Audit report


---


### Week 27: Applied Cryptography
**Topic tag:** Security • **Estimated hours:** 10.5h • **Major deliverable:** Cryptopals Set 1 solutions + writeups

**Learning objectives**
- Implement basic crypto primitives
- Recognize common pitfalls (ECB, padding)
- Write clear, reproducible crypto code


**Read / watch**
- **Security Engineering** — Chapters on crypto engineering (selected) (2h). [Security Engineering](https://www.cl.cam.ac.uk/archive/rja14/book.html)
- **Cryptopals** — Set 1 overview (1h). [Cryptopals](https://www.cryptopals.com/)


**Exercises & problem sets (with solutions/rubric)**
- Complete Cryptopals Set 1 (implement AES ECB/CBC, PKCS#7, etc.).
- Write a security note on pitfalls you encountered.


**Project milestone**
- **Spec:** Solutions in Python with tests; do not use high-level crypto libs beyond primitives.
- **Acceptance criteria & tests:** Tests pass against known vectors; writeups explain attacks.
- **Repo structure**
```text
security/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Attempt Set 2 challenges
- Benchmark implementations

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Why is ECB insecure?
1. What is an IV and why must it be random?
1. Define CPA security at a high level.


<details>
<summary>Answer key</summary>

1. Patterns leak because identical blocks map to identical ciphertext blocks.
1. Prevents pattern leakage and ensures freshness; must be unpredictable.
1. Adversary cannot distinguish encryptions under chosen-plaintext queries.


</details>

**Deliverables**
- Code + tests
- Writeups (md)


---


### Week 28: Software & Web Security
**Topic tag:** Security • **Estimated hours:** 11h • **Major deliverable:** Threat model & secure code audit

**Learning objectives**
- Apply threat modeling
- Harden a web service
- Add security testing


**Read / watch**
- **Berkeley CS161** — Software security + web security modules (2h). [Berkeley CS161](https://fa25.cs161.org/)


**Exercises & problem sets (with solutions/rubric)**
- Audit your API from Week 4: input validation, auth, logging.
- Add rate limiting and structured logging; test for common vulns.


**Project milestone**
- **Spec:** STRIDE threat model + mitigations; security tests (fuzz/basic).
- **Acceptance criteria & tests:** No critical issues in basic scans; mitigations documented.
- **Repo structure**
```text
security/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add OAuth 2.0
- Implement CSP and security headers

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is XSS?
1. Name two logging best practices.
1. What’s the principle of least privilege?


<details>
<summary>Answer key</summary>

1. Injecting scripts into trusted contexts.
1. Avoid secrets in logs; structured logs with levels.
1. Grant minimal rights needed for tasks.


</details>

**Deliverables**
- Threat model doc
- Security PRs & tests


---


### Week 29: HCI/UX Foundations
**Topic tag:** HCI • **Estimated hours:** 9.5h • **Major deliverable:** Prototype + usability test report

**Learning objectives**
- Apply human-centered design
- Prototype and evaluate
- Translate findings into changes


**Read / watch**
- **Design of Everyday Things** — Ch. on affordances/signifiers; read summaries if book not owned (2h). [Design of Everyday Things](https://mitpress.mit.edu/9780262525671/the-design-of-everyday-things/)


**Exercises & problem sets (with solutions/rubric)**
- Create low-fi wireframes for an app idea (paper or tool).
- Conduct 3 think-aloud tests; summarize findings.


**Project milestone**
- **Spec:** Clickable prototype of a task flow (e.g., 'upload and tag images').
- **Acceptance criteria & tests:** 3 usability sessions; prioritized fix list.
- **Repo structure**
```text
hci/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Run a SUS survey
- Create a style guide page

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define affordance vs. signifier.
1. What is usability?
1. Why test with 3–5 users?


<details>
<summary>Answer key</summary>

1. Affordance: possible actions; signifier: cues indicating them.
1. Effectiveness, efficiency, satisfaction in a context.
1. Early tests catch most major issues with minimal cost.


</details>

**Deliverables**
- Prototype link/images
- Usability report (2–3 pages)


---


### Week 30: Elective A (Compilers) — Scanning & Parsing
**Topic tag:** Compilers • **Estimated hours:** 11h • **Major deliverable:** Tokeniser + recursive-descent parser

**Learning objectives**
- Implement scanner & parser
- Produce ASTs with tests
- Handle errors gracefully


**Read / watch**
- **Crafting Interpreters** — Ch. 1–7 (scanning/parsing) (3h). [Crafting Interpreters](https://craftinginterpreters.com/)


**Exercises & problem sets (with solutions/rubric)**
- Implement a scanner for numbers/strings/identifiers/operators.
- Implement recursive-descent parser for expressions/statements.


**Project milestone**
- **Spec:** Subset of Lox grammar; unit tests for tokenization & parsing.
- **Acceptance criteria & tests:** Parses valid programs; reports errors with line/col; tests pass.
- **Repo structure**
```text
compilers/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add Pratt parser
- Error recovery strategies

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What’s the purpose of an AST?
1. Explain token vs lexeme.
1. Left vs right associativity?


<details>
<summary>Answer key</summary>

1. Structured representation for later stages.
1. Token is category/metadata; lexeme is raw text.
1. Defines grouping of repeated operators.


</details>

**Deliverables**
- Scanner+parser code
- AST examples


---


### Week 31: Elective A — Static Analysis & Interpretation
**Topic tag:** Compilers • **Estimated hours:** 12h • **Major deliverable:** Resolver + tree-walk interpreter

**Learning objectives**
- Implement name resolution
- Execute ASTs
- Handle runtime errors


**Read / watch**
- **Crafting Interpreters** — Ch. 8–13 (resolving, interpreting) (3h). [Crafting Interpreters](https://craftinginterpreters.com/)


**Exercises & problem sets (with solutions/rubric)**
- Implement lexical scope resolver; interpreter for expressions/statements.
- Add errors for undefined variables and arity mismatches.


**Project milestone**
- **Spec:** Interpreter for arithmetic, variables, functions.
- **Acceptance criteria & tests:** All provided sample programs produce expected output; resolver catches errors.
- **Repo structure**
```text
compilers/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add closures
- Tail-call optimization

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is lexical scope?
1. Difference between compile-time and run-time errors?
1. Why have a resolver?


<details>
<summary>Answer key</summary>

1. Scope determined by source structure.
1. Compile-time detected before execution; run-time during execution.
1. To bind identifiers to declarations and catch scope issues.


</details>

**Deliverables**
- Interpreter code + tests
- Resolver tests


---


### Week 32: Elective A — Bytecode VM
**Topic tag:** Compilers • **Estimated hours:** 12h • **Major deliverable:** Bytecode compiler + VM

**Learning objectives**
- Lower AST to bytecode
- Execute in a VM
- Manage memory basics


**Read / watch**
- **Crafting Interpreters** — Part II (VM) selected chapters) (3h). [Crafting Interpreters](https://craftinginterpreters.com/)


**Exercises & problem sets (with solutions/rubric)**
- Compile AST to bytecode; implement VM with stack, call frames, GC stub.


**Project milestone**
- **Spec:** Simple VM with arithmetic, branches, functions; mark-and-sweep stub.
- **Acceptance criteria & tests:** Test suite passes; performance report vs tree-walk.
- **Repo structure**
```text
compilers/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Implement GC fully
- Add objects/strings library

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Why bytecode?
1. Stack vs register VM?
1. What triggers GC?


<details>
<summary>Answer key</summary>

1. Portability and simpler implementation than native code.
1. Stack VMs use operand stacks; register VMs use registers for operands.
1. Heap pressure thresholds or allocation limits.


</details>

**Deliverables**
- Compiler + VM code
- Perf report


---


### Week 33: Elective A — Optimisation & Tooling
**Topic tag:** Compilers • **Estimated hours:** 10.5h • **Major deliverable:** Constant folding + simple peephole

**Learning objectives**
- Implement simple optimisations
- Measure performance impact
- Improve developer tooling


**Read / watch**
- **Crafting Interpreters** — Optimisation & tooling chapters (selected) (2h). [Crafting Interpreters](https://craftinginterpreters.com/)


**Exercises & problem sets (with solutions/rubric)**
- Implement constant folding and simple peephole passes; measure speedup.


**Project milestone**
- **Spec:** Add debug disassembler and IR printer.
- **Acceptance criteria & tests:** Demonstrable speedups on benchmark programs; docs updated.
- **Repo structure**
```text
compilers/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Implement local common-subexpression elimination
- Add simple profiler

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is SSA (conceptually)?
1. Define basic block.
1. Why measure before optimising?


<details>
<summary>Answer key</summary>

1. Single Static Assignment form, not implemented here but conceptually a unique assignment per variable.
1. Straight-line code with single entry and exit.
1. To ensure improvements are real and targeted.


</details>

**Deliverables**
- Optimised VM
- Benchmark results
- Docs


---


### Week 34: Elective B (Distributed) — RPC & MapReduce
**Topic tag:** Distributed Systems • **Estimated hours:** 12h • **Major deliverable:** MapReduce lab + RPC framework (toy)

**Learning objectives**
- Explain RPC and serialization
- Build a fault-tolerant MapReduce (basic)
- Handle worker failures (retry)


**Read / watch**
- **MIT 6.5840 (Distributed Systems)** — Intro + MapReduce lab (3h). [MIT 6.5840 (Distributed Systems)](https://pdos.csail.mit.edu/6.824/)


**Exercises & problem sets (with solutions/rubric)**
- Implement a toy RPC over TCP; handle request/response framing.
- Implement a mini MapReduce for word count across files.


**Project milestone**
- **Spec:** Coordinator + worker processes; simple master/worker protocol.
- **Acceptance criteria & tests:** Passes randomized tests; tolerates worker crash by reassigning tasks.
- **Repo structure**
```text
distributed-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add gRPC version
- Add exactly-once semantics discussion

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define idempotency in distributed ops.
1. Why is failure the norm?
1. What is a heartbeating mechanism?


<details>
<summary>Answer key</summary>

1. Repeating a request yields the same result.
1. Many components over networks fail independently.
1. Periodic liveness check to detect failures.


</details>

**Deliverables**
- Coordinator/worker code + tests
- Failure demo video


---


### Week 35: Elective B — Replication & Consistency
**Topic tag:** Distributed Systems • **Estimated hours:** 12h • **Major deliverable:** Key-value store with primary-backup

**Learning objectives**
- Explain linearizability vs eventual consistency
- Implement replication & failover
- Reason about correctness


**Read / watch**
- **MIT 6.5840 (Distributed Systems)** — Consistency & replication (3h). [MIT 6.5840 (Distributed Systems)](https://pdos.csail.mit.edu/6.824/)


**Exercises & problem sets (with solutions/rubric)**
- Implement primary-backup replication with write-ahead log; test failover.


**Project milestone**
- **Spec:** KV with PUT/GET; durability via log; leader election (simplified).
- **Acceptance criteria & tests:** Consistency tests pass; isolated node rejoins cluster safely.
- **Repo structure**
```text
distributed-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add Raft-style log replication
- Add snapshotting

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is linearizability?
1. Difference: availability vs durability?
1. Why use logs?


<details>
<summary>Answer key</summary>

1. Operations appear to occur atomically at a single time point between call and response.
1. Availability: service responds; durability: data persists across failures.
1. To provide an append-only history for recovery/replication.


</details>

**Deliverables**
- KV store + tests
- Consistency analysis


---


### Week 36: Elective B — Faults & Recovery
**Topic tag:** Distributed Systems • **Estimated hours:** 10.5h • **Major deliverable:** Failure injection and recovery testing

**Learning objectives**
- Design failure tests
- Implement recovery paths
- Measure system behavior under faults


**Read / watch**
- **MIT 6.5840 (Distributed Systems)** — Fault tolerance, failures (2.5h). [MIT 6.5840 (Distributed Systems)](https://pdos.csail.mit.edu/6.824/)


**Exercises & problem sets (with solutions/rubric)**
- Write chaos tests (kill -9, network delays) against your KV store; measure MTTR.


**Project milestone**
- **Spec:** Automated chaos test suite + recovery improvements.
- **Acceptance criteria & tests:** All chaos tests end in recovery; metrics recorded & graphed.
- **Repo structure**
```text
distributed-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add dashboards
- Automate repeated chaos experiments

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is split-brain?
1. How does quorum help?
1. Define MTTR.


<details>
<summary>Answer key</summary>

1. Multiple leaders exist due to partition.
1. Ensures majority agreement before committing actions.
1. Mean Time To Recovery.


</details>

**Deliverables**
- Chaos test scripts
- Metrics & report


---


### Week 37: Elective B — Observability & Ops
**Topic tag:** Distributed Systems • **Estimated hours:** 10h • **Major deliverable:** Tracing + metrics + dashboards

**Learning objectives**
- Instrument distributed apps
- Visualize latency & error rates
- Use data to drive improvements


**Read / watch**
- **MIT 6.5840 (Distributed Systems)** — Selected ops/observability case studies (2h). [MIT 6.5840 (Distributed Systems)](https://pdos.csail.mit.edu/6.824/)


**Exercises & problem sets (with solutions/rubric)**
- Add logging, metrics, and tracing to your system; simulate load and collect data.


**Project milestone**
- **Spec:** Expose /metrics; propagate trace IDs; dashboards.
- **Acceptance criteria & tests:** Latency SLO met on test load; dashboards show trends.
- **Repo structure**
```text
distributed-systems/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add autoscaling policy
- Add alerting rules

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What are the 'three pillars' of observability?
1. Define SLO vs SLA.
1. Why sample traces?


<details>
<summary>Answer key</summary>

1. Logs, metrics, traces.
1. SLO is internal target; SLA is external contractual commitment.
1. Reduce overhead while preserving insight.


</details>

**Deliverables**
- Instrumented service
- Dashboards + SLO report


---


### Week 38: Performance & Profiling
**Topic tag:** Performance • **Estimated hours:** 9.5h • **Major deliverable:** Optimized module + performance report

**Learning objectives**
- Profile before optimising
- Apply algorithmic + micro-optimisations
- Quantify improvements


**Read / watch**
- **Pro Git** — Bisect to find perf regressions (0.5h). [Pro Git](https://git-scm.com/book/en/v2)


**Exercises & problem sets (with solutions/rubric)**
- Use profilers (`cProfile`, `time`, `perf`) on earlier projects; identify bottlenecks.


**Project milestone**
- **Spec:** Pick one project; profile, optimize, and compare.
- **Acceptance criteria & tests:** ≥2x speedup on a target scenario or justified constraints.
- **Repo structure**
```text
performance/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Parallelize with multiprocessing/async
- Add caching

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Why measure wall time and CPU time?
1. What is Amdahl’s law?
1. When is caching harmful?


<details>
<summary>Answer key</summary>

1. To separate system load from algorithmic cost.
1. Speedup limited by serial fraction.
1. When it increases memory/complexity and misses dominate.


</details>

**Deliverables**
- Perf report with charts
- Optimized code


---


### Week 39: Checkpoint #3: Review & Writeups
**Topic tag:** Meta • **Estimated hours:** 6.5h • **Major deliverable:** Portfolio polishing + essays

**Learning objectives**
- Synthesize learning
- Communicate clearly
- Polish artifacts for employers


**Read / watch**
- **Google Doc Style** — Editing and proofreading (0.5h). [Google Doc Style](https://developers.google.com/style/)


**Exercises & problem sets (with solutions/rubric)**
- Write 2 reflective essays: what you can now build; how you learn CS concepts.
- Polish docs across repos; add diagrams where missing.


**Project milestone**
- **Spec:** Essays (1–2 pages each) + repo-wide doc updates.
- **Acceptance criteria & tests:** Clarity, correctness, completeness (rubric 0–4).
- **Repo structure**
```text
meta/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Create a personal site (GitHub Pages)
- Record short demo videos

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What are your top 3 strongest CS skills now?
1. What’s one topic to deepen post-course?
1. Where will you publish your portfolio?


<details>
<summary>Answer key</summary>

1. Self-evaluation.
1. Plan next steps.
1. e.g., GitHub Pages.


</details>

**Deliverables**
- Two essays
- Updated docs


---


### Week 40: APIs & Service Composition
**Topic tag:** Systems Integration • **Estimated hours:** 10.5h • **Major deliverable:** Compose two services + API gateway

**Learning objectives**
- Compose services
- Manage config & secrets
- Test end-to-end


**Read / watch**
- **Docker** — Dockerizing apps (1.5h). [Docker](https://docs.docker.com/get-started/)


**Exercises & problem sets (with solutions/rubric)**
- Containerize two earlier services; compose with Docker Compose; add gateway.


**Project milestone**
- **Spec:** `docker-compose.yml` with API gateway and two services.
- **Acceptance criteria & tests:** End-to-end tests pass; configuration documented.
- **Repo structure**
```text
systems-integration/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Add service discovery
- Use environment-specific configs

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is service discovery?
1. Why use env vars for config?
1. How to avoid secret leakage?


<details>
<summary>Answer key</summary>

1. Finding service endpoints dynamically.
1. 12-factor compatibility; simpler deployment.
1. Use secret managers; avoid committing secrets.


</details>

**Deliverables**
- Compose file
- E2E tests


---


### Week 41: Deployment & CI/CD
**Topic tag:** Systems Integration • **Estimated hours:** 9.5h • **Major deliverable:** Cloud-like deployment simulation

**Learning objectives**
- Automate deployments
- Protect main branches
- Roll back safely


**Read / watch**
- **GitHub Actions** — Multi-job pipelines + environments (1h). [GitHub Actions](https://docs.github.com/actions)


**Exercises & problem sets (with solutions/rubric)**
- Add staging/prod pipelines; protect branches; add smoke tests.


**Project milestone**
- **Spec:** Pipeline with build/test/deploy + approvals.
- **Acceptance criteria & tests:** Green pipeline deploys to staging on PR; prod on tagged release.
- **Repo structure**
```text
systems-integration/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Blue/green or canary deploys
- Add IaC stub

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Why separate staging and prod?
1. What is a canary release?
1. Why require approvals?


<details>
<summary>Answer key</summary>

1. To test changes in prod-like env safely.
1. Release to small % to limit blast radius.
1. Reduce risk and enforce review.


</details>

**Deliverables**
- Pipelines
- Docs


---


### Week 42: Observability & SRE Basics
**Topic tag:** Systems Integration • **Estimated hours:** 8.5h • **Major deliverable:** SLOs + error budgets + alerts

**Learning objectives**
- Set meaningful SLOs
- Respond to incidents
- Learn from postmortems


**Read / watch**
- **MIT 6.5840 (Distributed Systems)** — Ops case studies (selected) (1.5h). [MIT 6.5840 (Distributed Systems)](https://pdos.csail.mit.edu/6.824/)


**Exercises & problem sets (with solutions/rubric)**
- Define SLOs; set alerts; simulate incidents and write postmortems.


**Project milestone**
- **Spec:** SLO doc + alerts + 1 postmortem.
- **Acceptance criteria & tests:** Alerts fire appropriately; postmortem follows template.
- **Repo structure**
```text
systems-integration/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Run a game day
- Automate incident runbooks

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. Define error budget.
1. Why blameless postmortems?
1. What’s the golden signal set?


<details>
<summary>Answer key</summary>

1. Allowable unreliability to meet SLOs.
1. Encourage learning and transparency.
1. Latency, traffic, errors, saturation.


</details>

**Deliverables**
- SLOs
- Alerts
- Postmortem


---


### Week 43: Capstone Proposal & Literature Review
**Topic tag:** Capstone Prep • **Estimated hours:** 10.5h • **Major deliverable:** Approved proposal + lit review

**Learning objectives**
- Plan effectively
- De-risk unknowns
- Prepare for final build


**Read / watch**
- **Pro Git** — Project planning with issues/milestones (0.5h). [Pro Git](https://git-scm.com/book/en/v2)


**Exercises & problem sets (with solutions/rubric)**
- Follow the provided template for this phase; commit artifacts to `/capstone` repo.


**Project milestone**
- **Spec:** Two candidate project ideas; feasibility; risks; success metrics.
- **Acceptance criteria & tests:** Artifacts meet template; reviewed against rubric.
- **Repo structure**
```text
capstone-prep/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Seek external feedback
- Add risk burndown chart

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What problem do you solve?
1. Who are the users?
1. How will you evaluate success?


<details>
<summary>Answer key</summary>

1. Free-form
1. Free-form
1. Free-form


</details>

**Deliverables**
- Approved proposal + lit review


---


### Week 44: Design Doc & Architecture
**Topic tag:** Capstone Prep • **Estimated hours:** 10.5h • **Major deliverable:** Design doc + diagrams

**Learning objectives**
- Plan effectively
- De-risk unknowns
- Prepare for final build


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Follow the provided template for this phase; commit artifacts to `/capstone` repo.


**Project milestone**
- **Spec:** Architecture diagram, APIs, data model, component responsibilities, risks.
- **Acceptance criteria & tests:** Artifacts meet template; reviewed against rubric.
- **Repo structure**
```text
capstone-prep/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Seek external feedback
- Add risk burndown chart

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What are major components?
1. What are trust boundaries?
1. What are performance targets?


<details>
<summary>Answer key</summary>

1. Free-form
1. Free-form
1. Free-form


</details>

**Deliverables**
- Design doc + diagrams


---


### Week 45: Prototype 1: Core Path
**Topic tag:** Capstone Prep • **Estimated hours:** 10.5h • **Major deliverable:** Walking skeleton

**Learning objectives**
- Plan effectively
- De-risk unknowns
- Prepare for final build


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Follow the provided template for this phase; commit artifacts to `/capstone` repo.


**Project milestone**
- **Spec:** Minimal slice through system (hello world end-to-end).
- **Acceptance criteria & tests:** Artifacts meet template; reviewed against rubric.
- **Repo structure**
```text
capstone-prep/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Seek external feedback
- Add risk burndown chart

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What’s the thinnest vertical slice?
1. What’s the riskiest assumption?
1. How will you test it?


<details>
<summary>Answer key</summary>

1. Free-form
1. Free-form
1. Free-form


</details>

**Deliverables**
- Walking skeleton


---


### Week 46: Prototype 2: Data & Auth
**Topic tag:** Capstone Prep • **Estimated hours:** 10.5h • **Major deliverable:** Data model + auth working

**Learning objectives**
- Plan effectively
- De-risk unknowns
- Prepare for final build


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Follow the provided template for this phase; commit artifacts to `/capstone` repo.


**Project milestone**
- **Spec:** Implement data persistence and user auth; add tests.
- **Acceptance criteria & tests:** Artifacts meet template; reviewed against rubric.
- **Repo structure**
```text
capstone-prep/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Seek external feedback
- Add risk burndown chart

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What’s your threat model?
1. How will you migrate schemas?
1. What are backup policies?


<details>
<summary>Answer key</summary>

1. Free-form
1. Free-form
1. Free-form


</details>

**Deliverables**
- Data model + auth working


---


### Week 47: Prototype 3: Scale & Resilience
**Topic tag:** Capstone Prep • **Estimated hours:** 10.5h • **Major deliverable:** Load test + resilience plan

**Learning objectives**
- Plan effectively
- De-risk unknowns
- Prepare for final build


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Follow the provided template for this phase; commit artifacts to `/capstone` repo.


**Project milestone**
- **Spec:** Add caching/queues; run load test; improve error handling.
- **Acceptance criteria & tests:** Artifacts meet template; reviewed against rubric.
- **Repo structure**
```text
capstone-prep/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Seek external feedback
- Add risk burndown chart

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What is target QPS?
1. Where are bottlenecks?
1. How do you degrade gracefully?


<details>
<summary>Answer key</summary>

1. Free-form
1. Free-form
1. Free-form


</details>

**Deliverables**
- Load test + resilience plan


---


### Week 48: Final Capstone Plan
**Topic tag:** Capstone Prep • **Estimated hours:** 9.5h • **Major deliverable:** Feature-complete plan + test matrix

**Learning objectives**
- Plan effectively
- De-risk unknowns
- Prepare for final build


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Follow the provided template for this phase; commit artifacts to `/capstone` repo.


**Project milestone**
- **Spec:** Feature list locked; test plan; release plan.
- **Acceptance criteria & tests:** Artifacts meet template; reviewed against rubric.
- **Repo structure**
```text
capstone-prep/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Seek external feedback
- Add risk burndown chart

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What remains to build?
1. What is the cut line?
1. What is your demo plan?


<details>
<summary>Answer key</summary>

1. Free-form
1. Free-form
1. Free-form


</details>

**Deliverables**
- Feature-complete plan + test matrix


---


### Week 49: Capstone Build I
**Topic tag:** Capstone • **Estimated hours:** 12h • **Major deliverable:** MVP feature set

**Learning objectives**
- Implement features to spec
- Maintain quality via tests/CI
- Prepare a compelling defense


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Execute the plan; update risks weekly; keep demo script up to date.


**Project milestone**
- **Spec:** Deliverables per Capstone Spec (below).
- **Acceptance criteria & tests:** All acceptance tests pass; demo flows work; rubric ≥3 in all categories.
- **Repo structure**
```text
capstone/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Polish UX
- Add optional advanced features

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What did you learn this week?
1. What risks remain?
1. What’s your demo story?


<details>
<summary>Answer key</summary>

1. Reflection
1. Risk tracking
1. Narrative


</details>

**Deliverables**
- MVP feature set


---


### Week 50: Capstone Build II
**Topic tag:** Capstone • **Estimated hours:** 12h • **Major deliverable:** Feature complete + tests

**Learning objectives**
- Implement features to spec
- Maintain quality via tests/CI
- Prepare a compelling defense


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Execute the plan; update risks weekly; keep demo script up to date.


**Project milestone**
- **Spec:** Deliverables per Capstone Spec (below).
- **Acceptance criteria & tests:** All acceptance tests pass; demo flows work; rubric ≥3 in all categories.
- **Repo structure**
```text
capstone/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Polish UX
- Add optional advanced features

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What did you learn this week?
1. What risks remain?
1. What’s your demo story?


<details>
<summary>Answer key</summary>

1. Reflection
1. Risk tracking
1. Narrative


</details>

**Deliverables**
- Feature complete + tests


---


### Week 51: Capstone Stabilize
**Topic tag:** Capstone • **Estimated hours:** 11h • **Major deliverable:** Perf hardening + docs

**Learning objectives**
- Implement features to spec
- Maintain quality via tests/CI
- Prepare a compelling defense


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Execute the plan; update risks weekly; keep demo script up to date.


**Project milestone**
- **Spec:** Deliverables per Capstone Spec (below).
- **Acceptance criteria & tests:** All acceptance tests pass; demo flows work; rubric ≥3 in all categories.
- **Repo structure**
```text
capstone/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Polish UX
- Add optional advanced features

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What did you learn this week?
1. What risks remain?
1. What’s your demo story?


<details>
<summary>Answer key</summary>

1. Reflection
1. Risk tracking
1. Narrative


</details>

**Deliverables**
- Perf hardening + docs


---


### Week 52: Capstone Deliver & Defend
**Topic tag:** Capstone • **Estimated hours:** 12h • **Major deliverable:** Deployed app + report + oral defense

**Learning objectives**
- Implement features to spec
- Maintain quality via tests/CI
- Prepare a compelling defense


**Read / watch**


**Exercises & problem sets (with solutions/rubric)**
- Execute the plan; update risks weekly; keep demo script up to date.


**Project milestone**
- **Spec:** Deliverables per Capstone Spec (below).
- **Acceptance criteria & tests:** All acceptance tests pass; demo flows work; rubric ≥3 in all categories.
- **Repo structure**
```text
capstone/
├─ README.md
├─ src/
├─ tests/
├─ data/        # if needed
├─ requirements.txt (Python) / package.json (JS)
└─ .github/workflows/ci.yml
```
- **Linters/formatters:** - Python: `black`, `flake8`, `pytest` • JS: `eslint`, `prettier`
- **Stretch goals:** - Polish UX
- Add optional advanced features

- **Submission checklist**
- README includes problem statement, approach, and instructions
- All tests passing locally and in CI
- Static analysis (flake8/eslint) shows no errors
- Formatting (black/prettier) applied
- Time log (effort in hours) committed


**Assessment: short quiz**
1. What did you learn this week?
1. What risks remain?
1. What’s your demo story?


<details>
<summary>Answer key</summary>

1. Reflection
1. Risk tracking
1. Narrative


</details>

**Deliverables**
- Deployed app + report + oral defense


---

### Rubrics (0–4 scale)
- **Correctness:** 0 no working solution · 1 partially works · 2 mostly works with bugs · 3 correct on tests · 4 correct incl. edge cases & robust.
- **Design:** 0 ad-hoc · 1 poor structure · 2 some structure · 3 clear modularity & interfaces · 4 excellent abstractions & justified tradeoffs.
- **Analysis/Explanation:** 0 none · 1 superficial · 2 partial · 3 sound reasoning · 4 rigorous incl. complexity/perf & alternatives.
- **Testing:** 0 none · 1 minimal · 2 some unit tests · 3 good unit+integration tests, coverage ≥80% · 4 property/fuzz tests + CI.
- **Documentation:** 0 none · 1 sparse · 2 basic README · 3 clear README/API docs · 4 polished docs incl. diagrams, style adherence.

## Consolidated Reading List (canonical links)
- **CS50** — https://cs50.harvard.edu/x/
- **MCS (MIT 6.042J)** — https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf
- **Nand2Tetris** — https://www.nand2tetris.org/
- **OSTEP** — https://pages.cs.wisc.edu/~remzi/OSTEP/
- **Patterson & Hennessy (COD)** — https://books.google.com/books/about/Computer_Organization_and_Design.html?id=1lD9LZRcIZ8C
- **Tanenbaum OS (OSDI)** — https://archive.org/details/operating-systems-design-and-implementation-tanenbaum-2006
- **CS61B (DS)** — https://sp25.datastructur.es/
- **CMU 15-445 (DB)** — https://15445.courses.cs.cmu.edu/fall2025/syllabus.html
- **Beej Sockets** — https://beej.us/guide/bgnet/
- **Stanford CS144** — https://cs144.github.io/
- **Berkeley CS161** — https://fa25.cs161.org/
- **Security Engineering** — https://www.cl.cam.ac.uk/archive/rja14/book.html
- **Crafting Interpreters** — https://craftinginterpreters.com/
- **MIT 6.5840 (Distributed Systems)** — https://pdos.csail.mit.edu/6.824/
- **fast.ai** — https://course.fast.ai/
- **CS229 notes** — https://cs229.stanford.edu/notes2022fall/main_notes.pdf
- **Berkeley CS184 (Graphics)** — https://cs184.eecs.berkeley.edu/
- **Pro Git** — https://git-scm.com/book/en/v2
- **Google Doc Style** — https://developers.google.com/style/
- **ACM Code of Ethics** — https://www.acm.org/code-of-ethics
- **Cryptopals** — https://www.cryptopals.com/
- **Design of Everyday Things** — https://mitpress.mit.edu/9780262525671/the-design-of-everyday-things/
- **Google Eng Practices (Code Review)** — https://google.github.io/eng-practices/review/
- **pytest** — https://docs.pytest.org/
- **Black** — https://black.readthedocs.io/
- **flake8** — https://flake8.pycqa.org/
- **ESLint** — https://eslint.org/
- **Prettier** — https://prettier.io/
- **Docker** — https://docs.docker.com/get-started/
- **GitHub Actions** — https://docs.github.com/actions
- **PostgreSQL** — https://www.postgresql.org/docs/

### Skills Map (topic → objectives → artifacts)
- **Programming foundations:** packaging; testing; APIs → CLI tools, HTTP service
- **DS&A:** complexity; classic structures; sorting → DS library + analysis notes
- **Architecture:** logic→CPU→memory → Nand2Tetris HDL projects + explainers
- **OS:** processes/threads/memory → mini-labs + writeups
- **Networking:** sockets/TCP/HTTP → client/server + pcap analysis
- **Databases:** SQL/transactions/indexes → schema scripts + EXPLAIN reports
- **Software Eng:** reviews/docs/CI → CONTRIBUTING + CI pipelines
- **Theory:** automata/computability → proofs + regex engine
- **Security:** crypto/software/web → Cryptopals + hardened service
- **HCI:** prototyping/usability → prototype + report
- **Electives:** compilers/distributed/graphics/ML → working artifact
- **Capstone:** system integration → deployed app + performance report + defense


## Capstone Specification (Weeks 49–52)
**Goal:** Build a production‑like, networked system that integrates *systems + theory*.

**Requirements**
- **Functionality:** A multi‑user service (e.g., image catalog, note‑taking app, or task manager) with auth, CRUD, search, and background jobs.
- **Architecture:** ≥2 services; database; message queue or background worker; HTTP API; CLI/tooling.
- **Quality:** Tests (unit+integration+e2e); lint/format; docs; CI/CD; containerized run.
- **Performance targets:** Handle 200 req/min with p95 latency < 300 ms on your machine; include load‑test results.
- **Security:** Basic threat model; input validation; authN/Z; secure storage of secrets.
- **Report:** 6–10 pages covering design, tradeoffs, testing, performance, and future work.
- **Oral defense:** 10–15 minute recorded demo + Q&A prompts (included).

**Grading rubric:** same 0–4 categories; capstone must average ≥3.0 and no category <2.5.

