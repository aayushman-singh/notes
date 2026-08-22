#!/usr/bin/env sh
set -eu
python -c "import os; os.makedirs('/record', exist_ok=True); open('/record/test_ox_alpha.py','w').write('import urllib.request\nreq=urllib.request.Request(\"https://openrouter.ai/stealth/ox-alpha\", headers={\"User-Agent\":\"Mozilla/5.0\"})\ntry:\n    r=urllib.request.urlopen(req, timeout=10)\n    print(r.status)\nexcept Exception as e:\n    print(type(e).__name__, str(e))\n')"
