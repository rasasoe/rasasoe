# Repository About — manual settings still required

README updates do not change GitHub repository metadata. Open each repository's **About → gear icon**, enter the description and topics below, then save. This change requires the owner's settings access and is not performed by the current GitHub connector.

| Repository | Description | Topics |
| --- | --- | --- |
| VSH | Explainable AppSec prototype combining SAST, SBOM and LLM-assisted reasoning | appsec, sast, semgrep, sbom, fastapi, electron, security |
| BuddyBot | ROS 2 indoor autonomous robot with distributed Pi 5–RP2040 control | ros2, robotics, raspberry-pi, rp2040, opencv, autonomous-robot |
| DotasPlus | Defensive CTI pipeline connecting external IOCs to protected assets | threat-intelligence, cti, ioc, fastapi, celery, cybersecurity |
| python-asm-framework | Attack Surface Management prototype for authorized asset discovery | attack-surface-management, nmap, security, python, asset-discovery |

After saving, check the repository list and profile cards, not only README. Suggested pin order: **VSH → BuddyBot → python-asm-framework → DotasPlus**. The user has already pinned projects; the order must be checked in GitHub's profile UI, not inferred from README order.

## Validation boundaries

`python scripts/check_portfolio.py` checks local README paths, anchors and referenced image decoding, including every GIF frame and SVG XML parsing. GitHub Actions runs it on push and pull requests. It does not prove remote links, video playback, application correctness or About metadata.

`python scripts/check_about.py` separately reads public repository metadata and exits nonzero if a description is missing or expected topics are absent. It never changes repository settings. Network/API failures are errors, not success.

Content review checklist: own contribution with commit/PR evidence; reproducible demonstration with mock/live distinction; tested command, date and scope; unresolved limitations; planned work not presented as implemented.
