# Final assembling

This page describes how to assembly mechanical & electronic components dedicated to a nest box. Some 3D printed supports are prepared and then the electronic boards are inserted and fixed into it.

To follow these steps, it's required to have already realized a [nest box antenna](Antenna_nest_assembling.md) and the [electronic boards](Electronic_assembling.md).The main board has to **be [programmed](programming.md) and RTC has to be up-to-date**.

## Step 1 : Prepare the parts

* 3D print the parts :
  
    * Case : ["Upper_case.stl"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/Schwegler_%20Nest_box_2M/Files%20for%203D%20printing/Upper_case.stl) and ["Lower_case.stl"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/Schwegler_%20Nest_box_2M/Files%20for%203D%20printing/Lower_case.stl)
    * Door : ["Door.stl"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/Schwegler_%20Nest_box_2M/Files%20for%203D%20printing/Door.stl)
    * Technical door : ["Technical_door.stl"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/Schwegler_%20Nest_box_2M/Files%20for%203D%20printing/Technical_door.stl)
    * Lever : ["Lever_stp.stl"](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/blob/development/Schwegler_%20Nest_box_2M/Files%20for%203D%20printing/Lever_stp.stl)

* Install the lever on the servo motor

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Servo_lever.jpg">
<img src="../assets/images/Nest_box_assem/Servo_lever.jpg" alt="Servo equipped with lever" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Solder wire on the + and - connections of the power board 5v (remove the jack connector if present). Connect the other extremity of the wire to the waterproof USB connector

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Power_board_USB.jpg">
<img src="../assets/images/Nest_box_assem/Power_board_USB.jpg" alt="Power board with USB connector" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Solder the main button switch (bistable) to JST 2-PH connectors, and the switch button (monostable) to free wire end : Let ~10cm of wire for buth buttons.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Switch.jpg">
<img src="../assets/images/Nest_box_assem/Switch.jpg" alt="Switch" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Solder JST 2-PH connectors on the battery

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Battery_wired.jpg">
<img src="../assets/images/Nest_box_assem/Battery_wired.jpg" alt="Battery with connectors" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 2 : Install the parts and wire

* Install the two buttons on the upper case. Add two switch sealing boots with their seals.
* Install the USB connector and its seal
* Install the power board into the upper case and fix it with 2 x M2 L10 screws
* Connect the main button switch : one extremity to the solar charger output, the other to the booster input
* Connect the switch button to the 2 ways screw terminal block
* Connect the 3 ways JST XH cable (cable delivered with the 3 ways JST XH connector) into the PWR_mng connector
* Connect the 2 ways JST XH cable into to the PWR_5V connector
* Connect the battery to the solar charger battery input. **Make sure the main button is Off** (no CHG light on the solar charger module). If it's not the case, turn off the button
* Install the main board into the upper case and fix it with 2 x M2 L10 screws. Take care to **orient the USB connector** to avoid collisions with the RTC module
* Connect the wires from the power board (3 ways JST XH and 2 ways JST XH) to the PW_mng and PW connectors
* Install the door and then the servo motor. The pin of the door must be placed inside the lever hole. Fix the motor it with 2 x M2 L10 screws
* Install the equipped antenna and fix it with 1 x M2.5 L6 screw
* Connect the servo motor to the Servo connector of the main board
* Connect the antenna to the IR connector of the main board. Do not connect the coil antenna, only the IR sensors.
* Install the Tectus board and fix it to the upper case with a plastic clamp
* Connect the coil antenna to the antenna connector of the Tectus board
* Connect the Tectus board to the main board
* Install the red led and its seal on the upper case. Then connect it to the main board
* Fix the battery in the lower case with velcro strap

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_opened.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_opened.jpg" alt="Nest box assembled opened" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

* Add the technical door
* Close the nest box and fix it with 4 x M2.5 L6 countersunk screws
* Add sealing glue on the junction of the two cases

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_closed.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_closed.jpg" alt="Nest box assembled" width="250" >
</a>
<!-- markdownlint-enable MD033 -->
