# Li-Po / Li-Ion battery power supply board

This page describes the 5v power board, used to connect a 3.6v Li-Ion or 3.7v Li-Po battery to the device.

## Schematic of the system

<a href="../assets/images/Manufacturing/5V_board_schema.svg">
<img alt="Kicad schematic of 5V power board" src="../assets/images/Manufacturing/5V_board_schema.svg" width="600">
</a>

## Materials

### Power Boost

<a href="../assets/images/Power_board/5v_PowerBoost.png">
<img alt="snapshot of the Power Boost 1000 board" src="../assets/images/Power_board/5v_PowerBoost.png" width="300">
</a>

The Power Boost 1000 provides a 5V output voltage from an input voltage that can varies from **1.8V to 5.5V**. It can deliver **1A max**.
This component allow to use a battery, whose voltage varies with the state of the charge, as a power source for our device. The EN pin is used to safely switch On / Off the system.

More information in the [Adafruit tutorial](https://learn.adafruit.com/adafruit-powerboost-1000-basic) and in the [component datasheet](https://www.ti.com/product/TPS61090).

### Solar charger

<a href="../assets/images/Power_board/5v_SolarCharger.png">
<img alt="snapshot of the BQ24074 solar charger board" src="../assets/images/Power_board/5v_SolarCharger.png" width="300">
</a>

The BQ24074 board allow to manage the charge of a 3.7V Li-Po or 3.6V Li-Ion battery from a solar panel (MPTT solar charge), a DC charger or an USB port. When the solar panel is sunny enough, it powers the system directly to prevent battery from constantly charging/discharging.
The output voltage can fluctuate from **3.7V to 5V** and it can deliver **1.5A max**. Use a **5-10V solar panel** with this power board.

More information in the [Adafruit tutorial](https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout/overview)

### Solar panel

This 130 x 150 mm solar panel has a power of 2.5W It can deliver 500 mA for a nominal voltage of 5V.

<a href="../assets/images/Power_board/5v_SolarPanel.png">
<img alt="snapshot a 2.5W 5V solar panel" src="../assets/images/Power_board/5v_SolarPanel.png" width="300">
</a>

### Battery

The battery used is a Lithium-ion battery 3.6V. Its nominal voltage can reach 4.2V when fully charged. **Do not unload below 3V.**
During usage, ensure that the temperature is between **0°c to 50°c**.

<a href="../assets/images/Power_board/5v_battery.jpg">
<img alt="snapshot of a Li-ion battery" src="../assets/images/Power_board/5v_battery.jpg" width="300">
</a>
