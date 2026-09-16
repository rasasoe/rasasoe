"""Read-only metadata audit; no token or administration access required."""
import json
from urllib.request import Request, urlopen

EXPECTED = {
    'VSH': ['appsec', 'sast', 'semgrep', 'sbom', 'fastapi', 'electron', 'security'],
    'BuddyBot': ['ros2', 'robotics', 'raspberry-pi', 'rp2040', 'opencv', 'autonomous-robot'],
    'DotasPlus': ['threat-intelligence', 'cti', 'ioc', 'fastapi', 'celery', 'cybersecurity'],
    'python-asm-framework': ['attack-surface-management', 'nmap', 'security', 'python', 'asset-discovery'],
}


def check_metadata(data, topics):
    errors = []
    if not (data.get('description') or '').strip():
        errors.append('missing description')
    missing = sorted(set(topics) - set(data.get('topics', [])))
    if missing:
        errors.append('missing topics: ' + ', '.join(missing))
    return errors


if __name__ == '__main__':
    failed = False
    for name, topics in EXPECTED.items():
        try:
            request = Request(f'https://api.github.com/repos/rasasoe/{name}', headers={'User-Agent': 'portfolio-audit', 'Accept': 'application/vnd.github+json'})
            with urlopen(request, timeout=20) as response:
                data = json.load(response)
            errors = check_metadata(data, topics)
        except Exception as error:
            errors = [f'could not verify metadata: {error}']
        print(name + ': ' + ('; '.join(errors) if errors else 'PASS'))
        failed |= bool(errors)
    raise SystemExit(failed)
