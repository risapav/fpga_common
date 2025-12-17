# Modul `cdc_reset_synchronizer`

## Popis

Synchronizátor asynchrónneho resetu pre cieľovú hodinovú doménu.

Modul zabezpečuje bezpečnú synchronizáciu uvoľnenia asynchrónneho
reset signálu pomocou N-stupňového reťazca (predvolene 2 FF).
Reset je vstupne asynchrónny, výstup je synchronný a aktívny v L.

## Parametre

- `[in]`: STAGES      Počet za sebou radených FF pre synchronizáciu (minimálne 2).

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Hodinový signál cieľovej domény. |
| `rst_ni` | Asynchrónny reset, aktívny nízky. |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `rst_no` | Synchronný reset, aktívny nízky. |

## Príklady použitia

```systemverilog
cdc_reset_synchronizer #( .STAGES(2) ) u_rst_sync (
.clk_i   (clk),
.rst_ni  (async_rst_n),
.rst_no  (sync_rst_n)
);
```

