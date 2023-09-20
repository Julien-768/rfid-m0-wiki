
# Antenna for Schwegler

This antenna is designed for use on 3D printed door for [Schwegler nest box 2M](https://www.schwegler-natur.de/portfolio_1408366639/nisthoehle-2m/?lang=en), it is suitable with the Tectus RFID reader TITAN 4004 (also know as TLB-30-USB).

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/schwegler_antenna.jpg">
<img src="../assets/images/Antennas/schwegler_antenna.jpg" height="400" width="400">
</a>
<!-- markdownlint-enable MD033 -->

## Radiating pattern

The radiation pattern was measured with a 2.3mm EM4102 PIT Bird Tag from [Eccel Technology Ltd.](https://eccel.co.uk/product/2-3mm-em4102-pit-bird-tag-black/)
The read range is 400 mm (typical values) with a EM4102 transponders (1.7 mm Ø) in the best conditions.
The following results are measured on an antenna with a quality factor Q = 23.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Antennas/schwegler_radiation_best.png">
<img src="../assets/images/Antennas/schwegler_radiation_best.png" width="600">
</a>
<a href="../assets/images/Antennas/schwegler_radiation_worst.png">
<img src="../assets/images/Antennas/schwegler_radiation_worst.png" width="600">
</a>
<!-- markdownlint-enable MD033 -->

## Mechanical specifications

### Dimension

The antenna is an circle of Ø36 mm . You can access the [mechanical schematic on the repository](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/tree/master/antenna_schwegler)

### 3D preview

<!-- markdownlint-disable MD033 -->

<iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/raw/master/antenna_schwegler/Antenna.stl?inline=false" style="border:0;margin:0;width:100%;height:400px;"></iframe>

<!-- markdownlint-enable MD033 -->

## Electronic specifications

The antenna inductance is around 192µH to be compliant to the Tectus RFID reader TITAN 4004. It is suitable with the 125 - 134 kHz frequency range. It requires 7.5 m of Ø0.2mm enamelled copper wire which would make ~67 spires.

## Assembling instructions

Please refer to the [Developper section of the project for assembling instructions](./Assembling_antenna.md).
