# Modul `cdc_two_flop_synchronizer`

## Popis

Dvojstupňový synchronizátor signálu pre CDC (Clock Domain Crossing).

Parametrický WIDTH, reset aktívny LOW (negedge). Výstup q_o je
výsledkom po dvoch registroch (2-FF synchronizácia).

Modul je označený atribútmi pre Intel/Quartus aj Xilinx nástroje:
- altera_attribute (Quartus)
- ASYNC_REG attribute (Xilinx)

## Parametre

- `WIDTH`: Počet bitov signálu (predvolené 1).

## Vstupy (input)

| Názov | Popis |
|-------|--------|
| `clk_i` | Hodinový signál cieľovej domény. |
| `rst_ni` | Asynchrónny reset (aktívny LOW). |
| `d_i` | Vstupný asynchrónny signál (WIDTH bitov). |

## Výstupy (output)

| Názov | Popis |
|-------|--------|
| `q_o` | Synchronizovaný výstup (WIDTH bitov). |

