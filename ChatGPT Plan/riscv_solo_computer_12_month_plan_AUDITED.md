# Build-Your-Own RISC‑V Computer — 12‑Month Solo Roadmap

> A realistic path for an individual to design, implement, and boot a Linux‑capable RISC‑V computer on an FPGA — from zero HDL to a working SoC. Weekly checkpoints, deliverables, and acceptance tests included.

---

## Who this is for

- You’re comfortable with programming (Python/JS/C basics) but **new to digital design/HDL**.
- You can dedicate ~**8–12 hrs/week** for 12 months.
- You’re fine starting on **FPGA** (affordable, reprogrammable) instead of ASIC.

---

## Outcomes by Month 12

- A working **RISC‑V SoC** (RV32IM with MMU) on an FPGA dev board.
- Boots **Linux** from SD card; provides a **serial console** (and optional Ethernet/VGA).
- You understand the full stack: **HDL → CPU → SoC → bootloader → kernel → userland**.
- Repos with clean docs, testbenches, CI, and reproducible builds.

---

## Hardware & Tools (recommended)

- **FPGA board**: Digilent **Arty A7-100T** *or* Lattice **ECP5-85F** (e.g., **ULX3S**). These have sufficient logic/BRAM for a Linux-capable RV32 core with MMU.
  > Note: The **Arty A7-35T** is excellent for the early months (UART/SoC bring-up) but is typically **too resource-constrained** for a comfortable Linux-on-RISC‑V flow.
  Alternatives: Efinix Trion boards with sufficient LUTs/BRAM.
- **Serial/USB** cable; **MicroSD** card (>=8GB); optional **USB‑Ethernet** PHY add-on (if your board needs it).
- **Tooling**:
  - Open-source: `yosys`, `verilator`, `gtkwave`, `riscv-gnu-toolchain`. For place-and-route: `nextpnr-ecp5` (ECP5) is mature; **Xilinx 7‑series** (Arty A7) generally uses **Vivado** (open-source flows exist but are experimental).
  - Vendor: **Xilinx Vivado** for Arty A7; **Lattice Radiant/Trellis+nextpnr-ecp5** for ECP5.
