# Modul `picture_gen`

## Popis

Generátor testovacích obrazcov pre VGA výstup.

Modul generuje rôzne testovacie obrazce (šachovnice, prechody, farebné pruhy, pohyblivé prvky)
automaticky prispôsobené rozlíšeniu definovanému parametrom a riadené režimom `mode_i`.
Vstupy sú súradnice pixelov, signály časovania a povolenie činnosti modulu.

## Parametre

- `[in]`: MaxModes     Počet dostupných režimov generovania obrazcov.
- `[in]`: MAX_COUNTER_H   Najvyššia hodnota, ktorú dosiahne čítač počítajúci pozíciu v H smere
- `[in]`: MAX_COUNTER_V   Najvyššia hodnota, ktorú dosiahne čítač počítajúci pozíciu v V smere
- `[in]`: ModeWidth    Šírka bitov pre výber režimu (voľba obrazca).

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Hodinový signál (pixel clock). |
| `rst_ni` | Synchrónny reset, aktívny v L. |
| `enable_i` | Povolenie generovania obrazcov. |
| `h_line_i` | Informácie o horizontálnom časovaní (line_t typ). |
| `v_line_i` | Informácie o vertikálnom časovaní (line_t typ). |
| `x_i` | Aktuálna X súradnica pixelu. |
| `y_i` | Aktuálna Y súradnica pixelu. |
| `de_i` | Data Enable – indikuje viditeľnú oblasť pixelov. |
| `mode_i` | Výber režimu generátora obrazcov. |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `data_o` | Výstupný RGB565 dátový signál pre aktuálny pixel. |

## Príklady použitia

```systemverilog
import vga_pkg::*;

picture_gen #(
.MaxModes(8),
.MAX_COUNTER_H(MaxPosCounterX),
.MAX_COUNTER_V(MaxPosCounterY)
) u_picture_gen (
.clk_i(clk),
.rst_ni(rst_n),
.enable_i(1'b1),
.h_line_i(h_line),
.v_line_i(v_line),
.x_i(pixel_x),
.y_i(pixel_y),
.de_i(data_enable),
.mode_i(3'd2),
.data_o(rgb_data)
);
```

