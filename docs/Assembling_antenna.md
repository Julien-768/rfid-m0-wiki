# Assembling a coil antenna

## Bill of Materials

The material needed to make a coil antenna is:

* enamelled copper wire. We used the 0.2 copper wire from Radiospares ([RadioSpare ref 357-918](https://fr.rs-online.com/web/p/fils-de-cuivre/0357918))
* the structure to wrap the antenna around. This is the 3D printed part named antenna.stl.
* a glue gun
* standard wire for connecting to the reader part TODO REF
* connectors, if needed, to easily manipulate your antenna TODO REF
* soldering material, iron, solder, heat shrink, ...

## Antenna sizing

If wire lenght is not specified for the specific antenna we want to build, the Nagaoka's formula would help us.
It returns the inductance based on the size, the thickness and the number of spires of the coil antenna.
This script allows to check if the chosen coil design achieves the required inductance.

Note : we are not exactly in the conditions of the formula, the final inductance will need to be measured with an inductance meter.

<!-- markdownlint-disable MD038 -->
note "Python code for calculating the coil inductance"
    ```
    --8<-- "docs/assets/code/Inductors_characteristics.py"
    ```
<!-- markdownlint-enable MD038 -->

## Soldering instructions

The copper wire used is enamelled. For soldering we need first to remove the enamelled coating.
The safest option is to sand the enamel off by using a fine sandpaper.
An other option is to melt the enamel off by using the soldering iron, solder and the flux within it, extra flux.

If you are not used to the method, we strongly recommand to browse for some video of 'how to remove enamel coating from copper wire'

## Assembly steps

* Wrap the wire around its structure. Leave a starting lenght out of the wrapping, around 20 cm will be ok.
* When the wrapping is done, check the inductance of the coil with an inductance meter. Ensure to select the right frequency (as close as possible to the antenna frequency range).
  The theoretical quality factor of the antenna has to be ckecked too (Q option on the inductance meter). The Q quality factor can be calculed with the following equation :

    $$
    Q = \frac{2 \cdot \pi \cdot f \cdot L}{1000 \cdot R}
    $$

   with Q the quality factor, f the coil frequency in kHz, L the coil inductance in µH, and R the coil resistance in Ohm

* When the coil is validated, use the glue gun to fix the coil to the structure and wires together
* Prepare the enamelled wire for soldering few centimeters out of the coil. Solder standard wire on it, use heat shrink for insulation. Twist the cable for the antenna tail not to radiate.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/antenna_wiring.png">
<img src="../assets/images/Antennas/antenna_wiring.png" width="600">
</a>
<!-- markdownlint-enable MD033 -->

* Glue the welded parts close inside the 3D printed part
* Add your connector to the tail antenna
* Glue the connected parts
