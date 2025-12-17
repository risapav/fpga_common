# Modul `infoframe_builder`

## Popis

Kombinačný modul na stavbu štruktúry HDMI InfoFrame paketov.

Tento modul generuje kompletnú štruktúru InfoFrame paketu (hlavičku a telo)
na základe parametra IF_TYPE a príslušných vstupov. Podporuje typy
AVI, SPD a Audio. Výstupom sú polia bajtov pre hlavičku a telo,
dĺžka tela a vypočítaný kontrolný súčet (checksum) na pozícii payload_o[0].
Modul je čisto kombinačný a pripravený na pripojenie k serializačnej jednotke.

## Parametre

- `[in]`: IF_TYPE         Typ InfoFrame-u na vygenerovanie (z hdmi_pkg::infoframe_type_e).
- `[in]`: HEADER_MAX      Veľkosť poľa pre hlavičku (štandardne 3).
- `[in]`: PAYLOAD_MAX     Maximálna veľkosť poľa pre telo paketu (štandardne 32).

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `color_format_i` | Farebný formát pre AVI (RGB/YUV). |
| `aspect_ratio_i` | Pomer strán pre AVI (4:3 / 16:9). |
| `quant_range_i` | Dynamický rozsah pre AVI (Full/Limited). |
| `vic_code_i` | Video Identification Code pre AVI. |
| `vendor_name_i` | Meno výrobcu pre SPD (8 znakov ASCII). |
| `product_desc_i` | Popis produktu pre SPD (16 znakov ASCII). |
| `source_device_i` | Typ zdrojového zariadenia pre SPD. |
| `audio_channels_i` | Počet audio kanálov - 1 (napr. 1 pre 2 kanály). |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `header_o` | Pole 3 bajtov hlavičky (Typ, Verzia, Dĺžka). |
| `payload_o` | Pole bajtov tela paketu (payload_o[0] je checksum). |
| `payload_len_o` | Skutočná dĺžka tela paketu v bajtoch. |

## Príklady použitia

```systemverilog
// Inštancia pre generovanie AVI InfoFrame pre 800x600@60Hz, 4:3, RGB Full Range
infoframe_builder #(
.IF_TYPE(hdmi_pkg::INFO_AVI)
) avi_builder_inst (
.color_format_i(hdmi_pkg::COLOR_FORMAT_RGB),
.aspect_ratio_i(hdmi_pkg::ASPECT_RATIO_4_3),
.quant_range_i(hdmi_pkg::QUANT_RANGE_FULL),
.vic_code_i(8'd25),
// Ostatné vstupy môžu byť nepripojené (pre syntézu sa optimalizujú preč)
.header_o(avi_header),
.payload_o(avi_payload),
.payload_len_o(avi_payload_len)
);
```

