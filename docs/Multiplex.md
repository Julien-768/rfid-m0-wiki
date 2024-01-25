# Multiplex board

This page describes the multiplex board in charge to connect two antennas to the main board.

## Schematic of the system

<a href="../assets/images/Manufacturing/Multiplex_board_schema.svg">
<img alt="schematic of the multiplex board" src="../assets/images/Manufacturing/Multiplex_board_schema.svg" width="600">
</a>

## Materials

### CMOS Analog Switch

<a href="../assets/images/Multiplex_board/AnalogSwitch.png">
<img alt"snapshot of the component PI5A100 analog switch" src="../assets/images/Multiplex_board/AnalogSwitch.png" width="100">
</a>

The PI5A100 analog switch allows to multiplex four digital signals up to 5V and 30mA per channel with a 230MHz of bandwith for a low consumption (~10mA).

### Power MOSFET

<a href="../assets/images/Multiplex_board/PowerMosfet.png">
<img alt"snapshot of the component IRF540" src="../assets/images/Multiplex_board/PowerMosfet.png" width="100">
</a>

The IRF540 Mosfet are used to switch the RFID antennas. It accepts signals up to 100V and 33A, while ensuring a low-resistance (~50mOhm) to limit its impact on the RFID antenna range.
