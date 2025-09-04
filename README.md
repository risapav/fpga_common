# fpga_common
Zdieľaná knižnica modulov pre FPGA projekty

## ✅ Odporúčané riešenie: Git submoduly

### 💡 Kedy použiť:

Ak chceš mať knižnicu a dokumentáciu ako samostatný repozitár a chceš, aby projekty vždy používali konkrétnu verziu tejto knižnice.
### 🔧 Krok 1: Vytvor samostatný repozitár

Vytvor nový repozitár, napr.:

```bash
risapav/fpga_common
```

a presuň tam priečinky scs/ a docs_md/:

```
fpga_common/
├── scs/
└── docs_md/
```

### 🔧 Krok 2: Pridaj ho ako submodul do oboch projektov

V koreňovom adresári projektu (napr. fpga_ep4ce55f23):

```bash
git submodule add https://github.com/risapav/fpga_common common

# alebo

git submodule add git@github.com:risapav/fpga_common.git common
```

Tým sa knižnica a dokumentácia objavia ako:

```
fpga_ep4ce55f23/
├── common/
│   ├── scs/
│   └── docs_md/
├── src/
├── ...
```

    Prístup k súborom: common/scs/..., common/docs_md/...

### 🔧 Krok 3: Commitni a pushni submodul

```bash
git add .gitmodules common/
git commit -m "Pridaný submodul fpga_common"
git push
```

### 🔧 Krok 4: Práca s submodulom

Keď niekto klonuje projekt, musí spustiť:

```bash
git clone --recurse-submodules https://github.com/risapav/fpga_ep4ce55f23

# alebo po clone

git submodule sync
git submodule update --init --recursive
```

Pri úprave fpga_common, v konkrétnom projekte spustíš:

```bash
cd common
git pull origin main  # alebo iný branch
cd ..
git add common
git commit -m "Update common submodule to latest"
git push
git config status.showUntrackedFiles no
```

## Ak je problém, ktorý ti Git hlási, podobný tomuto:

```
error: Your local changes to the following files would be overwritten by merge:
	src/picture/picture_gen.sv
Please commit your changes or stash them before you merge.
Aborting
```

### Čo to znamená?

* Pokúšaš sa stiahnuť najnovšie zmeny z vetvy `main` z repozitára `origin`, ale máš **lokálne neuložené zmeny** v súbore `src/picture/picture_gen.sv`.
* Ak by Git pokračoval v merge alebo pull, prepísal by tento súbor zo vzdialeného repozitára, čo nechce spraviť bez tvojho vedomia.
* Git sa teda zastaví, aby si mal možnosť si svoje zmeny uložiť (commit) alebo ich odložiť bokom (stash).

---

### Riešenie

Vyber si jednu z možností:

---

#### ✅ Ak chceš svoje zmeny **zachovať**:

1. Ulož ich pomocou commit-u:

   ```bash
   git add src/picture/picture_gen.sv
   git commit -m "Moje zmeny v picture_gen.sv"
   git pull -f origin main
   ```

2. **Alebo** ak to ešte nechceš commitnúť, môžeš ich "odložiť" (stashnúť):

   ```bash
   git stash
   git pull -f origin main
   git stash pop
   ```

   > Poznámka: Ak `stash pop` skončí s konfliktom, budeš ho musieť vyriešiť manuálne.

---

#### ❌ Ak tvoje zmeny **nepotrebuješ**, môžeš ich zahodiť:

> Upozornenie: Prídeš o neuložené zmeny.

```bash
git checkout -- src/picture/picture_gen.sv
git pull -f origin main
```

---

Chceš, aby sme spolu pozreli, čo presne si zmenil v tom súbore? Môžeš použiť:

```bash
git diff src/picture/picture_gen.sv
```

Alebo ak potrebuješ, vysvetlím aj stash, conflict resolve, alebo prácu so submodulmi detailnejšie.

