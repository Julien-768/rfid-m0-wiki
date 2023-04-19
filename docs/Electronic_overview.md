# Overview

## Schematic of the system

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/rfid.elec.schematic/General_schematic.png">
<img src="../assets/images/rfid.elec.schematic/General_schematic.png" width="600">
</a>
<!-- markdownlint-enable MD033 -->

## Main board

The main board performs most of the system's functions :

* Sensor reading
* Data recording
* Time / Date management
* Security management (temperature and battery monitoring)

This board is **3.3V-logic level and powered in 5V** by one associated power board.

## Power board

The power board ensures the power and battery management to create a 5V.  
Some components are plugged into it :

* The SWITCH button that **connect / disconnect the battery** to the power board
* The START button that permits the user to **safely switch On / Off** the system
* An optional solar panel to reload the battery

A 3-wire cable connect the main board to the power board :

* EN : This line permits the main board to pilot the power supply (self-hold function)
* SW : This line allow the main board to read the START button status (pressed / released)
* VBAT : Battery voltage compatible with 3.3V-logic level

To be compatible with different battery technologies, two power board are available :

* [5V power supply board](./Power-5V.md) to use Li-Po or Li-Ion battery. A reload by USB-C or an optional solar panel is also possible.
* [12V power supply board](./Power-12V.md) to use lead-battery from 9V to 18V.
