# Assembling a coil antenna

## Bill of Materials

The material needed to make a coil antenna is:

- Enamelled copper wire. The 0.2 copper wire from Radiospares is used ([RadioSpare ref 357-918](https://fr.rs-online.com/web/p/fils-de-cuivre/0357918))
- The structure to wrap the antenna around. This is the 3D printed part named antenna.stl.
- A glue gun
- Standard 28 AWG wire for connecting to the RFID reader
- Soldering material, iron, solder, heat shrink...

## Antenna sizing

If the wire lenght is not specified for the specific antenna we want to build, the Nagaoka's formula would help us.
It returns the inductance based on the coil diameter, the thickness of the wire and the number of spires of the coil antenna.

Note : we are not exactly in the conditions of the formula, the final inductance will need to be measured with an inductance meter.

Two scripts are available for the sizing. The first one calculates the length of wire required for the coil antenna, based on the antenna diameter, the wire diameter and the desired inductance :

??? "Python code for coil inductance sizing"

    ```
    --8<-- "docs/assets/code/Antenna_coil_sizing.py"
    ```

The second script allows to check if the chosen coil design achieves the required inductance, based on the real length and number of spires of the coil :

??? "Python code to check the coil inductance"

    ```
    --8<-- "docs/assets/code/Inductors_characteristics.py"
    ```

## Soldering instructions

The copper wire used is enamelled. For soldering we need first to remove the enamelled coating.
The safest option is to sand the enamel off by using a fine sandpaper.
An other option is to melt the enamel off by using the soldering iron, solder and the flux within it, extra flux.

If you are not used to the method, we strongly recommand to browse for some video of ['How to remove enamel coating from copper wire'](https://www.youtube.com/results?search_query=how+to+remove+enamel+coating+from+copper+wire)

## Assembly steps

- Wrap the wire around its structure. Leave a starting length out of the wrapping, around 20 cm will be ok.
- When the wrapping is done, check the inductance of the coil with an inductance meter. Ensure to select the right frequency (as close as possible to the antenna frequency range).
  The theoretical quality factor of the antenna has to be checked too (Q option on the inductance meter). The Q quality factor can be calculated with the following equation :

  $$
  Q = \frac{2 \cdot \pi \cdot f \cdot L}{1000 \cdot R}
  $$

  with Q the quality factor, f the coil frequency in kHz, L the coil inductance in µH, and R the coil resistance in Ohm

- Once the coil is validated, use the glue gun to fix the coil to the structure and wires together
- Prepare the enamelled wire for soldering few centimeters out of the coil. Solder standard wire on it, use heat shrink for insulation. Twist the cable for the antenna tail not to radiate.

<a href="../assets/images/Antennas/Nest_box_antenna_wiring">
<img alt="Nestbox antenna wired around a 3D printed part" src="../assets/images/Antennas/Nest_box_antenna_wiring" width="500">
</a>

- Glue the welded parts close inside the 3D printed part
