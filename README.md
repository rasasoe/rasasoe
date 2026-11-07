<picture>
  <source media="(max-width: 600px)" srcset="assets/profile-banner-mobile.svg">
  <img src="assets/profile-banner.svg" width="100%" alt="Kim Min Gun — Security Engineering, Software Systems, Robotics">
</picture>

<p align="right"><strong>한국어</strong> &nbsp; | &nbsp; <a href="README.en.md">English</a></p>

# 김민건

**Software Engineering · Security · Systems · Robotics**

보안 분석 도구를 개발하고, ROS 2 기반 실물 로봇의 설계와 통합을 수행했습니다.  
기능을 나열하기보다 **직접 구현한 부분, 실행 결과, 검증 범위**를 명확히 기록하려고 합니다.

소프트웨어공학 전공 · 2027년 2월 졸업 예정

[기술 블로그](https://rasasoe.tistory.com/) · [완료된 프로젝트](#완료된-프로젝트) · [진행 중인 프로젝트](#진행-중인-프로젝트)

---

## 완료된 프로젝트

구현과 시연 또는 로컬 테스트까지 마친 범위를 정리했습니다. *완료*는 소개한 기능의 검증 상태를 의미하며, 모든 기능의 상용 수준 검증을 뜻하지 않습니다.

### 01. [VSH — 애플리케이션 보안 분석](https://github.com/rasasoe/VSH)

**정적 탐지 결과를 분석 화면과 공통 보고 형식으로 연결한 AppSec 프로토타입**

<p align="center"><a href="https://github.com/rasasoe/VSH"><img src="assets/vsh-workflow.svg" width="640" alt="VSH: 소스코드 및 의존성 분석에서 탐지, 설명, 결과 출력까지의 흐름"></a></p>

- **담당:** 기존 팀 프로젝트의 [upstream fork](https://github.com/vmfmgl0607/VSH)를 기반으로 Semgrep 실행·설정 연동, Windows 도구 wrapper, Finding v1.0 JSON export 및 테스트를 개인적으로 확장했습니다.
- **검증:** 단위 테스트 81개 통과, 실행 순서 변경 후에도 81개 통과, React 프로덕션 빌드 통과 (2026-09-16).
- **범위:** L2 mock 설명과 선택적 L3 검증을 구분합니다. 실제 취약점 악용 가능성이나 LLM 분석 품질을 입증한 결과는 아닙니다.

`Python` · `FastAPI` · `Semgrep` · `React` · `Electron`

[실행 화면](https://github.com/rasasoe/VSH#실행-화면) · [개인 기여와 커밋](https://github.com/rasasoe/VSH#my-contributions) · [검증과 한계](https://github.com/rasasoe/VSH#검증과-한계)

### 02. [BuddyBot — ROS 2 실내 이동 로봇](https://github.com/rasasoe/BuddyBot)

**3인 팀 프로젝트 · 팀장 / 전체 아키텍처 설계 / 시스템 통합**

<p align="center"><a href="https://github.com/rasasoe/BuddyBot#동작-데모"><img src="assets/buddybot.jpg" width="280" alt="실제로 제작한 3륜 옴니휠 BuddyBot 로봇"></a></p>

- Raspberry Pi 5의 ROS 2 인지·경로 계획과 Raspberry Pi Pico의 모터 제어를 분리하고 UART로 연결했습니다.
- LiDAR 기반 이동, 사용자 추종, 음성 요청을 통합하고 command mux 및 watchdog 안전 제어를 설계했습니다.
- 실제 로봇의 **주행·추종·음성 명령 데모**를 저장소에 공개했습니다.

`ROS 2` · `Python` · `Raspberry Pi` · `RP2040` · `OpenCV`

[동작 영상](https://github.com/rasasoe/BuddyBot#동작-데모) · [시스템 아키텍처](https://github.com/rasasoe/BuddyBot#전체-아키텍처)

### 그 밖의 구현·검증 프로젝트

| 프로젝트 | 구현 및 확인한 범위 |
| --- | --- |
| [DotasPlus](https://github.com/rasasoe/DotasPlus) | 문서 → IOC 추출 → 보호 자산 매칭 → Incident 기록. 로컬 fixture 기반 테스트 9개 통과 |
| [Python ASM Framework](https://github.com/rasasoe/python-asm-framework) | 승인 대상 확인, 공격 표면 결과 정규화 및 Finding export. 네트워크 없는 단위 테스트 6개 통과 |
| [AMR](https://github.com/rasasoe/AMR) · [MRP3MV4](https://github.com/rasasoe/MRP3MV4) | 엔코더 피드백·P제어와 AVR 기반 옴니휠 구동 실험. BuddyBot 이전의 별도 로봇 프로젝트 |

DotasPlus와 ASM의 테스트는 로컬·모의 입력을 대상으로 합니다. 실제 외부 서비스 전체의 종단 간 동작을 검증한 것은 아닙니다.

---

## 진행 중인 프로젝트

### [AEGIS — 자율 보안 AI 플랫폼](https://github.com/rasasoe/AEGIS-Showcase)

**로컬 LLM과 보안 에이전트의 실행 권한을 분리하는 개인 개발 프로젝트**

PentAGI와 Ollama를 연동하고, 분석 대상의 범위 확인 → 승인 → 격리 실행 → 증거 검토를 다루는 통제 계층을 개발하고 있습니다.

- **구현·로컬 검증:** Python Controller, 모델 연결, 승인·범위 검증, 독립 감시기 모의 테스트. 자동 회귀 테스트 305/305 통과 (2026-10-26 기준).
- **진행 중:** 실제 PentAGI Flow 종료 보장 및 자율 취약점 분석의 종단 간 증거 확보.
- **공개 범위:** 설계·검증 현황을 공개하며, 개발 소스는 비공개입니다.

`Python` · `Ollama` · `PentAGI` · `Docker` · `QEMU`

[아키텍처·개발 현황](https://github.com/rasasoe/AEGIS-Showcase)

---

### 기술과 기록

**Python · Linux · Docker · FastAPI · AppSec · ROS 2 · 임베디드 시스템**

개발 과정의 문제 해결과 기술 학습은 [Devin's Security Lab](https://rasasoe.tistory.com/)에 기록합니다.
