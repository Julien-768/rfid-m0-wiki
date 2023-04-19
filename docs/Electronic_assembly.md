# Electronic

Three boards have to be prepared :

* The main board
* The Tectus RFID reader
* A power-supply board : 5V or 12V

## Step 1 : Prepare the main board

|#| Description                    | Designation                                           | Quantity  | Dealer         | Reference       |
|-|--------------------------------|-------------------------------------------------------|-----------|----------------|-----------------|
|1| Main board                     | PCB of the main board                                 | 1         | -              | -               |
|2| Feather M0                     | Adafruit Feather M0 Adalogger                         | 1         | Mouser         | 485-2796        |
|3| RTC module                     | Adafruit DS3231 Precision RTC Breakout                | 1         | Mouser         | 485-3013        |
|4| Temperature sensor (optional)  | Adafruit MAX31865 RTD PT100 or PT1000 Amplifier       | 1         | Mouser         | 485-3328        |
|5| 2 ways screw terminal block    | Wire-To-Board Terminal Block, 2.54 mm, 2 Ways         | 2         | Farnell        | MP008513        |
|6| 3 ways screw terminal block    | Wire-To-Board Terminal Block, 2.54 mm, 3 Ways         | 2         | Farnell        | MP008514        |
|7| 4 ways screw terminal block    | Wire-To-Board Terminal Block, 2.54 mm, 4 Ways         | 1         | Farnell        | MP008515        |
|8| 8 ways screw terminal block    | Wire-To-Board Terminal Block, 2.54 mm, 8 Ways         | 1         | Farnell        | MP008517        |
|9| 2 ways JST XH connector        | JST XH angled male connector, 2.5mm, 2 ways           | 1         | Gotronic       | 49196           |
|10| 3 ways JST XH connector       | JST XH angled male connector + 15 cable, 2mm, 3 ways  | 1         | Gotronic       | 48917           |
|11| Resistor R5                   | 100 Ohm resistor 0.25W +5%                            | 1         | RS-Pro         | 707-7587        |
|12| Resistor R7 & R8              | 220 Ohm resistor 0.25W +5%                            | 2         | RS-Pro         | 707-7612        |
|11| Resistor R9                   | 270 Ohm resistor 0.25W +5%                            | 1         | RS-Pro         | 707-7625        |
|14| Capacitor C1                  | Electrolytic Capacitor 1000 µF 10 V                   | 1         | RS-Pro         | 526-1115        |
|15| Capacitor C2 & C3             | Electrolytic Capacitor 10 µF 25 V                     | 2         | RS-Pro         | 181-5401        |
|16| Mofset Q9 & Q10               | Power MOSFET N Channel 60 V 600 mA                    | 2         | RS-Pro         | 823-1827        |
|17| Power Mofset                  | Power MOSFET N Channel 55 V 41 A                      | 2         | RS-Pro         | 541-0086        |
|18| 3.3V voltage regulator        | Fixed LDO Voltage Regulator 3.3Vout 1A                | 1         | RS-Pro         | 5339498         |

* Weld the different screw terminal blocks into the board, as the two JST connectors
* Weld the Q9 and Q10 transistors and the resistors R5, R7, R8, R9
* Add the capacitors C1, C2, C3. Be careful to let enough length to be able to fold the components.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/Capacitor_mouting.jpg">
<img src="../assets/images/Main_board/Capacitor_mouting.jpg" alt="Main board with capacitors" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Weld the 3.3V voltage regulator and the two power MOSFET. Be careful to let enough length to be able to fold the components. The Q13 Mosfet has to be bent forward to not interfere with the USB port.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/MOSFET_mouting.jpg">
<img src="../assets/images/Main_board/MOSFET_mouting.jpg" alt="Main board with MOSFET" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Add the RTC module and then the Feather M0
* (Optionally) Add the temperature sensor

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/Final_assembly.jpg">
<img src="../assets/images/Main_board/Final_assembly.jpg" alt="Main board final_assembly" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 2 : Prepare the Tectus RFID reader

|#| Description                    | Designation                                             | Quantity  | Dealer         | Reference       |
|-|--------------------------------|---------------------------------------------------------|-----------|----------------|-----------------|
|1| RFID board                     | Tectus RFID Reader Industry OEM Board Titan TLB-30-SER  | 1         | Tectus         | 4004-01-000-00  |
|2| 2 ways screw terminal block    | Wire-To-Board Terminal Block, 2.54 mm, 2 Ways           | 2         | Farnell        | MP008513        |
|3| 4 ways screw terminal block    | Wire-To-Board Terminal Block, 2.54 mm, 4 Ways           | 1         | Tectus         | MP008515        |

* Weld a 2 ways screw terminal block on the right extremity of the RFID board
* Weld a 2 ways screw terminal block on the bottom holes of the RFID board
* Weld a 4 ways screw terminal block on the top left holes of the RFID board

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/RFID/RFID_board.jpg">
<img src="../assets/images/RFID/RFID_board.jpg" alt="RFID board with connectors" width="500" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 3 : Prepare a power-supply board

According to the power supply available, two different boards can be prepared :

