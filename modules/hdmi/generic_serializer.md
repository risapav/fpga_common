# Modul `generic_serializer`

## Popis

Generický, parametrizovateľný N-kanálový serializátor so synchronizovaným CDC a voliteľným DDR/SDR režimom.

Tento modul prevádza N paralelných slov pevnej šírky na N sériových výstupov.
Implementuje dvojstupňový CDC mechanizmus (`shadow_reg` + `load_toggle`) pre robustný prenos dát
z pomalej hodinovej domény (clk_i) do rýchlej domény (clk_x_i).

Podporuje:
- DDR režim (2 bity za cyklus, vyžaduje 5× clk_i).
- SDR režim (1 bit za cyklus, vyžaduje 10× clk_i).
- Obojstrannú serializáciu (LSB-first / MSB-first).
- Držanie posledného stavu pri `enable_i=0`.

## Parametre

- `[in]`: DDRIO Prepínač režimu. 1 = DDR (2 bity/clk_x_i), 0 = SDR (1 bit/clk_x_i).
- `[in]`: NUM_PHY_CHANNELS Počet fyzických kanálov na serializáciu (napr. 4 pre HDMI).
- `[in]`: WORD_WIDTH Šírka serializovaného slova (napr. 10 pre TMDS).
- `[in]`: LSB_FIRST Poradie serializácie. 1 = LSB prvý, 0 = MSB prvý.
- `[in]`: IDLE_WORD Vzor, ktorý sa uloží po resete a drží sa pri neaktívnom `enable_i`.

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `rst_ni` | Asynchrónny, aktívne nízky reset. |
| `enable_i` | Povolenie činnosti. Pri 0 sa posúvanie zastaví a výstupy držia poslednú hodnotu. |
| `clk_i` | Pomalý takt (paralelná doména, napr. pixel clock). |
| `clk_x_i` | Rýchly takt (serializačná doména, 5× alebo 10× clk_i). |
| `word_i` | Pole paralelných vstupných slov (šírky WORD_WIDTH). |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `data_request_o` | Impulz v clk_i doméne, keď modul očakáva nové dáta. |
| `phys_o` | Pole sériových výstupov (mapovaných na fyzické piny). |

## Príklady použitia

```systemverilog
// Ukážka použitia v HDMI vysielači
generic_serializer #(
.DDRIO(1),
.NUM_PHY_CHANNELS(4),
.WORD_WIDTH(10),
.LSB_FIRST(1),
.IDLE_WORD('0)
) u_tmds_serializer (
.rst_ni(rst_n),
.enable_i(hdmi_enable),
.clk_i(pixel_clk),
.clk_x_i(pixel_clk_5x),
.word_i(serializer_words),
.data_request_o(serializer_data_request),
.phys_o(hdmi_tmds_p)
);
```

