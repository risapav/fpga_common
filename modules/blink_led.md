# Modul `blink_led`

## Popis

Jednoduchý modul na blikanie LED s nastaviteľnou frekvenciou.

Modul generuje signál pre LED, ktorá bliká so zadanou frekvenciou
na základe vstupného hodinového signálu. Počet taktov na jednu polperiódu
sa vypočíta z parametrov `CLOCK_FREQ_HZ` a `BLINK_HZ`.

## Parametre

- `[in]`: CLOCK_FREQ_HZ  Frekvencia vstupného hodinového signálu v Hz (predvolené 50 MHz).
- `[in]`: BLINK_HZ       Požadovaná frekvencia blikania LED v Hz (predvolené 1 Hz).

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Vstupný hodinový signál. |
| `rst_ni` | Aktívny nízky synchronný reset. |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `led_o` | Výstupný signál pre LED (blikajúci). |

## Príklady použitia

```systemverilog
blink_led #(
.CLOCK_FREQ_HZ(50_000_000),
.BLINK_HZ(2)
) u_blink_led (
.clk_i(clk),
.rst_ni(rst_n),
.led_o(led)
);
```

