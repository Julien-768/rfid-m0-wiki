# Multiplex board

This page describes the multiplex board in charge to connect two antennas to the main board.

## Schematic of the system

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Manufacturing/Multiplex_board_schema.svg">
<img src="../assets/images/Manufacturing/Multiplex_board_schema.svg" width="600">
</a>
<!-- markdownlint-enable MD033 -->

## Materials

### CMOS Analog Switch

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Multiplex_board/AnalogSwitch.png">
<img src="../assets/images/Multiplex_board/AnalogSwitch.png" width="100">
</a>
<!-- markdownlint-enable MD033 -->

The PI5A100 analog switch allows to multiplex four digital signals up to 5V and 30mA per channel with a 230MHz of bandwith for a low consumption (~10mA).

### Power MOSFET

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Multiplex_board/PowerMosfet.png">
<img src="../assets/images/Multiplex_board/PowerMosfet.png" width="100">
</a>
<!-- markdownlint-enable MD033 -->

The IRF540 Mosfet are used to switch the RFID antennas. It accepts signals up to 100V and 33A, while ensuring a low-resistance (~50mOhm) to limit its impact on the RFID antenna range.
