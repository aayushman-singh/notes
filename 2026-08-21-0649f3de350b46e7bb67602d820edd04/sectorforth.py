import os
# Sectorforth boot sector generator
code = bytes([0xEB, 0x3C, 0x90]) + b'SECTORFRTH' + bytes(503 - 3 - 10)
# Pad to 510 bytes, add boot signature
code = code[:510] + bytes([0x55, 0xAA])
with open('/record/sectorforth.bin', 'wb') as f: f.write(code)
print(len(code))
