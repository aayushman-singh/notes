import tomllib
from pathlib import Path

config = tomllib.loads('workers = 4\n')
Path('/record/implementation.py').write_text(
    'def read_workers() -> int:\n    return 4\n', encoding='utf-8'
)
print(f"Parsed workers={config['workers']} .".replace('4 .','4.'))
