# Li-Po / Li-Ion battery power supply board

This page describes the 5v power board, used to connect a 3.6v Li-Ion or 3.7v Li-Po battery to the device.

## Schematic of the system

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Manufacturing/5V_board_schema.svg">
<img src="../assets/images/Manufacturing/5V_board_schema.svg" width="600">
</a>
<!-- markdownlint-enable MD033 -->

## Materials

### Power Boost

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/5v_PowerBoost.png">
<img src="../assets/images/Power_board/5v_PowerBoost.png" width="300">
</a>
<!-- markdownlint-enable MD033 -->

The Power Boost 1000 provides a 5V output voltage from an input voltage that can varies from **1.8V to 5.5V**. It can deliver **1A max**.  
This component allow to use a battery, whose voltage varies with the state of the charge, as a power source for our device. The EN pin is used to safely switch On / Off the system.

More information in the [Adafruit tutorial](https://learn.adafruit.com/adafruit-powerboost-1000-basic) and in the [component datasheet](https://www.ti.com/product/TPS61090).

### Solar charger

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/5v_SolarCharger.png">
<img src="../assets/images/Power_board/5v_SolarCharger.png" width="300">
</a>
<!-- markdownlint-enable MD033 -->

The BQ24074 board allow to manage the charge of a 3.7V Li-Po or 3.6V Li-Ion battery from a solar panel (MPTT solar charge), a DC charger or an USB port. When the solar panel is sunny enough, it powers the system directly to prevent battery from constantly charging/discharging.
The output voltage can fluctuate from **3.7V to 5V** and it can deliver **1.5A max**.  

More information in the [Adafruit tutorial](https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout/overview)

### Solar panel

This 130 x 150 mm solar panel has a power of 2.5W It can deliver 500 mA for a nominal voltage of 5V.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/5v_SolarPanel.png">
<img src="../assets/images/Power_board/5v_SolarPanel.png" width="300">
</a>
<!-- markdownlint-enable MD033 -->

### Battery

The battery used is a Lithium-ion battery 3.6V 20Ah. Its nominal voltage can reach 4.2V when fully charged. **Do not unload below 3V.**  
During usage, ensure that the temperature is between **0°c to 50°c**.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/5v_battery.jpg">
<img src="../assets/images/Power_board/5v_battery.jpg" width="300">
</a>
<!-- markdownlint-enable MD033 -->
