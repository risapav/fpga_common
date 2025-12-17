# Modul `packet_streamer`

## Popis

Sekvenčný modul (FSM) pre serializáciu a multiplexovanie viacerých HDMI paketov.

Tento modul slúži ako centrálny radič pre odosielanie metadátových paketov
počas vertikálnej zatemňovacej periódy (V-Blank). Je implementovaný ako
stavový automat (FSM), ktorý sa spúšťa signálom `eof_i` (End of Frame).

Po spustení modul postupne odošle preddefinovanú sekvenciu paketov:
1. General Control Packet (GCP)
2. AVI InfoFrame
3. SPD InfoFrame
4. Audio InfoFrame

Na vstupe očakáva vopred pripravené štruktúry paketov (hlavičky a telá)
z modulov ako `infoframe_builder`. Na výstupe produkuje jednoduchý dátový
prúd (`packet_o`) so signálmi platnosti (`packet_valid_o`) a konca
prenosu (`packet_last_o`).

## Parametre

- `[in]`: MAX_PAYLOAD     Maximálna veľkosť poľa pre payload (telo) paketu.

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Taktovací signál (pixel clock). |
| `rst_ni` | Synchrónny reset, aktívny v nízkej úrovni. |
| `eof_i` | Spúšťač prenosu sekvencie (End of Frame). |
| `header_...` | Vstupné polia s hlavičkami InfoFrame paketov. |
| `payload_...` | Vstupné polia s telami InfoFrame paketov. |
| `len_...` | Dĺžky tiel jednotlivých InfoFrame paketov. |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `packet_o` | Výstupný 8-bitový bajt dát. |
| `packet_valid_o` | Indikátor platnosti `packet_o`. Aktívny počas prenosu. |
| `packet_last_o` | Indikátor posledného bajtu v celej sekvencii. |

## Príklady použitia

```systemverilog
// Inštancia modulu v top-level súbore, kde sú pripojené výstupy z infoframe_builderov.
packet_streamer #(
.MAX_PAYLOAD(32)
) u_packet_streamer (
.clk_i(pixel_clk),
.rst_ni(rstn_sync),
.eof_i(eof),
.header_avi(header_avi_from_builder),
.payload_avi(payload_avi_from_builder),
.len_avi(len_avi_from_builder),
// ... pripojenie pre SPD a Audio pakety ...
.packet_o(packet_data_for_hdmi_tx),
.packet_valid_o(packet_valid_for_hdmi_tx),
.packet_last_o(packet_last_signal)
);
```