### 5V power supply board

|#| Description                        | Designation                                           | Quantity  | Dealer         | Reference         |
|-|------------------------------------|-------------------------------------------------------|-----------|----------------|-------------------|
|1| 12V board                          | PCB of the 5V power supply board                      | 1         | -              | -                 |
|2| Powerboost                         | Adafruit Powerboost 1000 Basic                        | 1         | Mouser         | 485-2030          |
|3| Universal charger                  | Adafruit Universal charger bq24074                    | 1         | Mouser         | 485-4755          |
|4| 2 ways screw terminal block        | Wire-To-Board Terminal Block, 2.54 mm, 2 Ways         | 2         | Farnell        | MP008513          |
|5| 3 ways screw terminal block        | Wire-To-Board Terminal Block, 2.54 mm, 3 Ways         | 1         | Farnell        | MP008514          |
|6| Capacitor C2 & C3                  | Ceramic Capacitor 0.1 µF 50 V Radial 5.08 mm          | 2         | RS-Pro         | 699-4891          |
|7| Capacitor C4                       | Electrolytic Capacitor 1000 µF 10 V                   | 1         | RS-Pro         | 526-1115          |
|8| 1N4001 diode                       | Recovery diode 50V 1A                                 | 2         | RS-Pro         | 628-8931          |
|9| SMD resistor 10k                   | SMD resistor 10 kOhm 250mW 1206                       | 1         | Mouser         | CR1206-FX-1002ELF |
|10| SMD resistor 47k                  | SMD resistor 47 kOhm 250mW 1206                       | 1         | Mouser         | CR1206-FX-4702ELF |
|11| SMD resistor 100k                 | SMD resistor 100 kOhm 250mW 1206                      | 4         | Mouser         | CR1206-FX-1003ELF |

* Weld the SMD resistors on the underside of the PCB
* Weld the C2 capacitor on the underside of the PCB.
* Weld the two 1N4001 diodes on the upper side of the PCB
* Weld the C3 capacitor by ensuring to not interfere withe the Powerboost location
* Weld the C4 capacitor. Ensure to let enough length to be able to fold the components.
* Add the three screw terminal blocks
* Weld the Powerboost
* Weld the Universal charger by ensuring there is no contact with the C2 capacitor pins
* On the underside  side of the PCB, cut the pins that protrude

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_Board/5v_powerSupp.jpg">
<img src="../assets/images/Power_Board/5v_powerSupp.jpg" alt="5v power supply" width="500" >
</a>
<!-- markdownlint-enable MD033 -->

### 12V power supply board

|#| Description                        | Designation                                           | Quantity  | Dealer         | Reference         |
|-|------------------------------------|-------------------------------------------------------|-----------|----------------|-------------------|
|1| 12V  board                         | PCB of the 12V power supply board                     | 1         | -              | -                 |
|2| SMD resistor 3k                    | SMD resistor 3 kOhm 250mW 1206                        | 1         | Mouser         | CR1206-FX-3001ELF |
|3| SMD resistor 15k                   | SMD resistor 15 kOhm 250mW 1206                       | 1         | Mouser         | CR1206-FX-1502ELF |
|4| SMD resistor 100k                  | SMD resistor 100 kOhm 250mW 1206                      | 4         | Mouser         | CR1206-FX-1003ELF |
|5| 2 ways screw terminal block        | Wire-To-Board Terminal Block, 2.54 mm, 2 Ways         | 3         | Farnell        | MP008513          |
|6| 3 ways screw terminal block        | Wire-To-Board Terminal Block, 2.54 mm, 3 Ways         | 1         | Farnell        | MP008514          |
|7| 2 ways screw terminal block 5.08mm | Wire-To-Board Terminal Block, 5.08 mm, 2 Ways         | 2         | Farnell        | MC000048          |
|8| 5V DC-to-DC converter              | Isolated Through Hole DC/DC Converter 5V 1.2A 6W      | 1         | RS-Pro         | 122-8157          |
|9| Power Mofset N channel Q2          | Power MOSFET N Channel 55 V 41 A                      | 1         | RS-Pro         | 541-0086          |
|10| Power Mofset P channel Q1         | Power MOSFET P Channel 100 V 6 A                      | 1         | RS-Pro         | 708-5140          |

* Weld the SMD resistors on the underside of the PCB
  
<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_Board/12v_powerSupp_SMD.jpg">
<img src="../assets/images/Power_Board/12v_powerSupp_SMD.jpg" alt="12v power supply with SMD" width="500" >
</a>
<!-- markdownlint-enable MD033 -->

* Weld the screw terminal blocks 2.54mm pitch on the upper side of the PCB
* Weld the 5V DC-to-DC converter
* Add the two 2 ways screw terminal block 5.08mm pitch
* Weld the two power MOSFET : N channel on the low-side
* On the underside  side of the PCB, cut the pins that protrude

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_Board/12v_powerSupp.jpg">
<img src="../assets/images/Power_Board/12v_powerSupp.jpg" alt="12v power supply" width="500" >
</a>
<!-- markdownlint-enable MD033 -->
