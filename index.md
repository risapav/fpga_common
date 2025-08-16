# Dokumentácia modulov

## 🔧 Zoznam

| Názov modulu | Popis | Zdrojový súbor |
|--------------|--------|----------------|
| [axi_interfaces](modules/axi_interfaces.md) | Definície AXI rozhraní (AXI4, AXI4-Lite, AXI4-Stream) pre použitie v SoC dizajne. | [axi_interfaces.sv](https://github.com/risapav/fpga_common/blob/main/src/axi/axi_interfaces.sv) |
| [axi_pkg](modules/axi_pkg.md) | Centrálna konfigurácia AXI-Stream zbernice. | [axi_pkg.sv](https://github.com/risapav/fpga_common/blob/main/src/axi/axi_pkg.sv) |
| [axis_checker_generator](modules/axis_checker_generator.md) | AXI4-Stream generátor šachovnicového vzoru (checkerboard pattern) | [axis_checker_generator.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_checker_generator.sv) |
| [axis_frame_streamer](modules/axis_frame_streamer.md) | AXI4-Stream Frame Streamer generujúci súradnice pixelov. | [axis_frame_streamer.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_frame_streamer.sv) |
| [axis_gradient_generator](modules/axis_gradient_generator.md) | Generuje AXI4-Stream výstup s farebným gradientom. | [axis_gradient_generator.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_gradient_generator.sv) |
| [axis_to_vga](modules/axis_to_vga.md) | Premosťuje AXI4-Stream dáta na paralelný VGA výstup. | [axis_to_vga.sv](https://github.com/risapav/fpga_common/blob/main/src/axis/axis_to_vga.sv) |
| [blink_led](modules/blink_led.md) | Jednoduchý modul na blikanie LED s nastaviteľnou frekvenciou. | [blink_led.sv](https://github.com/risapav/fpga_common/blob/main/src/utils/blink_led.sv) |
| [cdc_async_fifo](modules/cdc_async_fifo.md) | Asynchrónny FIFO buffer s oddelenými hodinovými doménami pre zápis a čítanie. | [cdc_async_fifo.sv](https://github.com/risapav/fpga_common/blob/main/src/cdc/cdc_async_fifo.sv) |
| [cdc_reset_synchronizer](modules/cdc_reset_synchronizer.md) | Synchronizátor asynchrónneho resetu pre cieľovú hodinovú doménu. | [cdc_reset_synchronizer.sv](https://github.com/risapav/fpga_common/blob/main/src/cdc/cdc_reset_synchronizer.sv) |
| [cdc_two_flop_synchronizer](modules/cdc_two_flop_synchronizer.md) | Dvojstupňový synchronizátor signálu pre CDC (Clock Domain Crossing). | [cdc_two_flop_synchronizer.sv](https://github.com/risapav/fpga_common/blob/main/src/cdc/cdc_two_flop_synchronizer.sv) |
| [generic_serializer](modules/generic_serializer.md) | Generický, parametrizovateľný N-kanálový serializátor so synchronizovaným CDC a voliteľným DDR/SDR režimom. | [generic_serializer.sv](https://github.com/risapav/fpga_common/blob/main/src/hdmi/generic_serializer.sv) |
| [picture_gen](modules/picture_gen.md) | Generátor testovacích obrazcov pre VGA výstup. | [picture_gen.sv](https://github.com/risapav/fpga_common/blob/main/src/picture/picture_gen.sv) |
| [rgb565_to_rgb888](modules/rgb565_to_rgb888.md) | Kombinačný modul, ktorý konvertuje 16-bitovú farbu vo formáte RGB565 na 24-bitovú farbu vo formáte RGB888. | [rgb565_to_rgb888.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/rgb565_to_rgb888.sv) |
| [seven_seg_mux](modules/seven_seg_mux.md) | Modul pre multiplexovanie 7-segmentového displeja. | [seven_seg_mux.sv](https://github.com/risapav/fpga_common/blob/main/src/utils/seven_seg_mux.sv) |
| [vga_ctrl](modules/vga_ctrl.md) | VGA kontrolér pre výstup RGB signálu a synchronizačných impulzov | [vga_ctrl.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_ctrl.sv) |
| [vga_line](modules/vga_line.md) | Generátor jednej časovej periódy VGA signálu | [vga_line.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_line.sv) |
| [vga_pixel_xy](modules/vga_pixel_xy.md) | Generátor VGA súradníc pixelov (X, Y) | [vga_pixel_xy.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_pixel_xy.sv) |
| [vga_pkg](modules/vga_pkg.md) | VGA parametre a typy (balíček) | [vga_pkg.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_pkg.sv) |
| [vga_timing](modules/vga_timing.md) | VGA generátor časovania | [vga_timing.sv](https://github.com/risapav/fpga_common/blob/main/src/vga/vga_timing.sv) |
