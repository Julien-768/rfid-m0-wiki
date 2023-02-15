# Assembling a coil antenna

## Bill of Materials

The material needed to make a coil antenna is enamelled copper wire. We used the [ref CUL100/0.10 from BLOCK](https://www.block.eu/en_US/productversion/cul-100010/) [RadioSpare ref 337-7088](https://fr.rs-online.com/web/p/fils-de-cuivre/3377088)

## Antenna dimensionning

If wire lenght is not specified for the specific antenna we want to build, the Nagaoka's formula would help us.
It returns the inductance based on the size, the thickness and the number of spires of the coil antenna.
This will give us the wire lenght to use to make the coil.
Note we are not exactly in the conditions of the formula, the final inductance will need to be measured with an inductance meter.

??? note "Python code for calculating the coil inductance"
    ```
    --8<-- "docs/assets/code/Inductors_characteristics.py"
    ```

## Soldering instructions

The copper wire used is enamelled. For soldering we need first to remove the enamelled coating.
The safest option is to sand the enamel off by using a fine sandpaper.
An other option is to melt the enamel off by using the soldering iron, solder and the flux within it, extra flux.

if you are not used to the method, we strongly recommand to browse for some video of 'how to remove enamel coating from copper wire'
