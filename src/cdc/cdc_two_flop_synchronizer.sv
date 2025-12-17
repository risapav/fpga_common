/**
 * @file cdc_two_flop_synchronizer.sv
 * @brief Dvojstupňový synchronizátor signálu pre CDC (Clock Domain Crossing).
 * @details Parametrický WIDTH, reset aktívny LOW (negedge). Výstup q_o je
 *          výsledkom po dvoch registroch (2-FF synchronizácia).
 *
 *          Modul je označený atribútmi pre Intel/Quartus aj Xilinx nástroje:
 *          - altera_attribute (Quartus)
 *          - ASYNC_REG attribute (Xilinx)
 *
 * @param WIDTH Počet bitov signálu (predvolené 1).
 *
 * @input clk_i Hodinový signál cieľovej domény.
 * @input rst_ni Asynchrónny reset (aktívny LOW).
 * @input d_i Vstupný asynchrónny signál (WIDTH bitov).
 * @output q_o Synchronizovaný výstup (WIDTH bitov).
 */

`default_nettype none 

`ifndef CDC_TWO_FLOP_SYNCHRONIZER_SV
`define CDC_TWO_FLOP_SYNCHRONIZER_SV

module cdc_two_flop_synchronizer #(
    parameter int WIDTH = 1
) (
    input  logic [WIDTH-1:0] d_i,
    input  logic             clk_i,
    input  logic             rst_ni,
    output logic [WIDTH-1:0] q_o
);

    // prvý a druhý stupeň synchronizácie
    // pridávame atribúty pre nástroje (Xilinx/Intel)
    (* ASYNC_REG = "TRUE" *)
    logic [WIDTH-1:0] sync_ff1;

    // Quartus atribút pre rozpoznanie synchronizátora (voliteľné, ale užitočné)
    (* altera_attribute = "-name SYNCHRONIZER_IDENTIFICATION FORCED_IF_ASYNCHRONOUS" *)
    logic [WIDTH-1:0] sync_ff2;

    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            sync_ff1 <= '0;
            sync_ff2 <= '0;
            q_o      <= '0;
        end else begin
            // prvý FF zachytí asynchrónny vstup
            sync_ff1 <= d_i;
            // druhý FF a výstup
            sync_ff2 <= sync_ff1;
            q_o      <= sync_ff2;
        end
    end

endmodule

`endif // CDC_TWO_FLOP_SYNCHRONIZER_SV

`default_nettype wire
