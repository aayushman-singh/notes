from pathlib import Path
title = "Fermat's Last Theorem in Lean 4"
summary = "Fermat's Last Theorem in Lean 4"
implementation = "def terms(text):\n    return {word.strip('.,:;!?()[]').lower() for word in text.split() if len(word) > 3}\n"
Path('/record/source_measure.py').write_text(implementation, encoding='utf-8')
scope = {}
exec(implementation, scope)
title_terms = scope['terms'](title)
summary_terms = scope['terms'](summary)
overlap = len(title_terms & summary_terms)
print(f'title_terms={len(title_terms)} summary_terms={len(summary_terms)} overlap={overlap}')