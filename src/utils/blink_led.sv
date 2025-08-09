/**
 * @brief       Jednoduchý modul na blikanie LED s nastaviteľnou frekvenciou.
 * @details     Modul generuje signál pre LED, ktorá bliká so zadanou frekvenciou
 *              na základe vstupného hodinového signálu. Počet taktov na jednu polperiódu
 *              sa vypočíta z parametrov `CLOCK_FREQ_HZ` a `BLINK_HZ`.
 *
 * @param[in]   CLOCK_FREQ_HZ  Frekvencia vstupného hodinového signálu v Hz (predvolené 50 MHz).
 * @param[in]   BLINK_HZ       Požadovaná frekvencia blikania LED v Hz (predvolené 1 Hz).
 *
 * @input       clk_i          Vstupný hodinový signál.
 * @input       rst_ni         Aktívny nízky synchronný reset.
 * @output      led_o          Výstupný signál pre LED (blikajúci).
 *
 * @example
 * blink_led #(
 *   .CLOCK_FREQ_HZ(50_000_000),
 *   .BLINK_HZ(2)
 * ) u_blink_led (
 *   .clk_i(clk),
 *   .rst_ni(rst_n),
 *   .led_o(led)
 * );
 */


`ifndef BLINK_LED_SV
`define BLINK_LED_SV

`default_nettype none

module blink_led #(
  parameter int CLOCK_FREQ_HZ = 50_000_000,  // predvolená frekvencia hodinového signálu
  parameter int BLINK_HZ      = 1            // frekvencia blikania LED v Hz
)(
  input  wire logic clk_i,
  input  wire logic rst_ni,  // Synchrónny reset aktívny v L
  output logic      led_o
);

  // divider = počet taktov pre jeden polperiódu blikania
  localparam int BlinkDivider = (CLOCK_FREQ_HZ == 0) ? 1 : CLOCK_FREQ_HZ / (2 * BLINK_HZ);
  localparam int CounterWidth = $clog2(BlinkDivider);
  
  logic [CounterWidth-1:0] counter;

  always_ff @(posedge clk_i) begin
    if (!rst_ni) begin
      counter <= 0;
      led_o <= 1'b0;
    end else if (counter == BlinkDivider - 1) begin
      counter <= 0;
      led_o <= ~led_o;
    end else begin
      counter <= counter + CounterWidth'(1);
    end
  end

endmodule

`endif    // BLINK_LED_SV
