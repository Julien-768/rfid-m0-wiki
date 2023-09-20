# Final assembling

This page describes how to assemble all the burrow device components into a Pelicase.

Some supports are prepared and then the electronic boards are mounted on it and wired. Finally the equipped supports are installed into the Pelicase and connected to the antenna and the batteries.

To follow these steps, it's required to have already realized a [burrow antenna](Antenna_burrow_assembling.md), all the [electronic boards](Electronic_assembling.md) and a [burrow case](Burrow_case.md).The main board has to **be [programmed](programming.md) and RTC has to be up-to-date**. In addition, the **burrow antenna has to be attached** to the case.

## Step 1 : Prepare the supports

* 3D print the part ["RFID_support.stl"](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_burrow/RFID_support.stl)
* Insert 2 x M2 nuts in the RFID support
* Insert the RFID reader in its support. Be careful to respect the orientation

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/RFID/RFID_wSupport.jpg">
<img src="../assets/images/RFID/RFID_wSupport.jpg" alt="RFID reader in its support" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Prepare the PVC fixation parts ["Lower_support"](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_burrow/Lower_support.pdf) and ["PCB_support"](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_burrow/PCB_support.pdf) according to their drawings
* Screw two angle brackets into the "Support_inf" plate with 4 self-tapping screws M3 x 6

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Lower_support.jpg">
<img src="../assets/images/Burrow_assembling/Lower_support.jpg" alt="Lower support" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 2 : Assembly the PCB support

* Attach the main board on the "Support_PCB" plate using 2 x M2 x 12 screws and M2 nuts into the top holes. Do not tighten
* Position the RFID reader and its support on the back side of the "Support_PCB" plate. The right hole of the RFID support has to be faced the holes of the main board
* Add 1 x M2 x 10 screw into the bottom hole of the main board, through the "Support_PCB" plate, and screw them into the RFID support
* Add 1 x M2 x 10 screw into the remaining hole of the RFID support
* Tight the 4 screws
* Add the power board 12V on the back side of the "Support_PCB" plate, facing the two top screws of the main board
* Add 2 x M2 nuts and tight them

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/PCB_support_noWire.jpg">
<img src="../assets/images/Burrow_assembling/PCB_support_noWire.jpg" alt="PCB support assembling without wires" width="800" >
</a>
<!-- markdownlint-enable MD033 -->

* Add and screw 6 wires from RFID reader to the main board
* Connect the 3 ways JST PH cable (cable delivered with the 3 ways JST PH connector) into the main board and wire it into the power board 12V connector (PWR_mng connector)
* Connect the 2 ways JST XH cable into the main board and wire it into the power board 12V connector (PWR_5V connector)
* Connect two wires into the main button with two lugs
* Maintain the SWITCH button into the "Support_PCB" by 2 x M2.5 x 20 screws, 2 washers and 2 x M2.5 nuts
* Connect the wire extremity to the "SWITCH" connector of the power board

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/PCB_support_Wire.jpg">
<img src="../assets/images/Burrow_assembling/PCB_support_Wire.jpg" alt="PCB support assembling with wires" width="800" >
</a>
<!-- markdownlint-enable MD033 -->

* Screw two angle brackets into the "Support_PCB" plate with 4 x M3 x 8, M3 washers and M3 nuts. Angle brackets have to be positioned on the RFID side of the plate.

## Step 3 : Assembly the case

* Wire the START button with two pairs of wires : Each pair have to be connected on the NO & COM pins.
*Note* It's advised to **wind the wires of each pairs together** in order to correctly wire them next into the main board
* Install the "Support_inf" plate into the case
* Insert the antenna connector into the main board screw terminal block and tight. **Ensure the IR receiver #1 (green wire) is positioned at the top**
  *Note* The antenna connector has to be screwed into the main board **before the "Support_PCB" plate fixation** into the case, for a better access to the screws
* Screw the red led into the 2 ways screw terminal block of the main board

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Terminal_wiring.jpg">
<img src="../assets/images/Burrow_assembling/Terminal_wiring.jpg" alt="Terminal wiring" width="600" >
</a>
<!-- markdownlint-enable MD033 -->

* Screw the "Support_PCB" plate into the "Support_inf" plate with 4 self-tapping screws M3 x 6
* Pass the START button cables through the "Support_PCB", and connect it to the terminal blocks of the power board 12V
* Prepare two power supply cables of 15cm, with lug at one extremity, and connect the other extremity in the "BAT 12V" connector of the power board

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Final_wiring01.jpg">
<img src="../assets/images/Burrow_assembling/Final_wiring01.jpg" alt="Final wiring" width="400" >
</a>
<a href="../assets/images/Burrow_assembling/Final_wiring02.jpg">
<img src="../assets/images/Burrow_assembling/Final_wiring02.jpg" alt="Final wiring" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Add 5 mm thick sealing tape on each side of the battery compartment
* Add 3 mm thick sealing tape above the battery slot
* Add the batteries and connect them with the dedicated lugs

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Final_assembling.jpg">
<img src="../assets/images/Burrow_assembling/Final_assembling.jpg" alt="Final assembling" width="400" >
</a>
<!-- markdownlint-enable MD033 -->