# Make the coil antenna and its metal sheath

The antenna consists of two parts :

- One part that forms the inner edges : IR sensors are inserted inside and the RFID antenna is cabled

- One part that forms the outer edges and screws into the first, with a waterproof seal to ensure the seal between the parts

When the two parts are assembled together and the cable is connected, a resin casting is carried out to protect the sensors.

## Step 1 : Make the antenna base

- **3D print** the part « Socle.stl »
- Apply a **first coat of epoxy resin** for impregnation on the inside walls that will receive the resin casting. Use the long-setting resin (24h) to have time to spread resin into the walls (Weight ratio for preparation : 5 resin - 1 hardener)
- [Cable a coil antenna](./Assembling_antenna.md) for a 190uH impedance (+/- 29 spires) around the antenna base
- **Cable the IR** emitters and receivers (provide 15cm of wire) by ensuring to [respect the cable colors](./assets/images/Manufacturing/Interface_board_schema.png)
- **Stick the IR** into the antenna :
    - Position the IR emitter on the left side, seated in the hole and block it with glue gun
    - Position the IR receiver on the right side, face to the hole and block it with glue gun.
    - Apply a polyurethane glue coat in the IR receiver hole (Araldite 2028-1 Spray Gun) to **form a bulb** on the inside of the antenna. This bulb will avoid mud accumulation before sensor.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_ant_base.png">
<img src="../assets/images/Antennas/burrow_ant_base.png" alt="Burrow antenna base" height="400" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 2 : Make the antenna cover

- 3D print the part « Socle_couvercle.stl »
- **Machine two flats** on the brass large nut

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_ant_nut.png">
<img src="../assets/images/Antennas/burrow_ant_nut.png" alt="Burrow antenna nut" width="300" >
</a>
<!-- markdownlint-enable MD033 -->

- **Screw** the brass pipe + O-ring with nut on cover

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_ant_cover.png">
<img src="../assets/images/Antennas/burrow_ant_cover.png" alt="Burrow antenna cover" height="400" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 3 : Wire the antenna

- **Connect the antenna wires** to the interface board by ensuring to respect the wire position into the terminal block

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/Burrow_ant_cable.jpg">
<img src="../assets/images/Antennas/Burrow_ant_cable.jpg" alt="Burrow antenna wire" width="500" >
</a>
<!-- markdownlint-enable MD033 -->

- **Prepare the Ethernet cable**: Strip and tin both ends of wires
- **Screw wires** to the terminal block by respecting the following color association :

| Color                             | Function                          |
|-----------------------------------|-----------------------------------|
|Green                              | Receiver IR 1                     |
|White/Green                        | Receiver IR 2                     |
|Blue                               | Emitter IR 1                      |
|White/Blue                         | Emitter IR 2                      |
|Brown                              | +3.3V                             |
|White/Brown                        | GND                               |
|White/Orange                       | Antenna +                         |
|Orange                             | Antenna -                         |
|Shield                             | Linked to GND                     |

- **Check the antenna** by measuring the electrical resistance with multimeter:

|Side +            | Side -            | Electrical resistance [Ohm]    |
|------------------|-------------------|--------------------------------|
|Orange            |White/Orange       | ~ 6 Ohm                        |
|Brown             |White/Brown        | ~ 6 MOhm                       |
|Green             |White/Brown        | ~ 12 MOhm                      |
|White/Green       |White/Brown        | ~ 12 MOhm                      |
|Brown             |Blue               | ~ 18 MOhm                      |
|Brown             |White/Blue         | ~ 18 MOhm                      |

- **Install the foam seal** inside the short pipe to ensure seal between cable and pipe
- **Pass the cable** through the cover inlet (so into the seal + pipe + nut)
- Pass the cable **in the stainless steel sheath**
- **Screw** the stainless steel sheath into the short pipe
- **Cut the ethernet cable** by letting 20cm of cable exceed
- **Pass the cable** extremity through the long pipe and screw the stainless steel sheath on it
- **Add the O-ring** on the long pipe, then the brass nut
- **Weld** the end of the cables to male connectors. Ensure to respect the same order than in the terminal block. The male connectors have to be grouped by 4, in order to pass through the brass nut. The shield has to be linked to the ground wire.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/Antenna_extremity.jpg">
<img src="../assets/images/Antennas/Antenna_extremity.jpg" alt="Antenna extremity" width="500" >
</a>
<!-- markdownlint-enable MD033 -->

## Step 4 : Pour the resin

- **Apply silicone** (LOCTITE SI 595 Superflex transparent) over the entire base/cover junction
- **Screw** the cover onto the base with self-tapping screws (6mm)
- **Apply silicone** into the large nut

<!-- markdownlint-disable MD036 -->
*Wait for complete drying before further handling*
<!-- markdownlint-enable MD036 -->

- Apply special resin modelling clay to the IR transmitters and receivers (inner side of the coil) to prevent the resin from passing over the components
- Ensure there is no cable protruding over the antenna. If it's the case, hold it inside with glue gun
- Install the antenna on **flat position** and hold the cable high

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_ant_preparation.jpg">
<img src="../assets/images/Antennas/burrow_ant_preparation.jpg" alt="Burrow antenna preparation" width="400" >
</a>
<!-- markdownlint-enable MD033 -->

- **Pour a first 20g of epoxy** resin to check the tightness (Weight ratio : 1 resin - 1 hardener)
- **Check there is no leaks** between parts or over the sensors. If it's the case, clean immediatly
- Once the resin dried, **pour a 130g resin** to complete the antenna (Weight ratio : 1 resin - 1 hardener)
- Let the resin dry a couple of hours. Then clean the antenna (remove modelling clay and excess of silicon)

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_ant_resin.jpg">
<img src="../assets/images/Antennas/burrow_ant_resin.jpg" alt="Antenna resined" height="400" >
