# Dokumentácia modulov

## 🔧 Zoznam

| Názov modulu | Popis | Zdrojový súbor |
|--------------|--------|----------------|
| [axis_checker_generator](modules/axis/axis_checker_generator.md) | - | [axis/axis_checker_generator.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_checker_generator.sv) |
| [axis_frame_streamer](modules/axis/axis_frame_streamer.md) | AXI4-Stream Frame Streamer generujúci súradnice pixelov. | [axis/axis_frame_streamer.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_frame_streamer.sv) |
| [axis_gradient_generator](modules/axis/axis_gradient_generator.md) | - | [axis/axis_gradient_generator.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_gradient_generator.sv) |
| [axis_to_vga](modules/axis/axis_to_vga.md) | Premosťuje AXI4-Stream dáta na paralelný VGA výstup. | [axis/axis_to_vga.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_to_vga.sv) |
| [blink_led](modules/utils/blink_led.md) | Jednoduchý modul na blikanie LED s nastaviteľnou frekvenciou. | [utils/blink_led.sv](https://github.com/risapav/fpga_common/blob/main/src/utils/blink_led.sv) |
| [cdc_async_fifo](modules/cdc/cdc_async_fifo.md) | Asynchrónny FIFO buffer s oddelenými hodinovými doménami pre zápis a čítanie. | [cdc/cdc_async_fifo.sv](https://github.com/risapav/fpga_common/blob/main/src/cdc/cdc_async_fifo.sv) |
| [cdc_reset_synchronizer](modules/cdc/cdc_reset_synchronizer.md) | Synchronizátor asynchrónneho resetu pre cieľovú hodinovú doménu. | [cdc/cdc_reset_synchronizer.sv](https://github.com/risapav/fpga_common/blob/main/src/cdc/cdc_reset_synchronizer.sv) |
| [cdc_two_flop_synchronizer](modules/cdc/cdc_two_flop_synchronizer.md) | Dvojstupňový synchronizátor signálu pre CDC (Clock Domain Crossing). | [cdc/cdc_two_flop_synchronizer.sv](https://github.com/risapav/fpga_common/blob/main/src/cdc/cdc_two_flop_synchronizer.sv) |
| [CheckerPattern](modules/axis/CheckerPattern.md) | AXI4-Stream generátor šachovnicového vzoru (checkerboard pattern) | [axis/axis_checker_generator.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_checker_generator.sv) |
| [generic_serializer](modules/hdmi/generic_serializer.md) | Generický, parametrizovateľný N-kanálový serializátor so synchronizovaným CDC a voliteľným DDR/SDR režimom. | [hdmi/generic_serializer.sv](https://github.com/risapav/fpga_common/blob/main/src/hdmi/generic_serializer.sv) |
| [GradientPattern](modules/axis/GradientPattern.md) | Generuje AXI4-Stream výstup s farebným gradientom. | [axis/axis_gradient_generator.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_gradient_generator.sv) |
| [hdmi_tx_top](modules/hdmi/hdmi_tx_top.md) | Hlavný modul digitálneho HDMI vysielača. | [hdmi/hdmi_tx_top.sv](https://github.com/risapav/fpga_common/blob/main/src/hdmi/hdmi_tx_top.sv) |
| [infoframe_builder](modules/hdmi/infoframe_builder.md) | Kombinačný modul na stavbu štruktúry HDMI InfoFrame paketov. | [hdmi/infoframe_builder.sv](https://github.com/risapav/fpga_common/blob/main/src/hdmi/infoframe_builder.sv) |
| [my_axi_peripheral](modules/axi/my_axi_peripheral.md) | Definície AXI rozhraní (AXI4, AXI4-Lite, AXI4-Stream) pre použitie v SoC dizajne. | [axi/axi_interfaces.sv](https://github.com/risapav/fpga_common/blob/main/src/axi/axi_interfaces.sv) |
| [packet_streamer](modules/hdmi/packet_streamer.md) | Sekvenčný modul (FSM) pre serializáciu a multiplexovanie viacerých HDMI paketov. | [hdmi/packet_streamer.sv](https://github.com/risapav/fpga_common/blob/main/src/hdmi/packet_streamer.sv) |
| [picture_gen](modules/picture/picture_gen.md) | Generátor testovacích obrazcov pre VGA výstup. | [picture/picture_gen.sv](https://github.com/risapav/fpga_common/blob/main/src/picture/picture_gen.sv) |
| [rgb565_to_rgb888](modules/vga/rgb565_to_rgb888.md) | Kombinačný modul, ktorý konvertuje 16-bitovú farbu vo formáte RGB565 na 24-bitovú farbu vo formáte RGB888. | [vga/rgb565_to_rgb888.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/rgb565_to_rgb888.sv) |
| [seven_seg_mux](modules/utils/seven_seg_mux.md) | Modul pre multiplexovanie 7-segmentového displeja. | [utils/seven_seg_mux.sv](https://github.com/risapav/fpga_common/blob/main/src/utils/seven_seg_mux.sv) |
| [tmds_encoder_pipelined](modules/hdmi/tmds_encoder_pipelined.md) | TMDS enkodér pre HDMI s 3-stupňovou pipeline a DC-balancom. | [hdmi/tmds_encoder_pipelined.sv](https://github.com/risapav/fpga_common/blob/main/src/hdmi/tmds_encoder_pipelined.sv) |
| [vga_ctrl](modules/vga/vga_ctrl.md) | VGA kontrolér pre výstup RGB signálu a synchronizačných impulzov | [vga/vga_ctrl.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_ctrl.sv) |
| [vga_line](modules/vga/vga_line.md) | Generátor jednej časovej periódy VGA signálu | [vga/vga_line.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_line.sv) |
| [vga_pixel_xy](modules/vga/vga_pixel_xy.md) | Generátor VGA súradníc pixelov (X, Y) | [vga/vga_pixel_xy.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_pixel_xy.sv) |
| [vga_timing](modules/vga/vga_timing.md) | VGA generátor časovania | [vga/vga_timing.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_timing.sv) |
