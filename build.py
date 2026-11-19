"""Build a public, read-only JSON index from teacher-edited YAML files."""
import json
from pathlib import Path
import yaml
ROOT = Path(__file__).parent
THEMES = ['身份认同','体验','人类创造力','社会组织','共享地球']
items = []
for path in sorted((ROOT/'content/tasks').glob('*.yml')):
    data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    if not isinstance(data, dict) or not data.get('published', False):
        continue
    if data.get('theme') not in THEMES or not data.get('title'):
        raise ValueError(f'Invalid theme/title: {path}')
    # Public resources only; no student information is stored.
    items.append({k:data.get(k) for k in ('title','theme','image','image_alt','summary','questions','vocabulary')})
(ROOT/'data.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Published {len(items)} task(s)')
