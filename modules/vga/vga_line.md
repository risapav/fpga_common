# Modul `vga_line`

## Popis

Generátor jednej časovej periódy VGA signálu

Modul `vga_line` implementuje konečný stavový automat (FSM), ktorý generuje
časovanie jednej línie VGA signálu (horizontálnej alebo vertikálnej) podľa
štruktúry `line_t`. FSM prechádza stavmi: aktívna oblasť (ACT), front porch (FRP),
synchronizačný impulz (SYN), back porch (BCP) a koniec riadku (EOL).
Výstupy indikujú aktuálnu fázu a generujú synchronizačné a riadiace signály.

## Parametre

- `[in]`: MAX_COUNTER        Najvyššia hodnota, ktorú dosiahne čítač.

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Hlavný hodinový signál. |
| `rst_ni` | Synchrónny reset, aktívny v L. |
| `inc_i` | Inkrementačný pulz (tick), ktorý aktivuje zmenu stavu FSM. |
| `line_i` | Časová štruktúra `line_t` s nastaveniami dĺžok jednotlivých fáz. |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `de_o` | Data Enable – vysoká počas aktívnej oblasti (ACT). |
| `syn_o` | Synchronizačný výstup – vysoký počas fáz SYN. |
| `eol_o` | End Of Line – jednocyklický pulz označujúci koniec celej periódy. |
| `nol_o` | Next Of Line – jednocyklický pulz jeden takt pred EOL. |

## Príklady použitia

```systemverilog
Názorný príklad použitia:
vga_line #(
.MAX_COUNTER(MaxLineCounter))
) u_hline (
.clk_i(clk),
.rst_ni(rst_n),
.inc_i(1'b1),
.line_i(h_line),
.de_o(hde),
.syn_o(hsyn),
.eol_o(eol),
.nol_o(nol)
);
```

