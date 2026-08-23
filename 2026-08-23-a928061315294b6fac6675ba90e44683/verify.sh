#!/usr/bin/env sh
set -eu
python -c "import os; p='/record/gloves.py'; os.makedirs('/record', exist_ok=True); open(p,'w').write('print(\"Electric shock gloves in use by Bellevue and Omaha police\")')"
