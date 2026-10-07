# Technical specifications

## Memory

The system stores its data on a Micro-SD card.

- The maximal supported size is 32GB ([SD and SDHC](https://www.arduino.cc/reference/en/libraries/sd/) card supported).
- For example, a 2GB SD card can record ~5,100,000,000 detections with tags (**~59 continuous days** with one detection per second).

## Powering

Several powering options are proposed :

- Lithium powered
  - 3.6V 20Ah 72Wh Li-ion battery (Weight ~0.3kg - Cost ~80€ )
  - 3.6V 20Ah 72Wh Li-ion battery (Weight ~0.3kg - Cost ~80€ ) + a solar panel

- Lead powered
  - 12V 5.4Ah 64.8Wh Lead battery (Weight ~1.7kg - Cost ~40€ ), for rodent device

## Consumption & Autonomy

For details about components consumption and autonomy calculation, refers to the [calculation sheet](./assets/images/User_description/Consumption_and_autonomy.xlsx).

### Autonomy

The autonomy varies according to the software configuration. Here is the autonomy measured with a 65 Wh battery

| System configuration                |  Autonomy  | Equivalent consumption [W.h] | Equivalent consumption per day |
| ----------------------------------- | :--------: | :--------------------------: | :----------------------------: |
| IR On - RFID (On) (1) - 12/24h mode | 17d 7h 9m  |           0.16 W.h           |            3.8 /day            |
| IR On - RFID (On) (1) - 24/24h mode | 10d 22h 9m |           0.25 W.h           |            6 W/day             |
| IR Off - RFID On - 12/24h mode      | 9d 8h 37m  |           0.29 W.h           |            7 W/day             |
| IR Off - RFID On - 24/24h mode      | 5d 6h 34m  |           0.52 W.h           |           12.5 W/day           |

??? note "RFID (On)"

      RFID triggered by infrared sensors

??? note Assomptions made for autonomy estimation

    - 50 detections with RFID tag per hour
    - One detection = 5 seconds in front of sensor, including 1 second to read the RFID tag
    - a 64.8Wh 12V 5.4 A.h Lead battery (more pessimistic situation)
    - T = 20°c

Some notions have to be kept in mind :

- There is no consumption difference if one or two IR sensors are active. In both cases, the two emitters & receivers are powered
- If the two IR sensors are inactive, the RFID is always in research mode (IR Off - RFID On) except during sleep mode
- If the temperature sensor is active, the IR receiver modules are powered even if opt_IR_1 & opt_IR_2 are False (same power supply)
- During sleep mode, only the microcontroler and the Real Time Clock are powered

### Component consumption

| Board           | Component                    |   Mode   | Power consumption [mW] |
| --------------- | ---------------------------- | :------: | :--------------------: |
| Power board 5V  | Power board                  |    -     |           43           |
| Power board 12V | Power board                  |    -     |          112           |
| Main board      | Feather (including SD) + RTC |    -     |           65           |
| Main board      | RFID reader & antenna        | Standby  |           80           |
| Main board      | RFID reader & antenna        | Research |          450           |
| Main board      | RFID reader & antenna        | Reading  |          232           |
| Main board      | 1 IR Emitting Diode          |    -     |          15.8          |
| Main board      | 1 IR receiver module         |    -     |          1.3           |
| Main board      | + 3.3V regulator             |    -     |           45           |

The consumptions are measured for T = 20°c.

The IR Emitting Diode is considered with 220 Ohm resistor and 50% PWM duty cycle.

**Be careful to the SD card consumption** : Its consumption can vary from 1 et 10mA according to the manufacturer and the production batch.

### Rodent device dimensions

The system is designed to be integrated into a [1150 hard case Pelicase](https://www.peli.com/eu/fr/product/cases/protector/1150) (240 x 198 x 109 mm).

<a href="../assets/images/User_description/1150_pelicase.jpg">
<img src="../assets/images/User_description/1150_pelicase.jpg" alt= "1150 Pelicase" width="350">
</a>

The operating tempererature range is 0°c to 50°c.

<!-- | System configuration                | Consumption [W.h] |  Autonomy  |
| ----------------------------------- | :---------------: | :--------: |
| I---------------------------------e | 3---------------7 | 1--------m |
| IR On - RFID (On) (1) - 24/24h mode | 5.9               | 10d 22h 9m |
| IR Off - RFID On - 12/24h mode      | 6.9               | 9d 8h 37m  |
| IR Off - RFID On - 24/24h mode      | 12.3              | 5d 6h 34m  | -->
