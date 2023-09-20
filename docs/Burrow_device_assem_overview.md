# Assembly a burrow device

This section describes the different steps to follow to assemble a device that monitor a burrow occupation. The list of required material is avaible at this [link](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.elec/-/blob/master/Bill%20of%20material.xlsx).

Firstly, a **burrow antenna is build**. This antenna receives the RFID antenna, able to detect RFID tags, but also two infrared sensors. The manufacturing of this device is based on 3D-printed parts in which electronic components are inserted. Resin is then added to protect the components from environment and rodents.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_antenna.jpg">
<img src="../assets/images/Antennas/burrow_antenna.jpg" width="250">
</a>
<!-- markdownlint-enable MD033 -->

Secondly **electronic component are mounted** into the boards. There are three boards that are required :

* A main board
* A power board in charge of power management
* A RFID reader based on a Tectus board

The last board only requires to weld some connectors. The power board (two variants exist) must be chosen according to the battery technology.

**A case is then prepared** and assembled with the antenna. The machining of the case must be carefully done to prevent water from entering the housing.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Case/Case_with_components.jpg">
<img src="../assets/images/Case/Case_with_components.jpg" alt="Case with external components" width="250" >
</a>
<!-- markdownlint-enable MD033 -->

The last step before the final assembling is to **program the main board**. This step must be done after the electronic assembling in order to correctly set the time of the real-time-clock (CR1220 coin cell must be inserted).

Finally **all the components are installed into the case**. This step requires wiring to connect the different boards together.

Once battery inserted and connected, the device will be ready for [checking](Check_burrow_device.md).

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Burrow_assembling/Final_assembling.jpg">
<img src="../assets/images/Burrow_assembling/Final_assembling.jpg" alt="Final assembling" width="300" >
</a>
<!-- markdownlint-enable MD033 -->
