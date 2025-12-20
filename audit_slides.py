import re

try:
    with open(r"c:\Users\mahim\OneDrive\Desktop\New folder\B2B.html", 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all slide divs
    # We look for <div class="slide or <div class="slide active
    # Then find the first h1 or h2 class="section-title"

    # Split by slide div
    slides = re.split(r'<div class="slide(?: active)?">', content)
    slides = slides[1:] # First chunk is header

    with open("slides_list.txt", "w", encoding="utf-8") as out:
        out.write(f"Total slices found: {len(slides)}\n")
        for i, slide_html in enumerate(slides):
            # Extract title
            title_match = re.search(r'<(?:h1|h2) class="section-title"[^>]*>(.*?)</(?:h1|h2)>', slide_html, re.DOTALL)
            if title_match:
                title = title_match.group(1).replace('<br>', ' ').strip()
                out.write(f"Slide {i}: {title}\n")
            else:
                out.write(f"Slide {i}: [No Title Found]\n")
    print("Done writing to slides_list.txt")

except Exception as e:
    print(f"Error: {e}")
