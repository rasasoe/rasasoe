# AEGIS

> **Project documentation moved:** Please use the [AEGIS-Showcase repository](https://github.com/rasasoe/AEGIS-Showcase) for the current development status, architecture, and roadmap. This page is a historical snapshot.

**Autonomous Security AI Platform** · **In Development**

> An experimental, locally operated cybersecurity AI platform focused on controlled execution, verifiable evidence, and security learning.

AEGIS is an ongoing personal software engineering project. It integrates local language models, a security-agent runtime, and a separately controlled execution layer. Its goal is to make security analysis observable, bounded, and evidence-driven — **not** to claim fully autonomous penetration-testing capability at this stage.

## What I am building

- **Agent orchestration:** a Python controller connecting to PentAGI through REST/GraphQL adapters.
- **Local AI inference:** an Ollama-based LLM pipeline, including GPT-OSS 20B, without depending on paid model APIs.
- **Execution control:** scope validation, short-lived one-time approvals, isolated workers, request budgets, and a fail-closed STOP state.
- **Evidence-oriented reporting:** validation and provenance checks for tool findings, with Korean-language explanations.
- **Security learning workflows:** static analysis, passive HTTP inspection, and planned integration of additional authorized lab exercises.

## Architecture at a glance

```text
User / Security Tutor UI
        |
  AEGIS Controller
        |-- Scope & approval checks
        |-- Evidence / reporting
        |
  PentAGI Adapter
        |
  Isolated agent runtime
        |-- Local Ollama model relay
        |-- Controlled security tools
        |-- Lifecycle monitor (validation in progress)
```

The external PentAGI engine is an upstream open-source dependency. AEGIS's own work focuses on orchestration, policy enforcement, integration, evidence, and learning-oriented UX; it is **not** presented as an original implementation of PentAGI.

## Development status

| Area | Status |
| --- | --- |
| Controller and approval / scope controls | Implemented; local tests passing |
| Ollama ↔ relay ↔ PentAGI model response | Verified in a local integration check |
| PentAGI native mock-tool compatibility | 9/9 local checks passed |
| Local regression suite | 305/305 passed at the latest recorded checkpoint |
| Independent server-side Flow lifecycle monitor | Implemented; simulation tests passed |
| Native PentAGI Flow termination and deployed monitor | **Pending live verification** |
| Autonomous vulnerability discovery with retained HTTP evidence | **Not yet demonstrated** |

**The passing tests are development evidence, not a claim that real-world penetration testing is operational.** The first end-to-end evaluation is planned for an isolated, explicitly authorized OWASP Juice Shop lab.

## Technologies

`Python` · `Ollama` · `GPT-OSS` · `PentAGI` · `Docker` · `QEMU` · `Linux` · `SQLite` · `REST/GraphQL` · `Semgrep` · `Bandit`

## Availability & disclosure

The development code and environment-specific configuration are **private** while the project is being validated. This public page contains high-level technical documentation only: no credentials, network topology, internal addresses, raw logs, or unrestricted execution instructions.

A sanitized architecture illustration, reproducible demonstrations, and non-sensitive results will be added when verified. No public runnable release is available yet.

**Status updated:** October 2026.
