# Power management

According to the choice of battery, two different power boards can be used with the device.  
Both boards are physically different but share the same functionnalities.

## Battery voltage measurement

A Li-Po / Li-ion battery voltage can reach 4.2V and a lead-battery 14V. As the Feather M0 do not accept more than 3.3V on its digital inputs, **a voltage divider is required**.  
The division ratio is different on the two power board (3 for a 5v power board / 6 for a 12v power board) according to the mounted resistors, and **has to be indicated into the software**.  

Some capacitors are also added in order to stabilize the reading. In addition, a moving average filter is performed in the software.

The battery voltage is recorded into the SD memory only if it varies by more than 0.1V since the last record.

## Power-off the system

For a long storage, an On / Off switch physically disconnect the system from the battery.  

For a clean power-off, a push-button allow a **controlled power-off** of the system to avoid to corrupt the SD card memory. In addition, the system can also pilot its own power-off in case of overtemperature or low battery voltage.

The method is described into this [tutorial](https://github.com/craic/arduino_power/blob/master/PowerOnPowerOff.md)

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/power_on_power_off_cycle.png">
<img src="../assets/images/Power_board/power_on_power_off_cycle.png">
</a>
<!-- markdownlint-enable MD033 -->
