Super, tu je návrh GitHub Actions workflow, ktorý vygeneruje dokumentáciu a **commitne a pushne ju do samostatnej vetvy `gh-pages`**, čím sa vyhneš rebasovaniu alebo konfliktom v `main`:

---

### Princíp:

* `main` branch zostáva čistý bez generovaných súborov.
* Dokumentácia sa generuje a commitne do vetvy `gh-pages`.
* Vetvu `gh-pages` môžeš nastaviť ako GitHub Pages zdroj (Settings → Pages).
* Pri ďalšom pushi do `main` sa dokumentácia prepíše v `gh-pages`.

---

```yaml
name: Generuj a publikuj dokumentáciu

permissions:
  contents: write
  pages: write
  id-token: write

on:
  push:
    paths:
      - "src/**/*.sv"
      - ".github/workflows/gen-docs.yml"
  workflow_dispatch:

jobs:
  generate-docs:
    runs-on: ubuntu-latest

    steps:
      - name: 🛎️ Checkout kódu
        uses: actions/checkout@v4
        with:
          fetch-depth: 0   # potrebné pre push a prečítanie celej histórie

      - name: 🐍 Nastav Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: 📦 Inštaluj závislosti a spusti generátor
        run: |
          pip install --upgrade pip
          python scripts/extract_sv_docs.py
          python scripts/generate_index.py

      - name: 🔍 Over obsah vygenerovanej dokumentácie
        run: |
          ls -lh docs_md || echo "docs_md priečinok neexistuje"

      - name: 📝 Inicializuj samostatnú vetvu gh-pages a commitni dokumentáciu
        run: |
          # Vytvor lokálnu vetvu gh-pages alebo ju prepni
          git fetch origin gh-pages || echo "Vetva gh-pages neexistuje, vytvorí sa nová"
          git checkout -B gh-pages origin/gh-pages || git checkout --orphan gh-pages

          # Vymaž starý obsah, nech zostane len dokumentácia
          git rm -rf . > /dev/null 2>&1 || true

          # Skopíruj dokumentáciu z docs_md
          cp -r docs_md/* .

          # Pridaj všetko do git indexu
          git add .

          # Commitni len ak sú zmeny
          if ! git diff --cached --quiet; then
            git config user.name "github-actions"
            git config user.email "github-actions@github.com"
            git commit -m "📝 Aktualizovaná dokumentácia z .sv súborov"
            git push origin gh-pages --force
            echo "✅ Dokumentácia publikovaná do vetvy gh-pages"
          else
            echo "⚠️ Žiadne zmeny v dokumentácii"
          fi

          # Prepni sa späť na main (alebo pôvodnú vetvu)
          git checkout main
```

---

### Ako to funguje?

* Po vygenerovaní sa workflow prepne na vetvu `gh-pages`.
* Odstráni všetky predchádzajúce súbory (vymaže starú dokumentáciu).
* Skopíruje novú dokumentáciu z `docs_md` do koreňového adresára vetvy `gh-pages`.
* Commitne a pushne zmeny (ak nejaké sú).
* Nakoniec sa prepne späť na `main`.

---

### Nastavenie GitHub Pages

* Vo svojom repozitári na GitHub → **Settings → Pages**.
* Ako zdroj vyber `gh-pages` vetvu a root adresár `/`.
* Po zapnutí bude dokumentácia dostupná online cez GitHub Pages.

---

### Výhody:

* `main` je čistý, nič sa do neho necommitne automaticky.
* Dokumentácia je online bez potreby ručného pushovania.
* Žiadne konflikty s generovanou dokumentáciou pri práci na kóde.

---

Ak chceš, môžem pomôcť aj s úpravou tvojich skriptov na správne uloženie v `docs_md` alebo ďalšími detailami.

Čo povieš?
