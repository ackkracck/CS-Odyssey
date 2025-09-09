# Build‑a‑Computer Learning Plan (6‑Week Mini‑Roadmap)

> A playful-yet-rigorous path to understand how computers work—from **bits and gates** to a **tiny CPU you design** and **program**—with options to go hands-on in hardware or FPGAs.

**Time:** ~10–12 hrs/week • **Prereqs:** Basic programming comfort (variables/loops/functions) • **Outcomes:** Design a minimal CPU, write simple assembly, and explain the hardware–software stack end to end.

---

## Week 1 — Bits → Gates (play & visualize)
**Goals**
- Grasp binary, truth tables, and combinational vs. sequential logic.
- Build core parts: half/full adders, multiplexers, and a D flip‑flop.

**Do**
- **Play:** *NandGame* — finish the **Combinational** and **Sequential** sets.
- **Visualize/Build:** In **Logisim Evolution** or **CircuitVerse**, recreate:
  - Half‑adder, full‑adder, 2:1 mux
  - D flip‑flop (with enable)
- **Deliverable:** A screenshot collage + 3–5 sentences describing each component.

**Resources**
- NandGame (browser)
- Logisim Evolution (desktop) • CircuitVerse (web)
- (Optional) “Code: The Hidden Language of Computer Hardware and Software” — chapters on codes and circuits

---

## Week 2 — Memory, ALU, and control signals
**Goals**
- Understand registers, RAM, and clocking.
- Design a small ALU and learn how control bits select operations.

**Do**
- **Play:** *Turing Complete* tutorials up through ALU & RAM.
- **Build:** In your simulator, implement an **8‑bit ALU** (ADD, SUB, AND, OR) and a tiny **register file** (e.g., 4×8‑bit).
- **Watch (optional):** Ben Eater’s 8‑bit computer playlist (ALU, clock, registers).

**Deliverable**
- ALU truth table(s) + a short note explaining control lines and status flags (e.g., zero/carry).

---

## Week 3 — A tiny CPU (datapath + ISA sketch)
**Goals**
- Learn how the PC, instruction memory, register file, and ALU connect.
- Draft a minimal **instruction set** and CPU **datapath** diagram.

**Do**
- **Course:** Nand2Tetris (Part I) — Projects 1–5 (focus on **Project 5: CPU**).
- **Play:** *MHRD* up to the first CPU spec level (good HDL thinking practice).
- **Design:** Draft your instruction formats and control signals (ADD, LOAD, STORE, JMP, JE).

**Deliverable**
- One‑page **ISA spec** + **datapath diagram** (PNG/SVG/PDF).

---

## Week 4 — Your first assembly & I/O
**Goals**
- Write and run simple assembly programs on a minimal CPU.
- See how memory‑mapped I/O works.

**Do**
- **Play/Finish:** *Turing Complete* CPU; write 3 small assembly programs:
  1. Sum of the first N integers
  2. Maximum of an array
  3. Loop with a conditional jump
- **RISC‑V sampler (optional):** Try **Ripes** (visual pipeline). Alternatives: **RARS** or **Venus**.

**Deliverable**
- Three assembly listings + expected/actual outputs, with a paragraph on how each maps to your datapath.

---

## Week 5 — Stretch paths (pick one)
**Game‑first path**
- *SHENZHEN I/O* or *TIS‑100* for assembly‑style problem solving and reading “datasheets.”

**Hardware‑curious path**
- Follow Ben Eater’s **clock + register** builds (or watch along).

**FPGA path**
- Work through **Project F** intros (graphics or RISC‑V assembler) to meet Verilog and toolchains.

**Deliverable**
- Short reflection (~250 words) on what the path taught you that your simulator didn’t.

---

## Week 6 — Capstone (minimal 8‑bit CPU)
**Build (sim)**
- Implement a **minimal 8‑bit CPU** with:
  - 2–4 registers, instruction memory, PC, ALU, and data memory
  - Core ops: `ADD`, `LOAD/STORE`, `JMP`, `JE` (or `JNZ`)
