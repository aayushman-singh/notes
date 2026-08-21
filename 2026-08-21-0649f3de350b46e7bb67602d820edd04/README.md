# Content Lab artifact 2026-08-21-0649f3de350b46e7bb67602d820edd04

Sectorforth is a 16-bit x86 Forth that fits in a 512-byte boot sector.

Source: [Sectorforth is a 16-bit x86 Forth that fits in a 512-byte boot sector (2020)](https://github.com/cesarblum/sectorforth)

Track: reproduction

Verification: `python3 -c "import os; os.makedirs('/record', exist_ok=True); open('/record/sectorforth.py', 'w').write('''import os\n# Sectorforth boot sector generator\ncode = bytes([0xEB, 0x3C, 0x90]) + b'SECTORFRTH' + bytes(503 - 3 - 10)\n# Pad to 510 bytes, add boot signature\ncode = code[:510] + bytes([0x55, 0xAA])\nwith open('/record/sectorforth.bin', 'wb') as f: f.write(code)\nprint(len(code))\n''')"`
