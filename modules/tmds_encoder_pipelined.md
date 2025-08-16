# Modul `tmds_encoder_pipelined`

## Popis

TMDS enkodér pre HDMI s 3-stupňovou pipeline a DC-balancom.

Tento modul implementuje enkódovanie TMDS podľa špecifikácie DVI/HDMI.
Vstupom je 8-bitový pixelový dátový kanál a riadiace bity (HSYNC, VSYNC),
výstupom je 10-bitové TMDS kódové slovo. Modul udržuje bežiacu disparitu
(running disparity) pre zabezpečenie DC-balansu. Je rozdelený do troch
pipeline stupňov:
- **S1**: Minimalizácia prechodov (8b -> 9b) + predvýpočet počtu jednotiek
- **S2**: Registrovanie medzivýsledkov (ones_in_qm8 sa prenáša pipelineom)
- **S3**: DC-balanovanie a výber výsledného 10b kódu

Modul podporuje režimy:
- VIDEO_PERIOD (štandardné TMDS enkódovanie pixelov)
- CONTROL_PERIOD (špeciálne riadiace symboly C0, C1)
- AUDIO_PERIOD a DATA_PERIOD (guard bands podľa HDMI špecifikácie)

Latencia modulu je fixne 3 taktovacie cykly.

## Parametre

- `[in]`: clk_i        Taktovací signál (pixel clock)
- `[in]`: rst_ni       Synchrónny reset, aktívny v nízkej úrovni
- `[in]`: data_i       8-bitové video dáta (tmds_data_t)
- `[in]`: data_type_i  Typ periódy (VIDEO, CONTROL, AUDIO, DATA)
- `[in]`: c0_i         Control bit 0 (napr. HSYNC)
- `[in]`: c1_i         Control bit 1 (napr. VSYNC)
- `[out]`: tmds_o       Výsledné 10-bitové TMDS kódové slovo

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Hlavný hodinový signál |
| `rst_ni` | Reset vstup (aktívny v 0) |
| `data_i` | Video dáta (RGB kanál) |
| `data_type_i` | Určuje režim enkódovania |
| `c0_i,` | c1_i   HDMI control signály |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `tmds_o` | Enkódovaný TMDS výstup |

## Príklady použitia

```systemverilog
// Príklad inštancie enkodéra pre jeden TMDS kanál
tmds_encoder_pipelined encoder_inst (
.clk_i       (clk_pixel),
.rst_ni      (rst_n),
.data_i      (pixel_r),
.data_type_i (VIDEO_PERIOD),
.c0_i        (hsync),
.c1_i        (vsync),
.tmds_o      (tmds_red)
);
```

