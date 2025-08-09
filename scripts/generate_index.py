import os
import re

modules_dir = 'docs_md/modules'
index_file = 'docs_md/index.md'
src_dir = 'src'  # cesta ku zdrojovým .sv súborom

md_files = [f for f in os.listdir(modules_dir) if f.endswith('.md')]
md_files.sort()

def extract_description(md_path):
    """Vyhľadá v markdown súbore text za ## Popis (prvý odstavec)."""
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    # Nájde sekciu ## Popis
    m = re.search(r"## Popis\s*(.*?)\n\s*\n", content, re.DOTALL)
    if m:
        # Odstráni nadbytočné medzery a nové riadky
        desc = m.group(1).strip().replace('\n', ' ')
        # Skráti na 120 znakov, ak je príliš dlhý
        if len(desc) > 120:
            desc = desc[:117] + "..."
        return desc
    return "-"

def find_source_file(module_name):
    """Nájde zdrojový súbor podľa mena modulu (.sv v src_dir)."""
    candidate = os.path.join(src_dir, module_name + '.sv')
    if os.path.isfile(candidate):
        return candidate
    # Ak sa nenájde, hľadáme kdekoľvek v src_dir
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file == module_name + '.sv':
                return os.path.relpath(os.path.join(root, file))
    return "-"

with open(index_file, 'w', encoding='utf-8') as f:
    f.write("# Dokumentácia modulov\n\n## 🔧 Zoznam\n\n")

    # Hlavička tabuľky
    f.write("| Názov modulu | Popis | Zdrojový súbor |\n")
    f.write("|--------------|--------|----------------|\n")

    for md in md_files:
        module_name = os.path.splitext(md)[0]
        md_path = os.path.join(modules_dir, md)
        desc = extract_description(md_path)
        src_file = find_source_file(module_name)

        # Odkaz na md dokumentáciu (relatívny)
        md_link = f"[{module_name}](modules/{md})"

        # Odkaz na zdrojový súbor (relatívny)
        if src_file != "-":
            src_link = f"[{os.path.basename(src_file)}](../{os.path.relpath(src_file)})"
        else:
            src_link = "-"

        f.write(f"| {md_link} | {desc} | {src_link} |\n")

print(f"📄 Aktualizovaný index: {index_file}")
