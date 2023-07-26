# Technical specifications

The system is designed to be integrated into a [1150 hard case Pelicase](https://www.peli.com/eu/fr/product/cases/protector/1150) (240 x 198 x 109 mm).

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/User_description/1150_pelicase.jpg">
<img src="../assets/images/User_description/1150_pelicase.jpg" alt= "1150 Pelicase" width="350">
</a>
<!-- markdownlint-enable MD033 -->

The operating tempererature range is 0°c to 50°c.

## Memory

The system stores its data on a Micro-SD card. The maximal supported size is 32GB ([SD and SDHC](https://www.arduino.cc/reference/en/libraries/sd/) card supported).

A 2GB SD card can record ~5,100,000,000 detections with tags (**~59 continuous days** with one detection per second).

## Powering

Several powering options are proposed :

* Lithium powered :
    * A 3.6V 20Ah 72Wh Li-ion battery
    * A 3.6V 20Ah 72Wh Li-ion battery equipped with solar panel

    Weight ~0.3kg - Cost ~80€ usually  
    This battery is required to be powered by solar panels.

* Lead powered : A 12V 5.4Ah 64.8Wh Lead battery

    Weight ~1.7kg - Cost ~40€ usually  
    This battery technology is quite common and easy to reload / transport.

## Consumption & Autonomy

For details about components consumption and autonomy calculation, refers to the [calculation sheet](./assets/images/User_description/Consumption_and_autonomy.xlsx).

### System consumption & autonomy

The autonomy of the system depends of its consumption, that varies according to the software configuration.

| System configuration                     |  Consumption [W.h]               | Autonomy              |
|------------------------------------------|:--------------------------------:|:---------------------:|
| IR On - RFID (On) - 12/24h mode          | 3.7                              | 17d 7h 9m             |
| IR On - RFID (On) - 24/24h mode          | 5.9                              | 10d 22h 9m            |
| IR Off - RFID On - 12/24h mode           | 6.9                              | 9d 8h 37m             |
| IR Off - RFID On - 24/24h mode           | 12.3                             | 5d 6h 34m             |

*(On) : RFID triggered by infrared sensors*

The autonomies are indicated considering :

* 50 detections with RFID tag per hour
* One detection = 5 seconds in front of sensor, incluging 1 second to read the RFID tag
* a 12V 5.4 A.h Lead battery (more pessimistic situation)
* T = 20°c

Some notions have to be kept in mind :

* There is no consumption difference if one or two IR sensors are active. In both cases, the two emitters & receivers are powered
* If the two IR sensors are inactive, the RFID is always in research mode (except during sleep mode)
* If the temperature sensor is active, the IR receivers are powered even if opt_IR_1 & opt_IR_2 are False (same power supply)
* During sleep mode, only the Feather & the RTC are powered

### Component consumption

| Component                                    | Power consumption [mW]          |
|----------------------------------------------|:-------------------------------:|
| 5V power board                               | 43                              |
| 12V power board                              | 112                             |
| Feather (including SD) + RTC                 | 65                              |
| RFID reader & antenna - Standby              | 80                              |
| RFID reader & antenna - Research             | 450                             |
| RFID reader & antenna - Reading              | 232                             |
| 1 IR Emitter                                 | 15.8                            |
| 1 IR Receiver                                | 1.3                             |
| + 3.3V regulator                             | 45                              |

The consumptions are measured for T = 20°c.

The IR emitter is considered with 220 Ohm resistor and 50% PWM duty cycle.

**Be careful to the SD card consumption** : Its consumption can vary from 1 et 10mA according to the manufacturer and the production batch.
