from pathlib import Path
title = "r/LocalLLM: Running Gemma 3 1B on an Android phone as the brain of an autonomous agent \u2014 it handles ~60-70% of requests"
summary = "r/LocalLLM: Running Gemma 3 1B on an Android phone as the brain of an autonomous agent \u2014 it handles ~60-70% of requests\n  with zero network\nI built an Android agent that uses a Gemma 3 1B model running locally on the phone as its primary brain. No API calls\n\n  for simple tasks \u2014 it works in airplane mode.\n\n\n\n  The agent has 30 tools (flashlight, clipboard, SMS, app launch, web"
implementation = "def terms(text):\n    return {word.strip('.,:;!?()[]').lower() for word in text.split() if len(word) > 3}\n"
Path('/record/source_measure.py').write_text(implementation, encoding='utf-8')
scope = {}
exec(implementation, scope)
title_terms = scope['terms'](title)
summary_terms = scope['terms'](summary)
overlap = len(title_terms & summary_terms)
print(f'title_terms={len(title_terms)} summary_terms={len(summary_terms)} overlap={overlap}')