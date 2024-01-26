# Modulated infrared functionnality

## Description

The infrarer barrier uses the same principle and components than infrared remote controls. A infrared pulsed light is emitted at a certain frequency (36kHz in our case). A receiver, only sensitive to this frequency, is placed in front of the emitter. This receiver sends a low-level output only if it detects the signal (high-level output if no signal).
Indeed this barrier in an On / Off system, with no distance detection. More the infrared signal is intense, higher can be the infrared barrier (several meters).

## Software used to generate a 36 kHz Pulsed Width Modulation

For generating a PWM on the Feather M0, we use the [Arduino SAMD21 turbo PWM](https://github.com/ocrdu/Arduino_SAMD21_turbo_PWM) on an available [PWM pin](./assets/images/Main_board/Feather_M0_pinout.png)

<!-- markdownlint-disable MD010 -->

```C
#include "SAMD21turboPWM.h"         // https://github.com/ocrdu/Arduino_SAMD21_turbo_PWM

#define PIN_IR_PWM      11          // output pwm 36kHz for IR sensor
//...
pinMode(PIN_IR_PWM, OUTPUT);
//...
TurboPWM pwm;
//...
pwm.setClockDivider(16, false);		// Main clock divided by 16 => 3MHz
pwm.timer(2, 4, 20, true);			// Use timer 2 for pin PIN_IR_PWM, divide clock by 4, resolution 20, single-slope PWM
pwm.analogWrite(PIN_IR_PWM, 500);   // PWM frequency is now around 36KHz, dutycycle is 500 / 1000 * 100% = 50%
```

<!-- markdownlint-enable MD010 -->

## PWM 36kHz - output generated

<a href="../assets/images/Main_board/Scope_IR_Modulation_output_1.png">
<img alt="scope screenshot of 36 kHz modulation for infrared emitter" src="../assets/images/Main_board/Scope_IR_Modulation_output_1.png" width="400">
</a>

Measurement made on the pin output of the Feather M0 without any Infrared emitter connected.

The Infrared emitter has an wide opening angle. For testing purpose, use heat shrink or wrap black tape around it to create a kind of pipe and reduce the opening angle.

## Infrared receiver - input read

<a href="../assets/images/Main_board/Scope_IR_input_1.png">
<img alt="scope screenshot of infrared photo receiver output" src="../assets/images/Main_board/Scope_IR_input_1.png" width="400">
</a>

Measurement made on the pin output of the Phototransistor TSOP34536.

## Examples on the web

- Coutning by IR crossing with Arduino UNO
  <http://makerspace56.org/comptage-par-franchissement-dune-barriere-infrarouge/>

- Youtube "la grotte du geek" with code dedicated for STM32CubeIDE
  <https://www.youtube.com/watch?v=\_tcBtZZDsCE>

- Adafruit "Using an Infrared Library on Arduino"
  <https://learn.adafruit.com/using-an-infrared-library/sending-ir-codes>

## How to check the infrared barriers are working ?

Refers to the [Checking procedure](Checking_procedure.md), section "Infrared beam" to know how to check the IR barrier