- **Reference open cores** (study/use where helpful):
  - [PicoRV32](https://github.com/cliffordwolf/picorv32)
  - [VexRiscv](https://github.com/SpinalHDL/VexRiscv)
  - [LiteX](https://github.com/enjoy-digital/litex) (framework for SoCs/peripherals)
  - [Zephyr RTOS](https://zephyrproject.org/)
  - [Buildroot](https://buildroot.org/)/[BusyBox](https://busybox.net/)

> ✅ **Philosophy:** You’ll implement core pieces yourself to learn, but you’ll also leverage **known-good IP** for time sinks (e.g., SDRAM controllers). Balance learning vs. shipping.

---

## Study Pattern

Every month includes:
- **Objectives** (what you’ll know/do)
- **Reading/Watch List**
- **Weekly Plan**
- **Deliverables & Acceptance Tests**
- **Stretch Goals** (optional)

---

## Month 1 — Digital Logic & HDL Basics

**Objectives**
- Understand combinational vs sequential logic, FSMs, registers, timing.
- Write/simulate Verilog/SystemVerilog (or VHDL) modules and testbenches.

**Reading/Watch**
- *Digital Design & Computer Architecture* (Harris/Harris) — Ch. 1–3.  
- Verilog/VHDL tutorial series (FPGA4Fun, HDLBits, or official language guides).
- Verilator + GTKWave quickstart.

**Weekly Plan**
1. Boolean algebra, gates; write adders/ALU slices; simulate in Verilator.
2. Flip‑flops, counters, debouncers; create a clock‑enable; simulate.
3. FSMs: traffic light, UART‑RX FSM (simulation only).
4. Put on hardware: **Blinky** + button debounce + LED patterns on FPGA.

**Deliverables**
- `hdl/` modules + `tb/` testbenches; CI running sims.
- Video/GIF of blinky + docs.

**Acceptance**
- All unit tests pass; waveforms inspected for UART‑RX FSM.

---

## Month 2 — Bus, Memory, and UART I/O

**Objectives**
- Learn simple on‑chip bus (Wishbone/AXI‑lite style), memory-mapped I/O.
- Implement a working **UART TX/RX** on FPGA.

**Reading/Watch**
- Wishbone or AXI‑Lite spec (pick one style and be consistent).
- UART protocol basics.

**Weekly Plan**
1. BRAM + simple bus interface; address decode.
2. UART‑TX in HDL; loopback test in sim.
3. UART‑RX; oversampling and framing error handling.
4. Integrate TX/RX; bring-up over USB‑serial; write a tiny ROM echo program.

**Deliverables**
- `uart/` core with testbench; memory map doc.
- ROM monitor: echo typed chars.

**Acceptance**
- Type in a terminal → echoed reliably at e.g., 115200 bps.

---

## Month 3 — Minimal RV32I CPU

**Objectives**
- Implement a simple **RV32I** core (single-cycle or 2‑stage).
- Pass the official ISA tests for the subset you implement.

**Reading/Watch**
- RISC‑V Unprivileged ISA Manual — RV32I.
- Explore PicoRV32 for reference (don’t copy; compare designs).

**Weekly Plan**
1. Instruction fetch/decode/execute skeleton, regfile, ALU ops.
2. Branch/jump handling; immediate decoding; PC update.
3. Load/store; alignment; exceptions (basic).
4. Run `riscv-tests` subset in Verilator; fix until green.

**Deliverables**
- `cpu/rv32i/` core + tests; instruction coverage report.

**Acceptance**
- All RV32I base tests pass in simulation; simple C programs run (via `-nostdlib`).

---

## Month 4 — SoC v0: Boot ROM, Timer, UART Console

**Objectives**
- Build a minimal **SoC**: CPU + BRAM + UART + timer + ROM monitor.
- Load binaries over serial into RAM and execute.

**Reading/Watch**
- Simple bootloader design; linker scripts; RISC‑V calling convention.

**Weekly Plan**
1. Top-level SoC + address map; CSR block for timer/IRQ.
2. Boot ROM: tiny monitor (peek/poke, mem-load via XMODEM/S‑record).
3. Cross-compile bare‑metal C; printf over UART.
4. Interrupts: timer tick increments counter; basic exception trap.

**Deliverables**
- `soc/min/` with ROM monitor + docs.
- Host tool to send binaries (Python script).

**Acceptance**
- From serial console, load a program into RAM and run it successfully.

---

## Month 5 — Peripherals & RTOS Bring‑up

**Objectives**
- Add SPI (for SD card) or QSPI flash; GPIO; simple PWM.
- **Port Zephyr RTOS** (or another small RTOS) to your SoC.

**Reading/Watch**
- Zephyr board porting guide; SPI protocol; SD card SPI mode.

**Weekly Plan**
1. SPI master + SD card init (SPI mode).
2. Block read/write to SD; simple FS (FatFs) under bare-metal.
3. Zephyr: define DTS/board files; UART console driver.
4. Zephyr threads/timers running; shell over UART.

**Deliverables**
- SPI core + SD driver; Zephyr “hello world” on hardware.

**Acceptance**
- Zephyr boots with shell; can read a file from SD.

---

## Month 6 — Multiply/Divide (M) & Pipeline Cleanups

**Objectives**
- Add **RV32M** (mul/div) unit; improve CPI via simple pipeline.
- Stabilize exception/trap paths.

**Reading/Watch**
- RISC‑V “M” extension; pipeline hazards; bypassing basics.

**Weekly Plan**
1. MUL/MULH variants; verify with directed tests.
2. DIV/REM; handle div-by-zero spec.
3. 2–3 stage pipeline; hazard detection; basic forwarding.
4. Performance runs; update docs/spec.

**Deliverables**
- `cpu/rv32im/` core; benchmarks (CoreMark) pre/post.

**Acceptance**
- CoreMark improves vs Month 3; all M‑tests pass.

---

## Month 7 — External SDRAM & Caches

**Objectives**
- Attach external **SDRAM** (or SRAM if your board has it).
- Implement **I‑cache/D‑cache** (small, direct-mapped).

**Reading/Watch**
- Your board’s SDRAM controller IP (reuse a proven core if needed).
- Cache basics; write-through vs write-back.

**Weekly Plan**
1. Integrate SDRAM controller; memory map; timing closure.
2. Boot with SDRAM as main RAM; stress tests (memtester).
3. Add I‑cache; measure instruction fetch stalls.
4. Add D‑cache (write-through first); coherence with MMIO.

**Deliverables**
- Cache controllers + validation tests; memory stress report.

**Acceptance**
- Stable operation from SDRAM; caches measurably reduce stalls.

---

## Month 8 — Privileged Spec & MMU

**Objectives**
- Implement RISC‑V **privileged architecture** (M/S/U modes).
- Add a **Sv32 MMU** with TLBs; handle page faults and traps.

**Reading/Watch**
- RISC‑V Privileged Spec (focus on Sv32).
- Linux RISC‑V boot requirements (for RV32).

**Weekly Plan**
1. CSR set for modes, interrupts, exceptions; trap vector.
2. Page table walker; TLB (ITLB/DTLB) design and refill policy.
3. Sv32 mapping tests; user/kernel isolation.
4. Integrate **OpenSBI** (SBI v0.3+) as the machine-mode firmware. Optionally add **U‑Boot** as a second-stage bootloader.

**Deliverables**
- MMU + TLB + page table walker; compliance tests.

**Acceptance**
- Userland cannot access kernel pages; page faults/traps correct under tests.

---

## Month 9 — Linux Bring‑up (Serial Console)

**Objectives**
- Boot a **Linux kernel** (RV32) with serial console.
- Provide rootfs via SD card (Buildroot + BusyBox).

**Reading/Watch**
- RISC‑V Linux kernel config; Buildroot workflow; device tree (DT).

**Weekly Plan**
1. Create DTS for your SoC; kernel defconfig; compile.
2. Buildroot: minimal rootfs + BusyBox; init=/bin/sh.
3. Boot logs over UART; debug hangs (earlycon).
4. Document boot flow: **Boot ROM (on-chip)** → **OpenSBI (M-mode)** → *(optional)* **U‑Boot** → **Linux kernel** → **init**.

**Deliverables**
- Kernel + rootfs images; DTS; boot logs.

**Acceptance**
- “`/ #`” BusyBox shell over serial on your hardware.

---

## Month 10 — Drivers & Networking

**Objectives**
- Add **Ethernet** MAC (or USB-to-serial networking) and bring up TCP/IP. *Hardware note:* boards like the **Arty A7** do **not** include an onboard Ethernet PHY; you’ll need a **PMOD RMII/RGMII PHY** or use a board with built‑in Ethernet.
- Flesh out drivers (timer, SPI, GPIO) in Linux.

**Reading/Watch**
- LiteEth or vendor MAC IP; Linux driver model basics.

**Weekly Plan**
1. Integrate MAC IP; DMA ring buffers.
2. Minimal Linux driver or use existing one via DT.
3. Bring up `ifconfig`, DHCP or static IP; test `ping`.
4. Package userland tools (dropbear, curl, busybox extras).

**Deliverables**
- Networking working; docs on how to reproduce.

**Acceptance**
- `ping` works both ways; `wget` or `scp` transfers a file.

---

## Month 11 — Graphics / Storage / Polishing

**Objectives**
- Optional **VGA/HDMI** text console or simple framebuffer.
- Improve storage (ext4 on SD), init scripts, and reliability.

**Reading/Watch**
- LiteVideo or simple HDMI IP; console framebuffer basics.

**Weekly Plan**
1. Video out IP integration (or skip if not desired).
2. Framebuffer console in Linux; ASCII text mode.
3. Rootfs hardening; fstab; clean shutdown; journaling FS.
4. QA pass: soak tests; document known issues.

**Deliverables**
- Optional video console; robust rootfs; comprehensive README.

**Acceptance**
- System runs for 24h under load without crash; graceful shutdown works.

---

## Month 12 — Capstone, Performance, and Report

**Objectives**
- Finalize **capstone demo**; measure and report performance.
- Clean repositories; write a **technical report** and a **hands-on guide**.

**Weekly Plan**
1. Benchmarks: CoreMark/LMbench; memory bandwidth; boot time.
2. End-to-end demo: “from power-on to Linux shell + network”.
3. Write the report (architecture, tradeoffs, results, lessons).
4. Publish: tagged release, reproducible build scripts, BOM.

**Deliverables**
- Public repo(s) with tagged v1.0; 10–20 page PDF report; video demo.

**Acceptance**
- A new user can follow your guide and boot Linux on your SoC.

---

## Risk Management & Tips

- **Timing closure**: keep clocks modest (25–50 MHz). Pipe where needed.
- **Reuse IP wisely**: SDRAM and Ethernet are time sinks — use proven cores (e.g., **LiteDRAM** for SDRAM, **LiteEth** for Ethernet).
- **Test early, test often**: simulate modules; add assertions; CI on sims.
- **Document** as you go: memory maps, register docs, build scripts.
- **Keep interfaces clean**: ready/valid handshakes, stable bus timing.

---

## Stretch Goals

- RV64 (64-bit) variant (if your FPGA resources allow). Linux RV64 is more common in the ecosystem, with wider prebuilt toolchain support.
- More cache levels; branch predictor.
- SMP (dual-core) with CLINT/PLIC.
- DMA engine; SDIO; USB host/device.
- JTAG debug (OpenOCD/gdb) integration.
- Custom ISA extensions for acceleration.

---

## Repository Layout (suggested)

```
riscv-solo-computer/
├─ docs/                # specs, memory map, bring-up notes
├─ fpga/                # board-specific files, constraints
├─ hdl/
│  ├─ cpu/              # rv32i/m core(s)
│  ├─ mmu/              # sv32 + tlb
│  ├─ cache/            # icache/dcache
│  ├─ bus/              # interconnect, bridges
│  ├─ periph/           # uart, spi, gpio, timer, mac, video
│  └─ sdram/            # controller + PHY glue
├─ tb/                  # testbenches (verilator)
├─ soc/
│  ├─ min/              # Month 4 SoC
│  └─ full/             # Linux-capable SoC
├─ sw/
│  ├─ bootrom/          # monitor/bootloader
│  ├─ opensbi/          # OpenSBI platform port
│  ├─ u-boot/           # optional secondary bootloader
│  ├─ baremetal/        # tests, demos
│  ├─ zephyr/           # BSP & samples
│  └─ linux/            # dts, defconfig, build scripts
├─ tools/               # host-side utilities (Python, etc.)
├─ scripts/             # build, flash, run, CI
└─ ci/                  # GitHub Actions or similar
```

---

## Weekly Time Budget (example)

- **2–3h reading** (specs, chapters, app notes)
- **4–6h implementation** (HDL/C/driver work)
- **2–3h testing & docs** (sim, bench, write-ups)

---

## License & Attribution

- License your HDL under a permissive license (e.g., Apache‑2.0/MIT).  
- Attribute third‑party IP clearly in `docs/THIRD_PARTY.md`.

---

*You’ve got this. Ship something small every week, and protect your weekends.* 🚀
