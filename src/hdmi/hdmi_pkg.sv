`ifndef HDMI_PACKAGE
`define HDMI_PACKAGE

`default_nettype none

package hdmi_pkg;

`ifndef RGB888_T_DEFINED
`define RGB888_T_DEFINED
    /** @brief Dátový typ pre jeden pixel vo formáte RGB888 (24 bitov). */
  typedef struct packed {
    logic [7:0] red; ///< @brief 8 bitov pre červenú zložku.
    logic [7:0] grn; ///< @brief 8 bitov pre zelenú zložku.
    logic [7:0] blu; ///< @brief 8 bitov pre modrú zložku.
  } rgb888_t;
`endif

    // Dátový typ pre 10-bitové TMDS dáta (jeden kanál)
    typedef logic [9:0] tmds_word_t;

    typedef logic [7:0] tmds_data_t;

    // Pole pre všetky 4 TMDS kanály (B, G, R, CLK)
    typedef tmds_word_t tmds_channel_data_t[0:3];

    // Typ periódy pre lepšiu čitateľnosť a bezpečnosť kódu (prevzaté z V1)
    typedef enum logic [1:0] {
      VIDEO_PERIOD,   // 00: Aktívne video dáta
      CONTROL_PERIOD, // 01: Riadiace symboly (HSync/VSync)
      AUDIO_PERIOD,   // 10: Perióda pre audio dáta (tu kódujeme len Guard Band)
      DATA_PERIOD     // 11: Perióda pre InfoFrame dáta (tu kódujeme len Guard Band)
    } tmds_period_e;

endpackage : hdmi_pkg

`endif
