import os
import re
import subprocess

# --- Dynamické zistenie URL repozitára a vetvy ---
def get_git_remote_url():
    try:
        url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            encoding='utf-8'
        ).strip()
        # Konverzia SSH URL na HTTPS
        if url.startswith("git@github.com:"):
            url = url.replace("git@github.com:", "https://github.com/")
        if url.endswith(".git"):
            url = url[:-4]
        return url
    except subprocess.CalledProcessError:
        return None

def get_git_branch():
    try:
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            encoding='utf-8'
        ).strip()
        return branch
    except subprocess.CalledProcessError:
        return "main"

GITHUB_REPO_URL = get_git_remote_url() or "https://github.com/unknown/repo"
BRANCH = get_git_branch() or "main"

# --- Cesty ---
modules_dir = 'docs_md/modules'
index_file = 'docs_md/index.md'
src_dir = 'src'

# --- Načítanie a zoradenie markdown súborov ---
md_files = [f for f in os.listdir(modules_dir) if f.endswith('.md')]
md_files.sort()

def extract_description(md_path):
    """Vyhľadá v markdown súbore text za ## Popis (prvý odstavec)."""
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    m = re.search(r"## Popis\s*(.*?)\n\s*\n", content, re.DOTALL)
    if m:
        desc = m.group(1).strip().replace('\n', ' ')
        if len(desc) > 120:
            desc = desc[:117] + "..."
        return desc
    return "-"

def find_source_file(module_name):
    """Nájde zdrojový súbor podľa mena modulu (.sv v src_dir)."""
    candidate = os.path.join(src_dir, module_name + '.sv')
    if os.path.isfile(candidate):
        return candidate
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file == module_name + '.sv':
                return os.path.relpath(os.path.join(root, file))
    return None

def generate_source_url(src_file):
    """Vytvorí URL na súbor v GitHub repozitári na konkrétnej vetve."""
    if not src_file:
        return "-"
    # Upravi cestu na URL (pre github musí byť s lomítkami)
    url_path = src_file.replace(os.sep, '/')
    return f"{GITHUB_REPO_URL}/blob/{BRANCH}/{url_path}"

with open(index_file, 'w', encoding='utf-8') as f:
    f.write("# Dokumentácia modulov\n\n## 🔧 Zoznam\n\n")
    f.write("| Názov modulu | Popis | Zdrojový súbor |\n")
    f.write("|--------------|--------|----------------|\n")

    for md in md_files:
        module_name = os.path.splitext(md)[0]
        md_path = os.path.join(modules_dir, md)
        desc = extract_description(md_path)
        src_file = find_source_file(module_name)

        md_link = f"[{module_name}](modules/{md})"
        src_link = generate_source_url(src_file) if src_file else "-"

        # V tabuľke použijeme Markdown link
        if src_link != "-":
            src_link_md = f"[{os.path.basename(src_file)}]({src_link})"
        else:
            src_link_md = "-"

        f.write(f"| {md_link} | {desc} | {src_link_md} |\n")

print(f"📄 Aktualizovaný index: {index_file}")
