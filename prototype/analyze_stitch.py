import os
import re
import json

base_dir = r"d:\prototype\stitch_ai_business_copilot_platform"
folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f != ".agents"]

results = []

for f in sorted(folders):
    code_path = os.path.join(base_dir, f, "code.html")
    if not os.path.exists(code_path):
        results.append({
            "folder": f,
            "has_code": False
        })
        continue
    
    with open(code_path, "r", encoding="utf-8", errors="ignore") as file:
        html = file.read()
    
    # Clean HTML tags for quick text extraction
    text = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)
    text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)
    
    # Check layout indicators
    is_mobile_folder_name = "mobile" in f.lower()
    has_bottom_nav = "bottom-nav" in html or "fixed bottom-0" in html or "pb-16" in html or "pb-20" in html
    has_sidebar = "<aside" in html or "w-[260px]" in html or "pl-[260px]" in html
    is_mobile_viewport = "max-w-md" in html or "max-w-sm" in html or "w-[375px]" in html or "w-[390px]" in html
    
    is_mobile = is_mobile_folder_name or (has_bottom_nav and not has_sidebar) or is_mobile_viewport
    
    # Extract headings
    h1 = ""
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL | re.IGNORECASE)
    if h1_match:
        h1 = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        h1 = ' '.join(h1.split())
        
    h2_list = [re.sub(r'<[^>]+>', '', m).strip() for m in re.findall(r'<h2[^>]*>(.*?)</h2>', text, re.DOTALL | re.IGNORECASE)]
    h2_list = [' '.join(x.split()) for x in h2_list if x.strip()][:5]
    
    # Extract buttons
    buttons = [re.sub(r'<[^>]+>', '', m).strip() for m in re.findall(r'<button[^>]*>(.*?)</button>', text, re.DOTALL | re.IGNORECASE)]
    buttons = [' '.join(b.split()) for b in buttons if b.strip() and len(b.strip()) < 40][:8]
    
    # Extract inputs/labels
    labels = [re.sub(r'<[^>]+>', '', m).strip() for m in re.findall(r'<label[^>]*>(.*?)</label>', text, re.DOTALL | re.IGNORECASE)]
    labels = [' '.join(l.split()) for l in labels if l.strip()][:8]

    results.append({
        "folder": f,
        "has_code": True,
        "is_mobile": is_mobile,
        "has_sidebar": has_sidebar,
        "h1": h1,
        "h2_list": h2_list,
        "buttons": buttons,
        "labels": labels,
        "length": len(html)
    })

with open(r"d:\prototype\abc-prototype\prototype\stitch_analysis.json", "w", encoding="utf-8") as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print("Analysis complete. Saved to stitch_analysis.json.")
