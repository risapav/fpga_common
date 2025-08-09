# Modul `unknown_module`

## Popis

VGA parametre a typy (balíček)

Balíček `vga_pkg` definuje všetky potrebné konštanty, dátové typy, štruktúry a pomocné funkcie
súvisiace s VGA časovaním a výstupom obrazu. Obsahuje štandardné režimy, polárne konštanty,
preddefinované RGB farby, ako aj funkcie na výpočet VGA parametrov.

## Parametre

- `[in]`: MaxLineCounter     Maximálna hodnota pre generátor riadkov (`vga_line`). Definuje šírku čítača.
- `[in]`: MaxPosCounterX     Maximálna horizontálna pozícia v pixeloch (napr. 1920).
- `[in]`: MaxPosCounterY     Maximálna vertikálna pozícia v pixeloch (napr. 1080).
- `[in]`: PulseActiveHigh    Konštanta definujúca aktívnu vysokú polaritu synchronizačných signálov.
- `[in]`: PulseActiveLow     Konštanta definujúca aktívnu nízku polaritu synchronizačných signálov.

@typedef     vga_mode_e         Výčtový typ definujúci podporované VGA režimy podľa VESA.
@typedef     line_t             Štruktúra popisujúca časovanie (visible_area, sync_pulse atď.) a polaritu.
@typedef     vga_data_t         Formát pixelu RGB565 (5:6:5).
@typedef     rgb565_t           Formát pixelu RGB565 (5:6:5).
@typedef     rgb888_t           Formát pixelu RGB888 (8:8:8).
@typedef     vga_sync_t         Štruktúra synchronizačných signálov (hs, vs).
@typedef     vga_params_t       Zjednotená štruktúra s horizontálnym a vertikálnym časovaním.

@function    get_vga_params()   Vráti kompletné časovanie (H + V) pre daný VGA režim.
@function    get_pixel_clock()  Vráti požadovanú frekvenciu pixelov v Hz pre daný VGA režim.
@function    get_total_pixels_per_frame()  Vypočíta celkový počet pixelov v jednej snímke (s blankingom).

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `RGB` | farby          Konštanty `RED`, `GREEN`, `BLUE`, `WHITE` atď. vo formáte `vga_data_t`. |

## Príklady použitia

```systemverilog
Použitie v module:
import vga_pkg::*;

vga_params_t params = get_vga_params(VGA_800x600_60);
int clk_hz = get_pixel_clock(VGA_800x600_60);
```

