# Assembling a coil antenna

## Bill of Materials

The material needed to make a coil antenna is:

* enamelled copper wire. We used the [ref CUL100/0.10 from BLOCK](https://www.block.eu/en_US/productversion/cul-100010/) ([RadioSpare ref 337-7088](https://fr.rs-online.com/web/p/fils-de-cuivre/3377088))
* the structure to wrap the antenna around. This is the 3D printed part named antenna.stl.
* a glue gun
* standard wire for connecting to the reader part TODO REF
* connectors, if needed, to easily manipulate your antenna TODO REF
* soldering material, iron, solder, heat shrink, ...

## Antenna dimensionning

If wire lenght is not specified for the specific antenna we want to build, the Nagaoka's formula would help us.
It returns the inductance based on the size, the thickness and the number of spires of the coil antenna.
This will give us the wire lenght to use to make the coil.
Note we are not exactly in the conditions of the formula, the final inductance will need to be measured with an inductance meter.

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

if you are not used to the method, we strongly recommand to browse for some video of 'how to remove enamel coating from copper wire'

## Assembly steps

* wrap the wire around its structure. Leave a starting lenght out of the wrapping, around 20 cm will be ok.
* when the wrapping is done, use the glue gun to fix the coil to the structure and wires together
* Prepare the enamelled wire for soldering few centimeters out of the coil. Solder standard wire on it, use heat shrink for insulation. Twist the cable for the antenna tail not to radiate.

TODO PHOTO

* Check the inductance of the coil
* glue the welded parts close inside the 3D printed part

* Add your connector to the tail antenna
* TODO
* glue the connected parts
