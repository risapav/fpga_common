/**
 * @brief       Synchronizátor asynchrónneho resetu pre cieľovú hodinovú doménu.
 * @details     Modul zabezpečuje bezpečnú synchronizáciu uvoľnenia asynchrónneho
 *              reset signálu pomocou N-stupňového reťazca (predvolene 2 FF).
 *              Reset je vstupne asynchrónny, výstup je synchronný a aktívny v L.
 *
 * @param[in]   STAGES      Počet za sebou radených FF pre synchronizáciu (minimálne 2).
 *
 * @input       clk_i       Hodinový signál cieľovej domény.
 * @input       rst_ni      Asynchrónny reset, aktívny nízky.
 * @output      rst_no      Synchronný reset, aktívny nízky.
 *
 * @example
 *   cdc_reset_synchronizer #( .STAGES(2) ) u_rst_sync (
 *     .clk_i   (clk),
 *     .rst_ni  (async_rst_n),
 *     .rst_no  (sync_rst_n)
 *   );
 */

`default_nettype none

`ifndef CDC_RESET_SYNCHRONIZER_SV
`define CDC_RESET_SYNCHRONIZER_SV

module cdc_reset_synchronizer #(
    parameter int unsigned STAGES = 2
)(
    input  logic clk_i,
    input  logic rst_ni,
    output logic rst_no
);

  // ============================================
  //   Kontrola parametrov
  // ============================================
  initial begin
    if (STAGES < 2)
      $fatal("cdc_reset_synchronizer: STAGES must be >= 2");
  end

  // ============================================
  //   Synchronizačný reťazec
  // ============================================
  (* altera_attribute = "-name SYNCHRONIZER_IDENTIFICATION FORCED_IF_ASYNCHRONOUS" *)
  logic [STAGES-1:0] rst_sync_q;

  // ============================================
  //   Dvoj-/viac-stupňový synchronizátor resetu
  // ============================================
  always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
      rst_sync_q <= '0;     // Resetujeme na "všetko 0" => výstupný reset aktívny
    end else begin
      rst_sync_q[0] <= 1'b1;
      rst_sync_q[STAGES-1:1] <= rst_sync_q[STAGES-2:0];
    end
  end

  // Výstupný synchronný reset (aktívny LOW)
  assign rst_no = rst_sync_q[STAGES-1];

endmodule

`endif // CDC_RESET_SYNCHRONIZER_SV

`default_nettype wire
