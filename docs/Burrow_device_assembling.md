# Final assembling

This page describes how to assemble all the burrow device components into a Pelicase.

Some supports are prepared and then the electronic boards are mounted on it and wired. Finally the equipped supports are installed into the Pelicase and connected to the antenna and the batteries.

To follow these steps, it's required to have already realized a [burrow antenna](Antenna_burrow_assembling.md), all the [electronic boards](Electronic_assembling.md) and a [burrow case](Burrow_case.md).The main board has to **be [programmed](programming.md) and RTC has to be up-to-date**. In addition, the **burrow antenna has to be attached** to the case.

## Step 1 : Prepare the supports

* 3D print the part ["RFID_support.stl"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/antenna_burrow/Support_RFID.stl)
* Insert 2 x M2.5 nuts in the RFID support
* Insert the RFID reader in its support. Be careful to respect the orientation

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/RFID/RFID_wSupport.jpg">
<img src="../assets/images/RFID/RFID_wSupport.jpg" alt="RFID reader in its support" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Prepare the PVC fixation parts ["Support_inf"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/antenna_burrow/Support_inf.pdf) and ["Support_PCB"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/antenna_burrow/Support_PCB.pdf) according to their drawings
* Screw two angle brackets into the "Support_inf" plate with 4 self-tapping screws M3 x 6

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Support_inf.jpg">
<img src="../assets/images/Burrow_assembling/Support_inf.jpg" alt="Support inf" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 2 : Assembly the PCB support

* Attach the main board on the "Support_PCB" plate using 2 x M2.5 x 12 screws and M2.5 nuts into the top holes. Do not tighten
* Position the RFID reader and its support on the back side of the "Support_PCB" plate, facing the two bottom holes of the main board
* Add 2 x M2.5 x 12 screws into the bottom holes of the main board, through the "Support_PCB" plate, and screw them into the RFID support
* Tight the 4 screws
* Add the power board 12V on the back side of the "Support_PCB" plate, facing the two top screws of the main board
* Add 2 x M2.5 nuts and tight them

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Support_PCB_noWire.jpg">
<img src="../assets/images/Burrow_assembling/Support_PCB_noWire.jpg" alt="Support PCB assembling without wires" width="800" >
</a>
<!-- markdownlint-enable MD033 -->

* Add and screw 6 wires from RFID reader to the main board
* Connect the 3 ways JST XH cable (cable delivered with the 3 ways JST XH connector) into the main board and wire it into the power board 12V connector (PWR_mng connector)
* Connect the 2 ways JST XH cable into the main board and wire it into the power board 12V connector (PWR_5V connector)
* Connect two wires into the main button with two lugs
* Maintain the SWITCH button into the "Support_PCB" by 2 x M2.5 x 20 screws, 2 washers and 2 x M2.5 nuts
* Connect the wire extremity to the "SWITCH" connector of the power board

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Support_PCB_Wire.jpg">
<img src="../assets/images/Burrow_assembling/Support_PCB_Wire.jpg" alt="Support PCB assembling with wires" width="800" >
</a>
<!-- markdownlint-enable MD033 -->
  
* Screw two angle brackets into the "Support_PCB" plate 2 x M3 x 8, M3 washers and M3 nuts. Angle brackets have to be positioned on the RFID side of the plate.

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