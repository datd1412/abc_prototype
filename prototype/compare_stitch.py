import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\prototype\abc-prototype\prototype\stitch_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

base_dir = r"d:\prototype\stitch_ai_business_copilot_platform"

groups = {}
non_prefixed = []

for item in data:
    name = item["folder"]
    match = re.match(r'^(bo_\d+|se_\d+|sa_\d+)', name)
    if match:
        prefix = match.group(1)
        if prefix not in groups:
            groups[prefix] = []
        groups[prefix].append(item)
    else:
        non_prefixed.append(item)

print("=== 1. PREFIXED GROUPS ANALYSIS ===")
for prefix, items in sorted(groups.items()):
    print(f"\nGroup: {prefix} ({len(items)} folders)")
    for it in items:
        f = it["folder"]
        is_mob = it["is_mobile"]
        h1 = it["h1"]
        print(f"  - [{'MOBILE ' if is_mob else 'DESKTOP'}] {f}")
        print(f"    H1: {h1}")
        print(f"    Headings: {', '.join(it['h2_list'][:3])}")
        print(f"    Buttons: {', '.join(it['buttons'][:5])}")
        print(f"    Labels: {', '.join(it['labels'][:5])}")

print("\n=== 2. NON-PREFIXED FOLDERS ANALYSIS ===")
print(f"Total non-prefixed: {len(non_prefixed)}")
for it in non_prefixed:
    f = it["folder"]
    h1 = it["h1"]
    print(f"\nFolder: {f}")
    print(f"  H1: {h1}")
    print(f"  Headings: {', '.join(it['h2_list'][:3])}")
    print(f"  Buttons: {', '.join(it['buttons'][:5])}")
    print(f"  Labels: {', '.join(it['labels'][:5])}")
