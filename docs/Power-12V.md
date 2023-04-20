# Lead-battery power supply board

This page describes the 12v power board, used to connect a 12v lead battery to the device.

## Schematic of the system

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Manufacturing/12V_board_schema.svg">
<img src="../assets/images/Manufacturing/12V_board_schema.svg" width="600">
</a>
<!-- markdownlint-enable MD033 -->

## DC-to-DC converter

The JCE0612S05 DC-to-DC converter provides a 5V output voltage from an input voltage that can varies from **9V to 18V**. It can deliver **1.2A max**.  
This component allow to use a battery, whose voltage varies with the state of the charge, as a power source for our device.  

Thanks to this converter, the power-board is compatible with several type of batteries : More secured, less sensitive to temperature or fire...

For more information, refers to the [component datasheet](https://www.mouser.fr/datasheet/2/942/SF_JCE06-1508846.pdf).

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/12v_DC_DC_converter.png">
<img src="../assets/images/Power_board/12v_DC_DC_converter.png" width="300">
</a>
<!-- markdownlint-enable MD033 -->

### Battery

The battery used is a 12V lead battery. Its nominal voltage can reach 14V when fully charged. **Do not unload below 12V.**  
During usage, ensure that the temperature is between **0°c to 50°c**.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/12v_Battery.jpg">
<img src="../assets/images/Power_board/12v_Battery.jpg" width="250">
</a>
<!-- markdownlint-enable MD033 -->
