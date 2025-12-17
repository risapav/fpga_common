# Modul `hdmi_tx_top`

## Popis

Hlavný modul digitálneho HDMI vysielača.

Tento modul predstavuje kompletný digitálny frontend pre HDMI vysielač.
Jeho úlohou je zobrať paralelné video, audio a paketové dáta a pretransformovať
ich na 4-bitový sériový TMDS stream pripravený na odoslanie na fyzické piny FPGA.

Funkčný tok:
1. Interný stavový automat (FSM) neustále monitoruje vstupné signály platnosti
(`video_valid_i`, `audio_valid_i`, `packet_valid_i`) a určuje aktuálnu
TMDS periódu (Video, Control, Audio alebo Data).
2. Na základe stavu FSM smeruje príslušné dáta (RGB pixely, audio/packet bajty
alebo riadiace signály HSYNC/VSYNC) do troch paralelných TMDS enkodérov.
3. Každý enkodér konvertuje 8-bitové dáta na 10-bitové DC-balansované TMDS slovo.
4. Štvrtý kanál pre TMDS hodiny je generovaný ako statický 10-bitový vzor.
5. Všetky štyri 10-bitové kanály sú poslané do `generic_serializer`-a, ktorý ich
prevedie na výsledný 4-bitový vysokorýchlostný sériový výstup.

## Parametre

- `[in]`: DDRIO           Prepínač režimu serializéra. 1 = DDR (vyžaduje 5x clk), 0 = SDR (vyžaduje 10x clk).

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Pomalý takt (paralelná doména, napr. pixel clock). |
| `clk_x_i` | Rýchly takt (serializačná doména, 5× alebo 10× clk_i). |
| `rst_ni` | Synchrónny reset, aktívny v nízkej úrovni. |
| `hsync_i,` | vsync_i Synchronizačné signály z video generátora. |
| `video_i` | 24-bitové video dáta (RGB888). |
| `video_valid_i` | Signál platnosti video dát (Data Enable). |
| `audio_i` | 8-bitové audio dáta (pre Audio Data Islands). |
| `audio_valid_i` | Signál platnosti audio dát. |
| `packet_i` | 8-bitové paketové dáta (pre InfoFrames). |
| `packet_valid_i` | Signál platnosti paketových dát. |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `hdmi_p_o` | Výsledný 4-bitový sériový stream (kladná časť diff. párov).
- hdmi_p_o[0]: Modrý kanál (TMDS Channel 2)
- hdmi_p_o[1]: Zelený kanál (TMDS Channel 1)
- hdmi_p_o[2]: Červený kanál (TMDS Channel 0)
- hdmi_p_o[3]: Hodinový kanál (TMDS Clock) |

## Príklady použitia

```systemverilog
hdmi_tx_top #(
.DDRIO(1)
) u_hdmi_tx (
.clk_i(pixel_clock),
.clk_x_i(pixel_clock_5x),
.rst_ni(reset_n),
// ... pripojenie ostatných signálov ...
.hdmi_p_o(hdmi_pins_p)
);
```