- **I/O flair:** Drive a 7‑segment display or a small text framebuffer (in‑sim).

**Write‑up**
- One‑page README covering: ISA, datapath, control signals, and a test program walk‑through.

**Submission checklist**
- ✅ Schematic/diagram
- ✅ Machine code + assembly for test programs
- ✅ Screenshots/trace showing correct execution

---

## Resource Directory (curated)

### Play & Build (games/sims)
- **Turing Complete** — simulator where you build from gates to a CPU and program it.
- **NandGame** — browser puzzle path from NAND to a programmable computer.
- **Logic World** — large‑scale logic sandbox (3D), great for big circuits (clocks, RAM, CPUs).
- **MHRD** — HDL puzzle game that culminates in a simple CPU.
- **Silicon Zeroes** — puzzles from adders and latches up to CPU‑like designs.
- **SHENZHEN I/O** — wire components and write compact assembly‑like code with datasheets.
- **TIS‑100** — assembly‑style programming puzzles for low‑level thinking.
- **Human Resource Machine** — friendly, visual introduction to assembly concepts.
- **Sim tools:** Logisim Evolution • CircuitVerse (web) • Digital (hneemann)

### Learn by Doing (courses & practice)
- **Nand2Tetris** (book + courses) — build the stack from gates → CPU → VM → simple OS.
- **MIT 6.004 Computation Structures** — classic notes, labs, and lectures.
- **HDLBits** — hundreds of bite‑sized Verilog exercises.
- **RISC‑V practice:** **Ripes** (visual), **RARS** / **Venus** (assemblers/sims).

### Readings (approachable → deep)
- **Code (2e)** — Petzold’s narrative from bits to computers.
- **How Computers Really Work** — circuits‑to‑OS with optional projects (Matthew Justice).
- **The Elements of Computing Systems** — the Nand2Tetris book.
- **The RISC‑V Reader** — concise modern ISA reference (Patterson & Waterman).
- **Digital Design and Computer Architecture** — full course‑style text (Harris & Harris).
- **Computer Organization and Design (RISC‑V ed.)** — the classic HW/SW interface.
- **The Art of Electronics (3e)** — real‑world electronics reference.
- **Make: Electronics (3e)** — hands‑on electronics primer.

### Optional Hardware Path
- **Ben Eater’s 8‑bit breadboard computer** (kits + videos).
- **FPGA on‑ramp:** **Project F** tutorials.
- **Microcontroller sims:** **Wokwi** (Arduino/ESP32/Pico) in your browser for quick I/O experiments.

---

## How to Work This Plan (habits that compound)
- **Daily 45‑minute block:** 20 min *play* (game/sim), 20 min *build* (your circuit), 5 min *notes*.
- **Weekly deliverable:** one diagram (datapath or truth table) + one tiny program (assembly or testbench).
- **Portfolio:** keep everything in a Git repo (circuits, screenshots, notes, capstone write‑up).

**Suggested repo structure**
```
build-a-computer/
  week01_bits_gates/
  week02_alu_memory/
  week03_cpu_design/
  week04_assembly_io/
  week05_path_choice/
  week06_capstone_cpu/
  docs/diagrams/
  tools/ (sim configs)
```

**License your learning:** add a permissive LICENSE; commit weekly with short logs describing what you learned.

---

## Acceptance Criteria (quick self‑check)
- You can **explain** combinational vs. sequential logic and draw truth tables.
- You can **design** a minimal 8‑bit CPU datapath and enumerate its ISA.
- You can **run** three assembly programs on your CPU (sum, max, loop/branch) and trace execution.
- You can **map** an I/O device via memory and interact with it from assembly.
- You can **compare** your sim experience to a hardware/FPGA approach in plain language.

Happy building! When you’re ready, I can expand this into an 8‑week or hardware‑only track tailored to your parts and budget.
