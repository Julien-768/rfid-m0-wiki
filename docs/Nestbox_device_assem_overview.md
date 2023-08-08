# Assembly a nest box device

This section describes the different steps to follow to assemble a device that monitor a nest box occupation. The list of required material is avaible at this[link](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.elec/-/blob/development/Bill%20of%20material.xlsx).

Firstly, a **nest box antenna is build**. This antenna receives the RFID antenna, able to detect RFID tags, but also two infrared sensors. The manufacturing of this device is based on 3D-printed parts in which electronic components are inserted and glued.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/schwegler_antenna.jpg">
<img src="../assets/images/Antennas/schwegler_antenna.jpg" width="300">
</a>
<!-- markdownlint-enable MD033 -->

Secondly **electronic component are mounted** into the boards. There are three boards that are required :

* A main board
* A power board in charge of power management
* A RFID reader based on a Tectus board

The RFID board only requires to weld some connectors.

Due to the dimensions of the nest box, **only the 5v power board can be used**. In addition, the compatibility with an additional solar panel or USB charger is possible.

The last step before the final assembling is to **program the main board**. This step must be done after the electronic assembling in order to correctly set the time of the real-time-clock (CR1220 coin cell must be inserted).

Finally **all the components are installed into the nest box and wired**. This step requires 3D-printing and wiring to connect the different boards together.

Once battery inserted and connected, the device will be ready.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Nest_box_assem/Nest_box_closed.jpg">
<img src="../assets/images/Nest_box_assem/Nest_box_closed.jpg" alt="Nest box assembled" width="250" >
</a>
<!-- markdownlint-enable MD033 -->
