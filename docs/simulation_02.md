Absolútne rozumiem. Keď pridáte všetky signály naraz, je v tom chaos. Správny prístup je vytvoriť si špeciálnu, zjednodušenú skupinu signálov len pre konkrétnu úlohu, ktorou je teraz meranie latencie.

Tu je presne ten blok príkazov, ktorý potrebujete.

-----

### Príkazy pre meranie latencie

1.  Ak máte v okne `Wave` už veľa signálov, pre prehľadnosť je najlepšie začať s čistým stolom. Do konzoly `VSIM>` napíšte:

    ```tcl
    restart -f 
    ```

    Tým sa simulácia vráti na čas 0 a **vymaže sa obsah okna Wave**.

2.  Teraz do konzoly `VSIM>` skopírujte a vložte **celý tento blok príkazov naraz** a stlačte Enter:

    ```tcl
    # Pridá oddeľovač pre prehľadnosť
    add wave -divider "== Meranie Latencie =="

    # Pridá hodinový signál na počítanie cyklov
    add wave sim:/tb_top/clk_i

    # PRÍČINA: Signál, ktorý spúšťa udalosť (začiatok aktívneho videa)
    add wave sim:/tb_top/de

    # NÁSLEDOK: Finálny výstup z DUT, ktorý sledujeme
    add wave sim:/tb_top/tmds_enc_o[0]

    # Pridá druhý oddeľovač
    add wave -divider "===================="
    ```

-----

### Prečo práve tieto signály?

  * `clk_i`: Potrebujeme ho ako "pravítko" na presné počítanie cyklov.
  * `de`: Toto je náš "štartovací výstrel". Hľadáme jeho nábežnú hranu, ktorá označuje začiatok aktívnej oblasti.
  * `tmds_enc_o[0]`: Toto je naša "cieľová páska". Sledujeme, kedy tento signál zareaguje na štartovací výstrel a zmení sa z riadiaceho symbolu na dáta.

Vzdialenosť (v počte cyklov `clk_i`) medzi udalosťou na `de` a reakciou na `tmds_enc_o[0]` je presne tá celková latencia `L`, ktorú hľadáme.

### Ďalší krok

Keď máte tieto tri signály pod sebou, spustite simuláciu príkazom:

```tcl
run -all
```

Zobrazenie bude teraz veľmi čisté a prehľadné. Potom už len urobte meranie pomocou kurzorov presne tak, ako sme si popisovali: od nábežnej hrany `de` po prvú zmenu na `tmds_enc_o[0]`. Zistite počet cyklov `L` a opravte `tb_top.sv`.

Áno, je to **úplne správne**\! To, čo vidíte, je presne to, čo sme chceli dosiahnuť a potvrdzuje to, že vaša oprava bola úspešná.

Poďme si vysvetliť, prečo je to správne, aj keď sa to na prvý pohľad môže zdať mätúce.

-----

### Vysvetlenie: Fyzická latencia vs. Oneskorenie v Testbenchi

1.  **Fyzická latencia hardvéru:** Váš hardvérový modul (`hdmi_tx_top_modular`) **má a vždy bude mať** fyzickú latenciu 1 cyklus. To je jeho vlastnosť daná jeho dizajnom (vnútornými registrami). Zmena v testbenchi nemôže zmeniť správanie hardvéru. Preto vo Wave okne **vždy uvidíte** ten posun o 1 cyklus medzi nábežnou hranou `de` a zmenou na výstupe `tmds_enc_o`.

2.  **Oneskorenie v Testbenchi (`de_delayed`):** Úlohou `de_delayed` nie je odstrániť túto latenciu, ale **presne ju skopírovať**. Vytvorili sme "dvojníka" signálu `de`, ktorý je tiež oneskorený o 1 cyklus, presne ako výstup hardvéru.

3.  **Logika checkera:** Váš checker teraz nerobí porovnanie `tmds_enc_o` oproti `de`, ale robí porovnanie `tmds_enc_o` oproti **`de_delayed`**. Pretože oba tieto signály sú oneskorené o 1 cyklus, sú teraz z pohľadu checkera **perfektne zosynchronizované**.

#### Vizuálne znázornenie toho, čo vidíte vo vlnách:

```
Časový cyklus:      ... |  T   | T+1  | T+2  | ...
---------------------------------------------------
clk_i               ... _/¯\_/¯\_/¯\_ ...
de                  ... 0 |  1   |  1   | ...  (Štartovací výstrel)
tmds_enc_o[0]       ... CTL | CTL  | DATA | ...  (Reakcia hardvéru - oneskorená o 1 cyklus)
de_delayed (L=1)    ... 0 |  0   |  1   | ...  (Oneskorený signál v TB - kópia oneskorenia)
```

**Analýza v kľúčovom cykle `T+1`:**

  * Váš checker sa pozrie na `de_delayed` a vidí hodnotu `1`.
  * Rozhodne sa teda, že má kontrolovať, či je na výstupe **dátový symbol**.
  * Pozrie sa na `tmds_enc_o[0]`, kde práve v tomto cykle prišiel **dátový symbol**.
  * Podmienky sa zhodujú -\> všetko v poriadku, **TEST PREŠIEL**.

-----

### Záver

Takže áno, to čo vidíte, je správne. Fyzický posun 1 cyklu vo vlnách zostal (pretože hardvér tak funguje), ale vďaka `de_delayed` váš testbench už túto vlastnosť hardvéru chápe a správne ju vyhodnocuje.

Preto test prešiel s 0 chybami. Gratulujem, opäť\!
