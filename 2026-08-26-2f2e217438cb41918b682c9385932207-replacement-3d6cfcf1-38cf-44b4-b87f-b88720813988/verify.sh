#!/usr/bin/env sh
set -eu
python -c 'import os

def write_file(path, content):
    with open(path, '"'"'w'"'"') as f:
        f.write(content)

# Simulate the core functionality: convert a list of text lines to Markdown
# Based on the described feature: screen memory without screenshots, just text to Markdown
# We implement a minimal version that takes raw text and formats it as Markdown headings and lists

def to_markdown(text):
    lines = text.strip().split('"'"'\n'"'"')
    md_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('"'"'#'"'"'):
            md_lines.append(line)
        elif line.startswith('"'"'- '"'"'):
            md_lines.append(line)
        else:
            md_lines.append('"'"'- '"'"' + line)
    return '"'"'\n'"'"'.join(md_lines)

# Test cases: explicit input cases
input1 = "Title\nSubtitle\n- item1\n- item2"
expected1 = "- Title\n- Subtitle\n- item1\n- item2"
input2 = "# Heading\nSome text"
expected2 = "# Heading\n- Some text"

result1 = to_markdown(input1)
result2 = to_markdown(input2)

# Verify results
ok1 = result1 == expected1
ok2 = result2 == expected2

# Write implementation file
impl_code = """
def to_markdown(text):
    lines = text.strip().split('"'"'\n'"'"')
    md_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('"'"'#'"'"') or line.startswith('"'"'- '"'"'):
            md_lines.append(line)
        else:
            md_lines.append('"'"'- '"'"' + line)
    return '"'"'\n'"'"'.join(md_lines)
"""
write_file('"'"'/record/ambient_context.py'"'"', impl_code)

# Print one concise measured finding
if ok1 and ok2:
    print("Text-to-Markdown conversion matches expected output for both test cases.")
else:
    print("Mismatch: conversion does not match expected output.")

exit(0)'
