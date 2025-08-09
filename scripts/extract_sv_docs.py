import re
from pathlib import Path

def parse_sv_file(filepath):
    content = filepath.read_text(encoding='utf-8')

    # 1. Nájdi všetky bloky /** ... */
    doc_blocks = re.findall(r"/\*\*(.*?)\*/", content, re.DOTALL)

    # 2. Nájdi meno modulu
    module_match = re.search(r"\bmodule\s+(\w+)", content)
    module_name = module_match.group(1) if module_match else "unknown_module"

    if not doc_blocks:
        return f"# Modul `{module_name}`\n\n_Žiadna dokumentácia k modulu._\n"

    block = doc_blocks[0].strip()

    brief = ""
    details = ""
    note = ""
    params = []
    code_blocks = []
    example_blocks = []
    inputs = []
    outputs = []
    inouts = []

    lines = [line.strip(" *") for line in block.splitlines()]

    current_tag = None
    current_text = []

    def flush_current():
        nonlocal current_tag, current_text
        text = "\n".join(current_text).strip()
        if current_tag == "brief":
            nonlocal brief
            brief = text
        elif current_tag == "details":
            nonlocal details
            details = text
        elif current_tag == "note":
            nonlocal note
            note = text
        elif current_tag == "param":
            if text:
                parts = text.split(None, 1)
                if len(parts) == 2:
                    params.append((parts[0], parts[1]))
                else:
                    params.append((parts[0], ""))
        elif current_tag == "input":
            if text:
                parts = text.split(None, 1)
                if len(parts) == 2:
                    inputs.append((parts[0], parts[1]))
                else:
                    inputs.append((parts[0], ""))
        elif current_tag == "output":
            if text:
                parts = text.split(None, 1)
                if len(parts) == 2:
                    outputs.append((parts[0], parts[1]))
                else:
                    outputs.append((parts[0], ""))
        elif current_tag == "inout":
            if text:
                parts = text.split(None, 1)
                if len(parts) == 2:
                    inouts.append((parts[0], parts[1]))
                else:
                    inouts.append((parts[0], ""))
        elif current_tag == "code":
            if text:
                code_blocks.append(text)
        elif current_tag == "example":
            if text:
                example_blocks.append(text)
        current_tag = None
        current_text = []

    for line in lines:
        if line.startswith("@brief"):
            flush_current()
            current_tag = "brief"
            current_text.append(line[len("@brief"):].strip())
        elif line.startswith("@details"):
            flush_current()
            current_tag = "details"
            current_text.append(line[len("@details"):].strip())
        elif line.startswith("@note"):
            flush_current()
            current_tag = "note"
            current_text.append(line[len("@note"):].strip())
        elif line.startswith("@param"):
            flush_current()
            current_tag = "param"
            current_text.append(line[len("@param"):].strip())
        elif line.startswith("@input"):
            flush_current()
            current_tag = "input"
            current_text.append(line[len("@input"):].strip())
        elif line.startswith("@output"):
            flush_current()
            current_tag = "output"
            current_text.append(line[len("@output"):].strip())
        elif line.startswith("@inout"):
            flush_current()
            current_tag = "inout"
            current_text.append(line[len("@inout"):].strip())
        elif line.startswith("@code"):
            flush_current()
            current_tag = "code"
        elif line.startswith("@example"):
            flush_current()
            current_tag = "example"
        elif line.startswith("@endcode") or line.startswith("@endexample"):
            flush_current()
        else:
            if current_tag:
                current_text.append(line)
    flush_current()

    md = f"# Modul `{module_name}`\n\n"

    if brief:
        md += f"## Popis\n\n{brief}\n\n"
    if details:
        md += f"{details}\n\n"
    if note:
        md += f"**Poznámka:** {note}\n\n"
    if params:
        md += "## Parametre\n\n"
        for name, desc in params:
            md += f"- `{name}`: {desc}\n"
        md += "\n"

    def gen_table(name, items):
        if not items:
            return ""
        table = f"## {name}\n\n"
        table += "| Názov | Popis |\n"
        table += "|-------|--------|\n"
        for n, d in items:
            table += f"| `{n}` | {d} |\n"
        table += "\n"
        return table

    md += gen_table("Vstupy (input)", inputs)
    md += gen_table("Výstupy (output)", outputs)
    md += gen_table("Obojsmerné (inout)", inouts)

    if code_blocks:
        md += "## Príklady kódu\n\n"
        for code in code_blocks:
            md += "```systemverilog\n" + code + "\n```\n\n"

    if example_blocks:
        md += "## Príklady použitia\n\n"
        for example in example_blocks:
            md += "```systemverilog\n" + example + "\n```\n\n"

    return md

def main():
    src_dir = Path("./src")
    out_dir = Path("./docs_md/modules")
    out_dir.mkdir(parents=True, exist_ok=True)

    sv_files = list(src_dir.rglob("*.sv"))
    print(f"Načítavam {len(sv_files)} .sv súborov...")

    for sv_file in sv_files:
        md = parse_sv_file(sv_file)
        md_file = out_dir / (sv_file.stem + ".md")
        md_file.write_text(md, encoding="utf-8")
        print(f"Vygenerovaný: {md_file}")

if __name__ == "__main__":
    main()
