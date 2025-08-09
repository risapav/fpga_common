# Modul `seven_seg_mux`

## Popis

Modul pre multiplexovanie 7-segmentového displeja.

Tento modul umožňuje zobrazovanie viacerých číslic na jednom 7-segmentovom displeji pomocou multiplexovania.
Vstupné číslice a bodky sú postupne zobrazované v pravidelnom časovom intervale s frekvenciou `DIGIT_REFRESH_HZ`.
Modul obsahuje interný segmentový dekóder a podporuje displeje so spoločnou anódou alebo katódou.

## Parametre

- `[in]`: CLOCK_FREQ_HZ      Frekvencia hodinového signálu (Hz). Predvolené: 50_000_000.
- `[in]`: NUM_DIGITS         Počet číslic na displeji. Predvolené: 3.
- `[in]`: DIGIT_REFRESH_HZ   Frekvencia prepínania medzi číslicami (Hz). Predvolené: 250.
- `[in]`: COMMON_ANODE       Typ displeja: 1 = spoločná anóda (CA), 0 = spoločná katóda (CK).

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Vstupný hodinový signál. |
| `rst_ni` | Synchronný reset, aktívny v L. |
| `digits_i` | Pole číslic (0–F) pre každý digit. |
| `dots_i` | Pole logických hodnôt pre desatinné bodky. |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `digit_sel_o` | Výber aktuálne zobrazovanej číslice (one-hot). |
| `segment_sel_o` | Výstupné segmenty: DP,G,F,E,D,C,B,A. |
| `current_digit_o` | Index práve zobrazovanej číslice. |

## Príklady použitia

```systemverilog
seven_seg_mux #(
.CLOCK_FREQ_HZ(50_000_000),
.NUM_DIGITS(4),
.DIGIT_REFRESH_HZ(500),
.COMMON_ANODE(1)
) u_display (
.clk_i(clk),
.rst_ni(rst_n),
.digits_i({digit3, digit2, digit1, digit0}),
.dots_i({dot3, dot2, dot1, dot0}),
.digit_sel_o(digit_sel),
.segment_sel_o(segment_sel),
.current_digit_o(active_digit)
);
```

