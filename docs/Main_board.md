# Main board

## Schematic of the system

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/Schematic.png">
<img src="../assets/images/Main_board/Schematic.png" width="800">
</a>
<!-- markdownlint-enable MD033 -->

The main board has different voltage levels :

* 5V : Provided by the PW connector, the 5V is distributed to the Feather M0, the RFID module, the servomotor and the 3.3V voltage regulator
* 3V (permanent) : Provided by the internal Feather M0 regulator, this 3V powers the RTC module
* 3V (piloted) : Provided by the 3.3V regulator, this voltage powers the IR emitter & receiver and the temperature sensor (RTD)

As the Feather is a 3V-logic level, all the inputs / outputs are **3V-logic based**.

Several **communication modes** are used :

* [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) for the RTC module
* [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface) for the integrated SD card and the RTD module
* [UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter) for the RFID reader

For **power supply**, refers to the [Overview](./Electronic_overview.md) section.

## Materials

### Development board

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/Feather_M0.png">
<img src="../assets/images/Main_board/Feather_M0.png" width="250">
</a>
<!-- markdownlint-enable MD033 -->

The Adafruit Feather M0 Adalogger is an Arduino-type development board specially designed for data recording applications. Its 256 kB of flash allows to have a larger memory than most equivalent models. The recorded data are stored into the integrated microSD slot.
**This is a 3.3v-logic level board : Be careful to ensure the voltage compatibility when it's used with 5v-logic sensors**  

More information about the board in the [Adafruit tutorial](https://learn.adafruit.com/adafruit-feather-m0-adalogger/overview)

Description of the pinout used :  
<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/Feather_M0_pinout.png">
<img src="../assets/images/Main_board/Feather_M0_pinout.png" width="800">
</a>
<!-- markdownlint-enable MD033 -->

### Servomotor

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/ServoMotor.png">
<img src="../assets/images/Main_board/ServoMotor.png" width="200">
</a>
<!-- markdownlint-enable MD033 -->

The Hitec HS-53 servomotor is suitable for miniaturized or energy-saving systems. With a rotational speed of 1.2 rev/s, it can deliver a maximal torque of 1.5 kg.cm.
5V power supply

For more details refers to the [datasheet](https://asset.conrad.com/media10/add/160267/c1/-/gl/001081926ML01/mode-demploi-1081926-mini-servomoteur-analogique-hitec-hs-53-112053-1-pcs.pdf)

### Real-Time-Clock (RTC) module

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/RTC_module.png">
<img src="../assets/images/Main_board/RTC_module.png" width="200">
</a>
<!-- markdownlint-enable MD033 -->

This sensor keeps the date & time thanks to its internal battery and a very low power consumption (~110µA @ 3.6V in standby mode). This module communicates with an I2C link and can be resynchronized by software. Supply voltage from 2.3V to 5.5V  
The internal battery is based on a [CR1220 3V lithium coin cell battery](https://www.adafruit.com/product/380)

More information about the board in the [Adafruit tutorial](https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/overview) and the [product specifications](https://www.adafruit.com/product/3013)

### RFID module

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/RFID/RFID_module.png">
<img src="../assets/images/RFID/RFID_module.png" width="300">
</a>
<!-- markdownlint-enable MD033 -->

The Tectus RFID board supports the HDX, FDX and EM4102 protocols. Linked to a 190µH external antenna, its range mainly depends of the antenna size and the type of transponder used.

More information about the [connection pinout](./uploads/81b7cef750505db74dd9b735ed8705fd/Connection_Drawing_TLB-30-SER.pdf) and the [communication](./uploads/651a3e69d9c31fa0e2970c75e4627ca0/scotty.v1.4_TLB-30-Commands_.pdf)

### Resistance-Temperature-Detector (RTD) sensor

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/RTD_module.png">
<img src="../assets/images/Main_board/RTD_module.png" width="200">
</a>
<!-- markdownlint-enable MD033 -->

This sensor measures the ambiant temperature thanks to a resistor that varies according to the temperature. The temperature admissible range is -200°c to +450°c. Supply voltage from 3V to 5V  
To use this sensor with two-wires probe, solder the *2/3 wire* et *2 wire* plugs and ensure the wires are connected on the *F+* et *F-* terminals.

More information in the [Adafruit tutorial](https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier/overview)

### Infrared barrier

This 36kHz modulated infrared barrier filters out natural ambient infrared radiation, and frees itself from the brightness of the environment.

#### Infrared emitter

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/IR_emitter.png">
<img src="../assets/images/Main_board/IR_emitter.png" width="200">
</a>
<!-- markdownlint-enable MD033 -->

The TSAL4400 emitter is an infrared diode that emits a light of 940nm wavelength.
The cathode (-) is the shortest pin (no flat visible). Max admissible current : 100mA  
To be compatible with the receiver, **this emitter has to emit a 36 kHz signal**. Refers to the [Infrared section](Infrared.md) to know how to create the modulation.

For more information refers to the [datasheet](https://www.vishay.com/docs/81006/tsal4400.pdf)

#### Infrared receiver

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Main_board/IR_phototransistor.png">
<img src="../assets/images/Main_board/IR_phototransistor.png" width="300">
</a>
<!-- markdownlint-enable MD033 -->

The TSOP34536 infrared receiver is designed to work in very noisy environment and detects only a 36 kHz IR signal.
With a very low power consumption, it can be powered from 2.5V to 5.5V

For more information refers to the [datasheet](https://www.vishay.com/doc?82490)
