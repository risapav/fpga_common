Tu je rozšírená verzia README.md pre `fpga_common` s pridanou sekciou **FAQ a tipy pre submoduly**, ktorá rieši najčastejšie problémy a dáva odporúčania pre CI/CD:

---

# fpga\_common

**Zdieľaná knižnica modulov pre FPGA projekty**

`fpga_common` obsahuje opakovane použiteľné moduly, dokumentáciu a nástroje pre prácu s FPGA projektmi.

---

## ✅ Odporúčané použitie: Git submoduly

Použitie submodulu umožňuje, aby projekty používali **konkrétnu verziu knižnice**, pričom dokumentácia a moduly sú spravované samostatne.

---

### 💡 Kedy použiť:

* Chceš mať knižnicu a dokumentáciu ako **samostatný repozitár**.
* Chceš, aby projekty vždy používali **konkrétnu verziu** knižnice.
* Chceš jednoducho aktualizovať knižnicu vo viacerých projektoch.

---

### 🔧 Krok 1: Vytvor samostatný repozitár

Vytvor nový repozitár, napr.:

```text
risapav/fpga_common
```

Struktúra:

```
fpga_common/
├── scs/        # HDL moduly
└── docs_md/    # Automaticky generovaná dokumentácia
```

---

### 🔧 Krok 2: Pridaj ho ako submodul do projektu

V koreňovom adresári projektu:

```bash
git submodule add https://github.com/risapav/fpga_common common
# alebo SSH
git submodule add git@github.com:risapav/fpga_common.git common
```

Výsledná štruktúra projektu:

```
fpga_ep4ce55f23/
├── common/
│   ├── scs/
│   └── docs_md/
├── src/
├── ...
```

Prístup k súborom: `common/scs/...`, `common/docs_md/...`.

---

### 🔧 Krok 3: Commitni a pushni submodul

```bash
git add .gitmodules common/
git commit -m "Pridaný submodul fpga_common"
git push
```

---

### 🔧 Krok 4: Práca so submodulom

#### Klonovanie projektu so submodulom:

```bash
git clone --recurse-submodules https://github.com/risapav/fpga_ep4ce55f23
# alebo po klasickom clone:
git submodule sync
git submodule update --init --recursive
# potom pri chybe
cd common
git checkout main      # alebo commit, ktorý existuje
git pull origin main
```

#### Aktualizácia submodulu:

1. Prejdite do adresára submodulu:

```bash
cd common
git pull origin main  # alebo iný branch
cd ..
```

2. Commitnite zmenu v submodule:

```bash
git add common
git commit -m "Update common submodule to latest"
git push
```

> Tip: Pre pohodlnejšiu kontrolu použite:

```bash
git config status.showUntrackedFiles no
```

---

### 🔧 Krok 5: Riešenie konfliktov a lokálnych zmien

Ak Git hlási chybu, napr.:

```
error: Your local changes to the following files would be overwritten by merge:
	src/picture/picture_gen.sv
Please commit your changes or stash them before you merge.
Aborting
```

#### Možnosti:

1️⃣ **Zachovať lokálne zmeny:**

```bash
git add src/picture/picture_gen.sv
git commit -m "Moje zmeny"
git pull -f origin main
```

Alebo:

```bash
git stash
git pull -f origin main
git stash pop
```

> Poznámka: Konflikty po `stash pop` rieš manuálne.

2️⃣ **Nechceš lokálne zmeny – zahodíš ich:**

```bash
git checkout -- src/picture/picture_gen.sv
git pull -f origin main
```

---

## 📝 Automatizovaná dokumentácia

* **extract\_sv\_docs.py** – Parsuje SystemVerilog súbory a generuje Markdown dokumentáciu (`docs_md/modules/`).
* **generate\_index.py** – Vytvára `index.md` so zoznamom modulov a odkazmi na zdrojové súbory.

### Použitie:

```bash
python scripts/extract_sv_docs.py
python scripts/generate_index.py
```

* Skripty podporujú **viacero zdrojových adresárov** vrátane submodulov.
* Súbory s rovnakým názvom z rôznych adresárov sa nezmiešajú – používajú unikátne cesty (`subdir_module.sv.md`).

---

## 📂 Štruktúra projektu

```
fpga_common/
├── scs/            # HDL moduly (SystemVerilog)
├── docs_md/        # Vygenerované Markdown súbory
├── scripts/
│   ├── extract_sv_docs.py
│   └── generate_index.py
└── README.md       # Tento súbor
```

---

## 🔗 CI/CD Workflow

* Automatické generovanie dokumentácie pri pushi:

```yaml
# .github/workflows/gen-docs.yml
python scripts/extract_sv_docs.py
python scripts/generate_index.py
```

* Publikovaná dokumentácia sa nachádza vo `docs_md/` a môže byť deployovaná do GitHub Pages.

---

## ❓ FAQ a tipy pre submoduly

### 1️⃣ Viacero súborov s rovnakým názvom

* Skripty `extract_sv_docs.py` a `generate_index.py` používajú **unikátne cesty**, aby sa predišlo prepísaniu dokumentácie pre súbory s rovnakým názvom v rôznych adresároch.
* Odporúča sa **nepoužívať duplicitné názvy modulov**, alebo použiť prefix/namespace.

---

### 2️⃣ Problémy pri clone submodulu

* Ak sa submodul nedá naklonovať:

```text
fatal: Fetched in submodule path 'common', but it did not contain <commit_hash>
```

* Riešenie:

  1. Skontroluj, či commit existuje v repozitári submodulu.
  2. Uisti sa, že používaš správnu vetvu (`main` alebo `master`).
  3. Prípadne resetni submodul:

```bash
git submodule sync
git submodule update --init --recursive --force
```

---

### 3️⃣ Lokálne zmeny v submodule

* Pri práci so submodulom sa **každý submodul správa ako samostatný repozitár**.
* Ak máš lokálne zmeny:

```bash
cd common
git status
git add ...
git commit -m "Moje zmeny"
git push
```

* Potom v hlavnom projekte commitni aktualizovaný pointer:

```bash
cd ..
git add common
git commit -m "Update common submodule"
git push
```

---

### 4️⃣ CI/CD tipy

* Pri workflow, ktorý generuje dokumentáciu, nezabudni spustiť:

```bash
git submodule update --init --recursive
```

* Pri nasadzovaní na GitHub Pages sa odporúča **použiť cache Python závislostí**, aby sa workflow zrýchlil:

```yaml
- uses: actions/setup-python@v4
  with:
    python-version: '3.11'
#    cache: 'pip'
```

---

Chceš, aby som k tomuto README pridal aj **diagram workflow submodulu a generovania dokumentácie**, aby bolo vizuálne jasné, čo sa deje krok za krokom?
