<picture>
  <source media="(max-width: 600px)" srcset="assets/profile-banner-mobile.svg">
  <img src="assets/profile-banner.svg" width="100%" alt="Kim Min Gun — Security Engineering, Software Systems, Robotics">
</picture>

<p align="right"><strong>한국어</strong> &nbsp; | &nbsp; <a href="README.en.md">English</a></p>

# 김민건

**Software Engineering · Security · Systems · Robotics**

보안 분석 도구를 개발하고, ROS 2 기반 실물 로봇의 설계와 통합을 수행했습니다.  
프로젝트를 시작한 **문제와 개발 목표**, 이를 위해 선택한 **기능과 구조**, 그리고 **실제로 구현·확인한 결과**를 구분해 기록합니다.

기존 상용 보안 제품의 기능을 대체했다고 주장하지 않습니다. 검증 자동화, 결과의 추적 가능성, 시스템 통합과 장애 대응을 직접 구현한 범위로 설명합니다.

소프트웨어공학 전공 · 2027년 2월 졸업 예정

[기술 블로그](https://rasasoe.tistory.com/) · [완료된 프로젝트](#완료된-프로젝트) · [진행 중인 프로젝트](#진행-중인-프로젝트)

---

## 완료된 프로젝트

**완료 시점이 최근인 프로젝트부터** 배치했습니다. 프로젝트에서 구현한 범위와 검증하지 못한 기능은 구분해 기록합니다.

**기간 기준:** 완료일과 나중의 README·테스트 보완 시점은 별개입니다. 시작일이 불분명한 경우 임의로 기입하지 않았습니다.

### 01. [BuddyBot — 가정용 AI 서빙 로봇 프로토타입](https://github.com/rasasoe/BuddyBot)

**개발 기간:** 2025.03–2026.06 · **완료 시점:** 2026.06  
**3인 팀 프로젝트 · 팀장 / 전체 아키텍처 설계 / 시스템 통합**

**기획 목표:** 음성 명령을 이해하고 집 안에서 이동하며 사람과 상호작용하는 **가정용 AI 서빙 로봇을 직접 만들어보자**는 아이디어에서 시작했습니다. 물품 운반·전달까지 완성된 제품이 아니라, 그 목표에 필요한 이동·인지·상호작용 기능을 구현한 프로토타입입니다.

**필요 기능 선정:** LiDAR 기반 실내 환경 인식·장애물 회피, 카메라 기반 객체·사람 인식, 마이크·STT 음성 명령, 목적지 이동·사용자 추종을 핵심 기능으로 정했습니다.

<p align="center"><a href="https://github.com/rasasoe/BuddyBot#동작-데모"><img src="assets/buddybot.jpg" width="280" alt="실제로 제작한 3륜 옴니휠 BuddyBot 로봇"></a></p>

- **설계·통합:** Raspberry Pi 5의 ROS 2 인지·주행 기능과 Pico의 모터 제어를 UART로 연결하고, command mux·watchdog 기반 제어·정지 경로를 구성했습니다.
- **구현·시연:** 실제 로봇으로 체크포인트 이동, 장애물 회피, 사용자 추종, 음성 명령, 비상정지를 시연했습니다.
- **구현 범위:** 실내 자율이동·상호작용 기능을 확인했으며, 물품 서빙의 전 과정이나 상용 수준의 안전성을 검증한 것은 아닙니다.

`ROS 2` · `Python` · `Raspberry Pi` · `RP2040` · `OpenCV`

[동작 영상](https://github.com/rasasoe/BuddyBot#동작-데모) · [시스템 아키텍처](https://github.com/rasasoe/BuddyBot#전체-아키텍처)

### 02. [VSH — 바이브 코딩 실시간 보안 도우미](https://github.com/rasasoe/VSH)

**프로젝트 개발 완료:** 2026.02 · **이후 개인 보완·재검증:** 2026.09 (개발 최초 시작일 미확인)

**기획 배경:** 바이브 코딩으로 코드를 빠르게 생성하면서 생기는 보안 위험을, **코드 작성·저장 단계에서 탐지하고 LLM으로 설명·수정 제안**하면 어떨까? 이 아이디어에서 시작했습니다. 팀 최종 제출본은 MCP 서버·파일 감시 데모를 포함하고, 개인 포크는 데스크톱 UI·분석 결과 형식과 검증을 확장했습니다.

<p align="center"><a href="https://github.com/rasasoe/VSH"><picture><source media="(max-width: 600px)" srcset="assets/vsh-workflow-mobile.svg"><img src="assets/vsh-workflow.svg" width="100%" alt="VSH L1 정적 탐지, L2 LLM 설명, L3 선택적 PoC 생성 및 검증 흐름"></picture></a></p>

- **팀 결과 / 개인 기여:** [팀 최종 제출본(MVP-final)](https://github.com/vmfmgl0607/VSH/tree/MVP-final)의 FastMCP·변경 감시 기능과 별개로, 내 포크에서는 Semgrep·도구 설정, Windows wrapper, Finding v1.0 export, 테스트 등을 보완했습니다.
- **검증 결과:** 단위 테스트 81개 및 역순 실행 81개 통과, React 프로덕션 빌드 통과 (2026-09-16). 로컬 취약 코드 fixture의 분석 UI도 실행했습니다.
- **검증 범위:** 팀 파일 감시 데모는 지정된 샘플 파일 중심이며, `apply_fix`는 실제 파일을 자동 수정하지 않습니다. 포크의 L2 공개 데모는 mock, L3 PoC 종단 간 검증은 미완료입니다.

`Python` · `FastAPI` · `Semgrep` · `React` · `Electron`

[실행 화면](https://github.com/rasasoe/VSH#실행-화면) · [개인 기여와 커밋](https://github.com/rasasoe/VSH#my-contributions) · [검증과 한계](https://github.com/rasasoe/VSH#검증과-한계)

### 기타 프로젝트

- **[DotasPlus](https://github.com/rasasoe/DotasPlus)** — IOC 수집·자산 매칭·Incident 기록. 2026.09 로컬 테스트 9개 통과.
- **[Python ASM Framework](https://github.com/rasasoe/python-asm-framework)** — 허가 대상 점검·노출 결과 정규화. 2026.09 오프라인 테스트 6개 통과.
- **[AMR](https://github.com/rasasoe/AMR)** · **[MRP3MV4](https://github.com/rasasoe/MRP3MV4)** — 엔코더 제어·3륜 옴니휠 구동·센서 실험.

위 날짜는 개발 완료일이 아닌 **확인된 테스트 시점**입니다. 상세 개발 기록과 한계는 각 저장소에서 볼 수 있습니다.

---

## 진행 중인 프로젝트

### [AEGIS — 자율 보안 AI 플랫폼](https://github.com/rasasoe/AEGIS-Showcase)

**진행 중 · 공개 개발·검증 기록:** 2026.10–현재 (실제 최초 착수일과 구분)  
**개인 프로젝트 · 로컬 LLM과 보안 에이전트의 실행 권한 분리**

**검증 목표:** AI가 판단을 내리더라도 승인되지 않은 대상이나 도구를 실행하지 못하는지, 중단 명령이 **실제 실행 중인 작업까지 종료**하는지, 보고서의 판단이 **확인 가능한 도구 증거와 연결**되는지 검증하려는 프로젝트입니다.

PentAGI와 Ollama를 연동하고, 범위 확인 → 승인 → 격리 실행 → 증거 검토를 위한 통제 계층을 개발하고 있습니다.

- **확인된 결과:** Python Controller, 모델 연결, 승인·범위 검증, 독립 감시기 모의 테스트. 2026-10-26 기록 기준 자동 회귀 테스트 305/305 통과(실제 취약점 발견 성공률이 아닌 로컬 테스트 결과).
- **아직 검증할 것:** 실제 PentAGI 작업 종료 보장, 허가된 실습 환경에서의 자율 분석·HTTP 증거 수집 및 검증 가능한 보고서 생성.
- **공개 범위:** 설계·검증 현황을 공개하며, 개발 소스는 비공개입니다.

`Python` · `Ollama` · `PentAGI` · `Docker` · `QEMU`

[아키텍처·개발 현황](https://github.com/rasasoe/AEGIS-Showcase)

---

### 기술과 기록

**Python · Linux · Docker · FastAPI · AppSec · ROS 2 · 임베디드 시스템**

개발 과정의 문제 해결과 기술 학습은 [Devin's Security Lab](https://rasasoe.tistory.com/)에 기록합니다.
