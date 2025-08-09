# Modul `unknown_module`

## Popis

Centrálna konfigurácia AXI-Stream zbernice.

Tento balíček definuje základné parametre a dátové typy
pre AXI4-Stream komunikáciu používanú v celom projekte.
Umožňuje jednotnú konfiguráciu šírky dát a používateľských signálov.

## Parametre

- `AXI_DATA_WIDTH`: Šírka TDATA zbernice v bitoch (default: 16).
- `AXI_USER_WIDTH`: Šírka TUSER signálu v bitoch (default: 1).

@typedef     axi4s_payload_t  Dátová štruktúra pre AXI4-Stream prenos.

## Príklady použitia

```systemverilog
// Príklad použitia v module:
import axi_pkg::*;
axi4s_payload_t payload;
assign payload.TDATA = 16'hABCD;
assign payload.TUSER = 1'b0;
assign payload.TLAST = 1'b1;
```

