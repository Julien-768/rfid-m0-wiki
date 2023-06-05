# Antenna for burrow

This antenna is designed for use on an outdoor burrow, it is suitable with the Tectus RFID reader TITAN 4004 (also know as TLB-30-USB).

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_antenna.jpg">
<img src="../assets/images/Antennas/burrow_antenna.jpg" height="400" width="400">
</a>
<!-- markdownlint-enable MD033 -->

## Radiating pattern

The radiation pattern was measured with a FDX Biolog Tiny Tag from [biolog-animal](https://www.biolog-animal.com/en/products/veterinarian/biolog-tiny-domestic-fauna-10268/)
The read range is 700 mm (typical values) with a FDX transponders (8 mm x 1.4 mm Ø)

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/burrow_radiation.png">
<img src="../assets/images/Antennas/burrow_radiation.png" width="600">
</a>
<!-- markdownlint-enable MD033 -->

## Mechanical specifications

### Dimension

The antenna is a circle of Ø91 mm  by 7 mm height. You can access the [mechanical schematic on the repository](https://gitlab.in2p3.fr/rfid_m0/rfid_m0.meca/-/tree/master/antenna_burrow)

### 3D preview

<!-- markdownlint-disable MD033 -->
<iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https%3A%2F%2Fgitlab.in2p3.fr%2Frfid_m0%2Frfid_m0.meca%2F-%2Fraw%2Fmaster%2Fantenna_burrow%2FAssembly.stl%3Finline%3Dfalse&orientation=bottom&bgcolor=transparent" style="border:0;margin:0;width:100%;height:400px;"></iframe>
<!-- markdownlint-enable MD033 -->

## Electronic specifications

The antenna inductance is around 192µH to be compliant to the Tectus RFID reader TITAN 4004. It is suitable with the 125 - 134 kHz frequency range. It requires 8.8 m of Ø0.2mm enamelled copper wire which would make 30.6 spires (One spire is 0.286 m).

## Assembling instructions

Please refer to the [Developper section of the project for assembling instructions](./Assembling_antenna.md).
