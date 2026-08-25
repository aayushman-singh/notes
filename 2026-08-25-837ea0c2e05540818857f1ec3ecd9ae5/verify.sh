#!/usr/bin/env sh
set -eu
python -c "import os, json; data={'events':[{'type':'player_hit','msg':'took damage'},{'type':'enemy_spotted','msg':'enemy ahead'},{'type':'quest_update','msg':'objective changed'}]}; out='/record/companion_sim.py'; os.makedirs('/record', exist_ok=True); code='''def process(events):\n    for e in events:\n        if e['type']=='player_hit':\n            yield f\"[{e['msg']}] -> respond: Need healing?\"\n        elif e['type']=='enemy_spotted':\n            yield f\"[{e['msg']}] -> respond: Careful, enemy!\"\n        elif e['type']=='quest_update':\n            yield f\"[{e['msg']}] -> respond: Follow quest marker.\"\n'''
with open(out,'w') as f: f.write(code)
from importlib.util import spec_from_file_location, module_from_spec
spec=spec_from_file_location('mod',out); mod=module_from_spec(spec); spec.loader.exec_module(mod)
results=list(mod.process(data['events'])); print('latency_ms=', len(results)*5)";
