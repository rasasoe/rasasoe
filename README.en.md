<picture>
  <source media="(max-width: 600px)" srcset="assets/profile-banner-mobile.svg">
  <img src="assets/profile-banner.svg" width="100%" alt="Kim Min Gun — Security Engineering, Software Systems, Robotics">
</picture>

<p align="right"><a href="README.md">한국어</a> &nbsp; | &nbsp; <strong>English</strong></p>

# Kim Min Gun

**Software Engineering · Security · Systems · Robotics**

I build security analysis tools and integrate real-world robotics systems with ROS 2. I explain **why I started each project, which features and architecture I selected, and what I actually built and demonstrated**.

These projects are not claims to replace mature commercial security tools. They document hands-on verification automation, traceability, system integration, and failure-handling work.

Software Engineering undergraduate · Expected graduation: February 2027

[Technical blog](https://rasasoe.tistory.com/) · [Completed projects](#completed-projects) · [In progress](#in-progress)

---

## Completed Projects

These projects have documented implementation and demonstration or local test results. *Completed* refers only to the described and verified scope, not production certification.

**Date convention:** Where an actual project development period is documented, it is labeled as such. Otherwise, dates reflect **confirmed work or test activity**, not an assumed development start or completion date. Repository creation is not treated as project inception.

### 01. [VSH — Application Security Analysis](https://github.com/rasasoe/VSH)

**Documented activity and verification:** Feb–Sep 2026 (not a confirmed inception-to-completion period)

**Project aim:** Bring together **L1 static detection**, **L2 LLM explanations** of findings, and **optional L3 PoC generation and verification** into one developer-facing AppSec workflow.

<p align="center"><a href="https://github.com/rasasoe/VSH"><picture><source media="(max-width: 600px)" srcset="assets/vsh-workflow-mobile.svg"><img src="assets/vsh-workflow.svg" width="100%" alt="VSH L1 detection, L2 LLM explanation and optional L3 PoC generation and verification"></picture></a></p>

- **My contribution:** Built on an [upstream team-project fork](https://github.com/vmfmgl0607/VSH); individually extended Semgrep execution and configuration, Windows tool wrappers, Finding v1.0 JSON export, and tests.
- **Evidence:** 81 unit tests passed, the same 81 passed in reverse order, the React production build passed (September 16, 2026), and a local vulnerable-code fixture was displayed in the working analysis UI.
- **Verification boundary:** L1 has local test evidence; the L2 public demo uses mocks. End-to-end L3 PoC generation/execution, real LLM output quality, and field detection accuracy remain unverified.

`Python` · `FastAPI` · `Semgrep` · `React` · `Electron`

[Demo screenshot](https://github.com/rasasoe/VSH#실행-화면) · [Contributions and commits](https://github.com/rasasoe/VSH#my-contributions) · [Verification notes](https://github.com/rasasoe/VSH#검증과-한계)

### 02. [BuddyBot — Home AI Serving Robot Prototype](https://github.com/rasasoe/BuddyBot)

**Development period:** Mar 2025–Jun 2026  
**Three-person capstone · Team lead / system architecture / integration**

**Original idea:** Build an AI-assisted home serving robot that could understand spoken commands, navigate indoor spaces, and interact with people. The completed scope is a **mobile perception/navigation/interaction prototype**, not a household product proven to carry and serve items.

**Feature selection:** LiDAR-based environment sensing and obstacle avoidance, camera-based object/person recognition, microphone and STT voice commands, waypoint navigation, and person following.

<p align="center"><a href="https://github.com/rasasoe/BuddyBot#동작-데모"><img src="assets/buddybot.jpg" width="280" alt="Physical BuddyBot three-wheel omnidirectional robot"></a></p>

- **Architecture:** Integrated ROS 2 perception/navigation on Raspberry Pi 5 with Pico motor control over UART, plus command arbitration and watchdog-based stopping.
- **Built and demonstrated:** Checkpoint navigation, obstacle avoidance, person following, voice commands, and software emergency stop on the physical robot.
- **Scope:** Indoor movement and interaction are demonstrated; end-to-end item serving and production-grade safety are not claimed.

`ROS 2` · `Python` · `Raspberry Pi` · `RP2040` · `OpenCV`

[Working demos](https://github.com/rasasoe/BuddyBot#동작-데모) · [System architecture](https://github.com/rasasoe/BuddyBot#전체-아키텍처)

### Other Implemented and Tested Projects

| Project | Confirmed activity | Intended validation and evidence |
| --- | --- | --- |
| [DotasPlus](https://github.com/rasasoe/DotasPlus) | Dec 2025–Sep 2026 | Whether external IOC observations can be consistently linked to protected assets and incidents; 9 local fixture tests passed |
| [Python ASM Framework](https://github.com/rasasoe/python-asm-framework) | Feb–Sep 2026 | Whether authorized target controls and normalized attack-surface reports behave predictably; 6 offline unit tests passed |
| [AMR](https://github.com/rasasoe/AMR) | Oct 2025–Feb 2026 | Implemented and experimented with encoder feedback, proportional speed control, and inverse kinematics |
| [MRP3MV4](https://github.com/rasasoe/MRP3MV4) | Aug 2025–Feb 2026 | AVR/LM629 holonomic drive and sensor/camera movement experiments |

Dates in this table are **verified activity windows, not asserted full development periods**. DotasPlus and ASM use local or simulated test inputs; external end-to-end collection has not been independently verified.

---

## In Progress

### [AEGIS — Autonomous Security AI Platform](https://github.com/rasasoe/AEGIS-Showcase)

**In progress · documented public development/verification activity:** Oct 2026–present (not a confirmed initial start date)  
**Individual project · separating local-model reasoning from tool-execution authority**

**Validation goal:** Establish whether an agent can be prevented from executing unapproved targets or tools, whether STOP actually terminates **live agent processes**, and whether a reported security conclusion has **verifiable tool evidence**.

Integrating PentAGI and Ollama with scope validation, explicit approval, isolated execution, and evidence review.

- **Evidence:** Python Controller, model connection, approval/scope checks, simulated lifecycle monitor; 305/305 local regression tests passed as of October 26, 2026 (not a real vulnerability-discovery success rate).
- **Not yet validated:** Live PentAGI Flow termination and end-to-end authorized lab analysis with reproducible HTTP evidence and reporting.
- **Publication:** Design and verification reports are public; development source code remains private.

`Python` · `Ollama` · `PentAGI` · `Docker` · `QEMU`

[Architecture and development status](https://github.com/rasasoe/AEGIS-Showcase)

---

### Technical Areas and Notes

**Python · Linux · Docker · FastAPI · AppSec · ROS 2 · Embedded systems**

Engineering notes and technical learning: [Devin's Security Lab](https://rasasoe.tistory.com/).
