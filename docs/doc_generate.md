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

      - name: 🐍 Nastav Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
#          cache: 'pip' # Pridaný riadok na zrýchlenie

      - name: 📦 Inštaluj závislosti a spusti generátor
        run: |
          pip install --upgrade pip
          python scripts/extract_sv_docs.py
          python scripts/generate_index.py

      - name: 🔍 Over obsah vygenerovanej dokumentácie (voliteľné)
        run: ls -lh docs_md

      - name: 🚀 Publikuj do gh-pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs_md   # Priečinok, ktorý sa má publikovať
          user_name: 'github-actions[bot]'
          user_email: 'github-actions[bot]@users.noreply.github.com'
          commit_message: '📝 Aktualizovaná dokumentácia'
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
