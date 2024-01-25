# Antenna for Schwegler

This antenna is designed for use on 3D printed door for [Schwegler nest box 2M](https://www.schwegler-natur.de/portfolio_1408366639/nisthoehle-2m/?lang=en), it is suitable with the Tectus RFID reader TITAN 4004 (also know as TLB-30-USB).

<a href="../assets/images/Antennas/schwegler_antenna.jpg">
<img alt="wired antenna and infrared beams around the 3D print in the lab" src="../assets/images/Antennas/schwegler_antenna.jpg" height="400" width="400">
</a>

## Radiating pattern

The radiation pattern was measured with a 2.3mm EM4102 PIT Bird Tag from [Eccel Technology Ltd.](https://eccel.co.uk/product/2-3mm-em4102-pit-bird-tag-black/)
The read range is 400 mm (typical values) with a EM4102 transponders (1.7 mm Ø) in the best conditions.
The following results are measured on an antenna with a quality factor Q = 23.

<a href="../assets/images/Antennas/schwegler_radiation_best.png">
<img alt="image of the radiation pattern of the Schwegler antenna with best TAG orientation" src="../assets/images/Antennas/schwegler_radiation_best.png" width="600">
</a>
<a href="../assets/images/Antennas/schwegler_radiation_worst.png">
<img alt="image of the radiation pattern of the Schwegler antenna with worth TAG orientation" src="../assets/images/Antennas/schwegler_radiation_worst.png" width="600">
</a>

## Mechanical specifications

### Dimensions

The internal diameter a the mechanical part is 32 mm. It is designed for great tits bird species. The depth the bird would have to cross is 34 mm.
The wired antenna itself is an circle of Ø36 mm by TODO height . You can access the [mechanical schematic on the repository](https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/tree/master/antenna_schwegler)

### 3D preview

<iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https://gitlab.in2p3.fr/rfid.m0/rfid.m0.meca/-/raw/master/antenna_schwegler/Antenna.stl?inline=false" style="border:0;margin:0;width:100%;height:400px;"></iframe>

## Electronic specifications

The antenna inductance is around 192µH to be compliant to the Tectus RFID reader TITAN 4004. It is suitable with the 125 - 134 kHz frequency range. It requires 7.5 m of Ø0.2mm enamelled copper wire which would make ~67 spires.

## Assembling instructions

Please refer to the [Developper section of the project for assembling instructions](./Assembling_antenna.md).
