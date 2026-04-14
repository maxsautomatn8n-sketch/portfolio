#!/usr/bin/env python3
"""
Extracts the base64 logo from the original email HTML and injects it
into the upgraded template, replacing the placeholder URL.

Usage:
  1. Save your original email HTML as:
       /home/user/portfolio/email/original.html
  2. Run:
       python3 /home/user/portfolio/email/inject_logo.py
"""
import re, sys

ORIGINAL = '/home/user/portfolio/email/original.html'
TEMPLATE = '/home/user/portfolio/email/simulation-credit.html'
PLACEHOLDER = 'https://www.credit-on-line.com/assets/img/logo-col.png'

with open(ORIGINAL, 'r', encoding='utf-8') as f:
    source = f.read()

match = re.search(r'(data:image/[^;]+;base64,[A-Za-z0-9+/=\r\n]+?)(?=")', source)
if not match:
    print("ERROR: No base64 image found in original HTML.", file=sys.stderr)
    sys.exit(1)

data_uri = match.group(1).replace('\r','').replace('\n','')
print(f"Found base64 image ({len(data_uri):,} chars), injecting into template...")

with open(TEMPLATE, 'r', encoding='utf-8') as f:
    template = f.read()

if PLACEHOLDER not in template:
    print(f"ERROR: Placeholder URL not found in template:\n  {PLACEHOLDER}", file=sys.stderr)
    sys.exit(1)

updated = template.replace(f'src="{PLACEHOLDER}"', f'src="{data_uri}"')

with open(TEMPLATE, 'w', encoding='utf-8') as f:
    f.write(updated)

print(f"Done. Logo embedded in:\n  {TEMPLATE}")
