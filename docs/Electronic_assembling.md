# Electronic

This page describes how to prepare the three electronic boards required by the device.

Firstly a main board is assembled to receive the different components and connectors. Secondly, some terminal blocks are added to the RFID board in order to be easily connected with the other boards. Finally, a power board is assembled according to the choice of battery (5v or 12v battery).

## Step 1 : Prepare the main board

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
* Insert the CR1220 battery the corresponding slot of the RTC module
* Insert a microSD card in the corresponding slot of the SD module

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/Final_assembling.jpg">
<img src="../assets/images/Main_board/Final_assembling.jpg" alt="Main board final_assembling" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 2 : Prepare the Tectus RFID reader

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

* Prepare the Powerboost and the Universal charger by assembling them
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
<a href="../assets/images/Power_board/5v_powerSupp.jpg">
<img src="../assets/images/Power_board/5v_powerSupp.jpg" alt="5v power supply" width="500" >
</a>
<!-- markdownlint-enable MD033 -->

### 12V power supply board

* Weld the SMD resistors on the underside of the PCB
  
<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/12v_powerSupp_SMD.jpg">
<img src="../assets/images/Power_board/12v_powerSupp_SMD.jpg" alt="12v power supply with SMD" width="500" >
</a>
<!-- markdownlint-enable MD033 -->

* Weld the screw terminal blocks 2.54mm pitch on the upper side of the PCB
* Weld the 5V DC-to-DC converter
* Add the two 2 ways screw terminal block 5.08mm pitch
* Weld the two power MOSFET : N channel on the low-side
* On the underside  side of the PCB, cut the pins that protrude

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/12v_powerSupp.jpg">
<img src="../assets/images/Power_board/12v_powerSupp.jpg" alt="12v power supply" width="500" >
</a>
<!-- markdownlint-enable MD033 -->
