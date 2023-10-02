# Final assembling

This page describes how to assembly mechanical & electronic components dedicated to a nest box. Some 3D printed supports are prepared and then the electronic boards are inserted and fixed into it.

To follow these steps, it's required to have already realized a [nest box antenna](Antenna_nest_assembling.md) and the [electronic boards](Electronic_assembling.md).The main board has to **be [programmed](programming.md) and RTC has to be up-to-date**.

## Step 1 : 3D print the parts

* Case : [Upper_case.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/Upper_case.stl) and [Lower_case.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/Lower_case.stl)
* Technical door : [Technical_door.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/Technical_door.stl)
* RFID support : [RFID_support.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/RFID_support.stl)
* Battery case : [Battery_case.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/Battery_case.stl)
* Battery cover : [Battery_cover.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/Battery_cover.stl)
* Trap lever : [Trap_lever.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/Trap_lever.stl)
* Trap door : [Trap_door.stl](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_schwegler/3D_print/Full_device/Trap_door.stl)

## Step 2 : Prepare the case

* Solder the main button switch (bistable) and the switch button (monostable) to free wire end : Let ~10cm and ~20cm of wire respectively.
* Solder the USB connecter to a JST connector. let ~15cm of wire
* Install the two buttons on the lower case. Add two switch sealing boots with their seals.
* Install the USB connector and its seal
* Install the red led and its seal on the lower case

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_bottom.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_bottom.jpg" alt="Nest box bottom" width="450" >
</a>
<!-- markdownlint-enable MD033 -->

* Install one O-rings Ø36mmx1 on each extremity of the antenna
* Install the antenna into the lower case and fix it with 2 x M2 L6 screws

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_wAntenna.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_wAntenna.jpg" alt="Nest box empty with antenna" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 3 : Add electronic boards & wiring

* Install the power board into the lower case and fix it with 2 x M2 L8 screws + 2 x M2 L10 screws
* Connect the USB wires to the 'Batt' connector of the solar charger
* Connect the switch button to the 2 ways screw terminal block 'SW'
* Connect the main button switch  to the 2 ways screw terminal block 'On / Off'

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Power_board_installed.jpg">
<img src="../assets/images/Nest_box_assem/Power_board_installed.jpg" alt="Installation of power board" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

* Install the main board into the lower case and fix it with 1 x M2 L8 screws into the left bottom hole
* Connect the 3 ways JST XH cable (cable delivered with the 3 ways JST XH connector) into the PWR_mng connector, and the other extremity of this cable to the power board (connector BAT / EN / SW)
* Connect the 2 ways JST XH cable into to the PW connector, and the other extremity of this cable to the power board (connector +5V / GND)
* Connect the LED to the main board into the LED connector
* Connect the cable from the antenna into the 8 ways screw terminal block. **Do not connect the RFID antenna**. Ensure to connect the photoreceptor at the top of the antenna into the PR1 screw terminal block, and the one of the bottom into the PR2 block.
* Connect the RFID connector to free wire end : Let ~10cm of wire

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Main_board_installed.jpg">
<img src="../assets/images/Nest_box_assem/Main_board_installed.jpg" alt="Installation of main board" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

* Install the Tectus RFID board into its 3D-printed support
* Connect the coil antenna to the antenna connector of the Tectus board
* Connect the Tectus RFID board to the main board
* Once all the wires connected, fix the RFID support to the lower case by 2 x M2 L20 screws, through the main board

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_opened.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_opened.jpg" alt="Nest box assembled opened" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 4 : Close the case

* Add some Loctite SI5940 Sealant to the joint surface, all around the lower case. Wait about 1h for it dry before moving to the next operation

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_opened_seal.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_opened_seal.jpg" alt="Nest box assembled opened with seal" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

* Close the nest box and fix it with 4 x M2.5 L6 countersunk screws
* Add the trap door, the trap lever and its elastic
* Add the technical door

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_closed.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_closed.jpg" alt="Nest box assembled" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 5 : Add the battery

* Solder the battery to the USB cable
* Install the battery into the battery case
* Add the battery cover
* Close the assembly with 4 x M2 L10 screws
* Connect the USB cable into the USB connector
