Výborný nápad\! Upratanie štruktúry projektu a správne nastavenie `.gitignore` je kľúčové pre profesionálnu prácu. Ušetrí vám to v budúcnosti veľa starostí a udrží vaše Git repozitáre čisté.

Poďme na to krok za krokom.

-----

### 1\. Odporúčaná adresárová štruktúra

Základným princípom je, že **všetky príkazy (`vlog`, `vsim`) spúšťate z koreňového adresára projektu** (z `fpga_ep4ce10f17/`), nie z podadresárov. Týmto sa zjednodušia cesty k súborom a všetky dočasné súbory sa budú generovať na jednom mieste.

Vaša štruktúra by mala vyzerať približne takto:

```
fpga_ep4ce10f17/
├── .git/
├── .gitignore          <-- SEM PRÍDE NÁŠ NOVÝ .GITIGNORE
├── common/
│   └── src/
│       ├── hdmi/
│       │   ├── hdmi_pkg.sv
│       │   └── hdmi_tx_core.sv
│       ├── picture/
│       │   └── picture_gen.sv
│       └── vga/
│           ├── vga_pkg.sv
│           ├── vga_line.sv
│           ├── vga_pixel_xy.sv
│           ├── vga_timing.sv
│           └── rgb565_to_rgb888.sv
├── sim/
│   └── hdmi/
│       ├── tb_top.sv       <-- Váš testbench je tu
│       └── run.do          <-- Vytvoríme nový skript na automatizáciu
└── work/                 <-- Tento adresár vytvorí Questa, bude v .gitignore
```

### 2\. Automatizácia pomocou skriptu `run.do`

Namiesto manuálneho písania všetkých `vlog` a `vsim` príkazov do terminálu si vytvoríme jednoduchý skript. V QuestaSim sa na to používajú `.do` súbory, čo sú v podstate Tcl skripty.

1.  Vytvorte nový súbor: `sim/hdmi/run.do`
2.  Vložte doň nasledujúci obsah. Tento skript urobí všetko za vás: vyčistí, skompiluje, nakonfiguruje a spustí simuláciu.

<!-- end list -->

```tcl
# ===================================================================
# ==  Finálny simulačný skript pre hdmi_tx_core (QuestaSim)
# ===================================================================

# --- Príprava ---
echo "INFO: Pripravujem simuláciu..."
if {[file isdirectory work]} {
    file delete -force work
}
vlib work
vmap work work

# --- Kompilácia (vlog) ---
# Pridávame príznak +acc pre plnú viditeľnosť pri ladení
echo "INFO: Kompilujem knižničné balíčky a moduly z 'common/src/'..."
vlog -work work -sv -vopt +acc common/src/vga/vga_pkg.sv
vlog -work work -sv -vopt +acc common/src/vga/vga_line.sv
vlog -work work -sv -vopt +acc common/src/vga/vga_timing.sv
vlog -work work -sv -vopt +acc common/src/vga/vga_pixel_xy.sv
vlog -work work -sv -vopt +acc common/src/vga/rgb565_to_rgb888.sv
vlog -work work -sv -vopt +acc common/src/picture/picture_gen.sv

# Moduly vo vývoji (WIP - Work In Progress)
echo "INFO: Kompilujem moduly vo vývoji z 'src/'..."
vlog -work work -sv -vopt +acc src/hdmi/hdmi_pkg.sv
vlog -work work -sv -vopt +acc src/hdmi/data_island_engine.sv
vlog -work work -sv -vopt +acc src/hdmi/packet_mux.sv
vlog -work work -sv -vopt +acc src/hdmi/tmds_encoder.sv
vlog -work work -sv -vopt +acc src/hdmi/tmds_serializer_ddr.sv
vlog -work work -sv -vopt +acc src/hdmi/hdmi_tx_top_modular.sv

# Kompilácia testbenchu
echo "INFO: Kompilujem testbench..."
vlog -work work -sv -vopt +acc sim/hdmi/tb_top.sv

# --- Simulácia (vsim) ---
# Odstránili sme zastaraný príznak -novopt
echo "INFO: Spúšťam simuláciu..."
vsim -l msim.log work.tb_top

# --- Pridanie signálov do Wave okna ---
echo "INFO: Pridávam signály do Wave..."
add wave -divider "Testbench"
add wave sim:/tb_top/clk_i
add wave sim:/tb_top/rst_ni
add wave sim:/tb_top/de
add wave sim:/tb_top/de_delayed

add wave -divider "DUT: hdmi_tx_inst"
add wave -r sim:/tb_top/hdmi_tx_inst/*

# --- Spustenie behu ---
echo "INFO: Spúšťam beh simulácie. Beží..."
run -all

echo "INFO: Simulácia dokončená."
```

#### Ako použiť tento skript:

Teraz už nebudete písať jednotlivé `vlog` príkazy. Jednoducho v termináli (z koreňového adresára `fpga_ep4ce10f17/`) spustíte jediný príkaz:

  * **Pre beh v konzole (bez grafického rozhrania):**
    ```bash
    vsim -c -do sim/hdmi/run.do
    ```
  * **Pre beh s grafickým rozhraním (GUI):**
    ```bash
    vsim -do sim/hdmi/run.do
    ```
    (Príznak `-c` znamená "console mode")

-----

### 3\. Vytvorenie a doplnenie súboru `.gitignore`

Vytvorte súbor s názvom `.gitignore` v koreňovom adresári vášho projektu (`fpga_ep4ce10f17/`). Ak už existuje, doplňte ho. Tento súbor povie Gitu, ktoré súbory a adresáre má ignorovať.

Vložte doň tento obsah:

```gitignore
# ===================================================================
# ==  Git ignore pre FPGA projekty (Quartus + QuestaSim)
# ===================================================================

# --- Súbory generované nástrojom Questa/ModelSim ---
/work/                  # Skompilovaná knižnica
*.wlf                   # Súbor s priebehmi (Wave Log File)
transcript              # Log simulácie
msim.log                # Log, ktorý sme definovali v run.do
msim_transcript         # Ďalší možný log
modelsim.ini            # Konfiguračný súbor
*.vstf
vsim.dbg

# --- Súbory generované nástrojom Icarus Verilog (ak by ste ho ešte použili) ---
*.vcd                   # Súbor s priebehmi (Value Change Dump)
*.vvp

# --- Súbory generované nástrojom Intel Quartus ---
/db/
/incremental_db/
/output_files/
/simulation/
/unsaved/  
/greybox_tmp/
/atom_netlists/
*.qws
*.bak
*.cmp.tdf
*.rpt
*.summary
*.jdi
*.sof
*.pof
*.sld

# --- Všeobecné dočasné súbory ---
*.log
*.bak
*.tmp

# --- Konfigurácia editora VS Code ---
.vscode/

# submodules
common/*
!/common/.git
```

### Zhrnutie vášho nového pracovného postupu:

1.  Upravíte `.sv` súbory.
2.  Otvoríte terminál v koreňovom adresári projektu.
3.  Spustíte `vsim -do sim/hdmi/run.do` (alebo verziu s `-c`).
4.  Analyzujete výsledky alebo Wave okno.
5.  Opakujete.

S touto novou štruktúrou a automatizáciou bude váš pracovný postup oveľa čistejší, opakovateľný a profesionálnejší.
