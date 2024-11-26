# Make the Coil Antenna and its Metal Sheath

The antenna consists of two main parts:

- **Antenna Base**: Houses the IR sensors and cabling for the RFID antenna.
- **Antenna Cover**: Screws onto the Antenna Base and uses a waterproof seal to ensure a secure fit.

When the Antenna Base and Cover are assembled and the cable is connected, resin casting is applied to protect the sensors.

## Step 1: Prepare the Antenna Base

Refer to the [dedicated page](./Antenna_Burrow.md) for a full description of the antenna and its specifications.

- **3D Print** the part [“Antenna.stl”](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_burrow/antenna.stl).
- Apply a **first coat of epoxy resin** to the interior walls of the Antenna Base for impregnation, which will help secure the resin casting. Use a long-setting resin (24 hours) to allow time to fully spread resin along the walls. (Preparation weight ratio: 5 parts resin to 1 part hardener).
- **Wind a Coil Antenna**: Follow the [antenna assembly guide](./Assembling_antenna.md) and wind approximately 30 turns around the Antenna Base to achieve an impedance of 192uH.
- **Connect the IR Emitters and Receivers**: Attach wires (15 cm) to each component, ensuring you follow the [wire color table](#wire_color_table).
- **Secure the IR Components into the Antenna Base**:
  - Position the **IR Emitting Diode** on the left side of the Antenna Base in its designated hole and secure it with a glue gun.
  - Position the **IR Receiver Module** on the right side in its hole, facing outward, and secure it with a glue gun.
  - Apply a polyurethane glue coat (Araldite 2028-1 Spray Gun) inside the IR receiver hole to form a **protective bulb** around the IR Receiver Module. This bulb prevents mud from accumulating over the sensor.

<a href="../assets/images/Antennas/Burrow_ant_base.png">
<img src="../assets/images/Antennas/Burrow_ant_base.png" alt="Burrow antenna base" height="400">
</a>

## Step 2: Prepare the Antenna Cover

- **3D Print** the part [“Cover.stl”](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/blob/master/antenna_burrow/cover.stl).
- Apply a **first coat of epoxy resin** to the interior walls of the Antenna Cover for impregnation, just as for the Antenna Base. Use the same long-setting resin (24 hours) and preparation ratio (5 parts resin to 1 part hardener).
- **Attach the Short Pipe**: Secure the Short Pipe to the Antenna Cover using an O-ring and a brass nut to create a waterproof seal.

<a href="../assets/images/Antennas/Burrow_ant_cover.png">
<img src="../assets/images/Antennas/Burrow_ant_cover.png" alt="Burrow antenna cover" height="400">
</a>

## Step 3: Wire the Antenna Assembly

1. **Connect the Antenna Wires**:

   - Connect each antenna wire to the interface board’s terminal block, ensuring correct color-positioning for each wire according to the following color associations:

   <a name="wire_color_table"></a>

   | Color        | Function      |
   | ------------ | ------------- |
   | Green        | Receiver IR 1 |
   | White/Green  | Receiver IR 2 |
   | Blue         | Emitter IR 1  |
   | White/Blue   | Emitter IR 2  |
   | Brown        | +3.3V         |
   | White/Brown  | GND           |
   | White/Orange | Antenna +     |
   | Orange       | Antenna -     |
   | Shield       | Linked to GND |

   <a href="../assets/images/Antennas/Burrow_ant_cable.jpg">
   <img src="../assets/images/Antennas/Burrow_ant_cable.jpg" alt="Burrow antenna wire" width="500" >
   </a>

2. **Prepare the Ethernet Cable**:

   - Strip and tin both ends of the Ethernet cable wires.
   - Screw each wire into the terminal block, following the color associations above.

3. **Check Electrical Resistance**:

   - Measure the resistance between specified points to confirm wiring accuracy. Record the following values for reference:

   | Side +      | Side -       | Electrical Resistance (Ohm) |
   | ----------- | ------------ | --------------------------- |
   | Orange      | White/Orange | ~6 Ω                        |
   | Brown       | White/Brown  | ~6 MΩ                       |
   | Green       | White/Brown  | ~12 MΩ                      |
   | White/Green | White/Brown  | ~12 MΩ                      |
   | Brown       | Blue         | ~18 MΩ                      |
   | Brown       | White/Blue   | ~18 MΩ                      |

4. **Install the Foam Seal**:

   - Insert the foam seal inside the Short Pipe to waterproof the connection.
   - Pass the cable through the Antenna Cover inlet (seal, Short Pipe, and brass nut).

5. **Assemble the Cable Sheath**:

   - Pass the cable through the **Stainless Steel Sheath** and screw it into the Short Pipe.
   - Cut the Ethernet cable to leave 20 cm of excess.
   - Pass the cable through the Long Pipe, and screw the Stainless Steel Sheath onto it.
   - **Attach the O-ring** to the Long Pipe, then secure with a brass nut.
   - **Solder Cable Ends to Male Connectors**: Solder wires to the male connectors in the same order as in the terminal block. Group connectors in sets of four to fit through the brass nut. Ensure the shield wire is connected to ground.

<a href="../assets/images/Antennas/Antenna_extremity.jpg">
<img src="../assets/images/Antennas/Antenna_extremity.jpg" alt="Antenna extremity" width="500">
</a>

## Step 4: Pour and Cure the Resin

1. **Seal the Cover-Base Junction**:

   - Apply a continuous coat of **LOCTITE SI 595 Superflex transparent silicone** around the cover-base junction to ensure waterproofing.
   - Screw the Antenna Cover onto the Antenna Base using 6mm self-tapping screws. Apply additional silicone as needed to seal any gaps.

2. **Prepare the Antenna for Resin Pouring**:

   - Use modeling clay to cover the IR Emitters and IR Receivers on the inner side of the coil, preventing resin from covering these components.
   - Ensure all cables are positioned inside the antenna. Secure any loose cables with a glue gun to keep them from protruding.

3. **Position the Antenna**:

   - Place the antenna flat and level. Keep the cable upright to prevent shifting as resin cures.

4. **Pour Resin in Two Stages**:

   - **First Pour**: Mix a **20g batch of epoxy resin** (ratio: 2 parts resin to 1 part hardener, with 1% white pigment) to check for leaks.
   - Once the first layer is dry, pour a final **130g batch** of resin with the same ratio to fill the antenna. Allow 24 hours for curing.

5. **Final Clean-Up**:
   - Once the resin is fully cured, remove any remaining modeling clay and excess silicone. Verify the integrity of all seals.

<a href="../assets/images/Antennas/Burrow_ant_resin.jpg">
<img src="../assets/images/Antennas/Burrow_ant_resin.jpg" alt="Antenna resined" height="400">
</a>
