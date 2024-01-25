# Electronic

This page describes how to prepare the three electronic boards required by the device.

Firstly a main board is assembled to receive the different components and connectors. Secondly, some terminal blocks are added to the RFID board in order to be easily connected with the other boards. Finally, a power board is assembled according to the choice of battery (5v or 12v battery).

Optionally, a multiplex board can be assembled in order to connect two antennas to the main board.

## Step 1 : Prepare the main board

- Weld the different screw terminal blocks into the board, as the two JST connectors
- Add the RTC module : Ensure to **mount the coin cell battery on the top side**
- Add the Feather M0
- (Optionally) Add the temperature sensor
- Insert the CR1220 battery the corresponding slot of the RTC module
- Insert a microSD card in the corresponding slot of the SD module

<a href="../assets/images/Main_board/Final_assembling.jpg">
<img src="../assets/images/Main_board/Final_assembling.jpg" alt="Main board final_assembling" width="500" >
</a>

## Step 2 : Prepare the Tectus RFID reader

- Weld a 2 ways screw terminal block on the right extremity of the RFID board
- Weld a 2 ways screw terminal block on the bottom holes of the RFID board
- Weld a 4 ways screw terminal block on the top left holes of the RFID board

<a href="../assets/images/RFID/RFID_board.jpg">
<img src="../assets/images/RFID/RFID_board.jpg" alt="RFID board with connectors" width="500" >
</a>

## Step 3 : Prepare a power-supply board

According to the power supply available, two different boards can be prepared :

### 5V power supply board

- Prepare the Powerboost and the Universal charger by assembling them
- Weld the Powerboost
- Weld the Universal charger
- Add the different screw terminal blocks
- Complete the power board by adding the 1000µF capacitor (not represented in the picture)

<a href="../assets/images/Power_board/5v_powerSupp.jpg">
<img src="../assets/images/Power_board/5v_powerSupp.jpg" alt="5v power supply" width="500" >
</a>

### 12V power supply board

- Weld the screw terminal blocks
- Weld the 5V DC-to-DC converter

<a href="../assets/images/Power_board/12v_powerSupp.jpg">
<img src="../assets/images/Power_board/12v_powerSupp.jpg" alt="12v power supply" width="500" >
</a>

## Step 4 (optional) : Prepare a multiplex board

- Weld the screw terminal blocks : 3 x 8 screw and 1 x 3 screws
- Add the 5v DC-to-DC converters (not represented in the picture)

<a href="../assets/images/Multiplex_board/Multiplex_board.jpg">
<img src="../assets/images/Multiplex_board/Multiplex_board.jpg" alt="multiplex board" width="500" >
</a>
