
def to_markdown(text):
    lines = text.strip().split('
')
    md_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('#') or line.startswith('- '):
            md_lines.append(line)
        else:
            md_lines.append('- ' + line)
    return '
'.join(md_lines)
