# Modul `vga_ctrl`

## Popis

VGA kontrolér pre výstup RGB signálu a synchronizačných impulzov

Modul `vga_ctrl` je vrcholový riadiaci modul pre VGA výstup. Integruje generátor časovania (`vga_timing`)
a výstupnú logiku, ktorá riadi synchronizačné impulzy, data enable signály a farebný výstup.
Z FIFO zásobníka načítava RGB dáta v režime "aktívne zobrazovanie" (hde & vde). Ak FIFO neobsahuje dáta
počas požiadavky, výstupne sa generuje diagnostická farba `UNDERRUN_COLOR`.
Počas blankingu sa výstupne generuje `BLANKING_COLOR`.

## Parametre

- `[in]`: BLANKING_COLOR     Farba (RGB565), ktorá sa zobrazuje počas "blanking" intervalov.
- `[in]`: UNDERRUN_COLOR     Diagnostická farba zobrazovaná pri podtečení FIFO.
- `[in]`: MAX_COUNTER_H   Najvyššia hodnota, ktorú dosiahne čítač počítajúci pozíciu v H smere
- `[in]`: MAX_COUNTER_V   Najvyššia hodnota, ktorú dosiahne čítač počítajúci pozíciu v V smere

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Hlavný hodinový signál (pixel clock). |
| `rst_ni` | Asynchrónny reset, aktívny v L. |
| `enable_i` | Povolenie činnosti (aktivuje generovanie signálov). |
| `h_line_i` | Časové parametre pre horizontálnu synchronizáciu (štruktúra typu `line_t`). |
| `v_line_i` | Časové parametre pre vertikálnu synchronizáciu (štruktúra typu `line_t`). |
| `fifo_data_i` | RGB565 farebné dáta pre aktuálny pixel z FIFO zásobníka. |
| `fifo_empty_i` | Signál indikujúci prázdny FIFO (podtečenie). |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `hde_o` | Aktivita horizontálnej oblasti (1 počas ACT fázy). |
| `vde_o` | Aktivita vertikálnej oblasti (1 počas ACT fázy). |
| `dat_o` | Výstupné RGB dáta (typ `vga_data_t`) pre DAC. |
| `syn_o` | Výstupný signál typu `vga_sync_t` (obsahuje h_sync a v_sync). |
| `eol_o` | Pulz na konci riadku (End Of Line). |
| `eof_o` | Pulz na konci celej snímky (End Of Frame). |

## Príklady použitia

```systemverilog
Názorný príklad použitia:

import vga_pkg::*;

localparam VgaMode = VGA_640x480_60;
localparam int PixelClockHz = get_pixel_clock(VgaMode);

// --- Signály pre prepojenie modulov ---
rgb565_t picture_data;     // Dáta z generátora obrazu
rgb565_t   data_out;       // Finálne dáta z VGA radiča
vga_sync_t sync_out;       // Finálne sync signály z VGA radiča
wire       hde, vde;       // Data Enable signály
wire       eol, eof;       // Pulzy konca riadku/snímky

line_t      h_line;
line_t      v_line;

`ifdef __ICARUS__
// Pre simuláciu (Icarus) zadáme parametre manuálne
h_line = '{640, 16, 96, 48, PulseActiveLow};
v_line = '{480, 10, 2, 33, PulseActiveLow};
`else
// Pre syntézu (Quartus) použijeme funkciu z balíčka vga_pkg
	        vga_params_t vga_params = get_vga_params(VgaMode);
assign h_line = vga_params.h_line;
assign v_line = vga_params.v_line;
`endif

// --- Inštancia VGA radiča (časovanie + dátová cesta) ---
vga_ctrl #(
.BLANKING_COLOR(16'h0000),
.UNDERRUN_COLOR(16'hF81F)
) u_ctrl (
.clk_i        (pixel_clk),
.rst_ni       (rst_n),
.enable_i     (1'b1), // Radič beží neustále
.h_line_i     (h_line),
.v_line_i     (v_line),
.fifo_data_i  (picture_data),
.fifo_empty_i (1'b0), // Zdroj dát (generátor) nie je nikdy prázdny
.hde_o        (hde),
.vde_o        (vde),
.dat_o        (data_out),
.syn_o        (sync_out),
.eol_o        (eol),
.eof_o        (eof)
);
```

