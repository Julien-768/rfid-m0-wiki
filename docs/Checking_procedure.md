# Checking procedure

This page describes a simple procedure to check your hardware, either on the field or in your office.

## Before testing

1. Plug-in the battery
2. Check the SD memory card and the RTC battery are in their slots

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Procedure/Battery_connection.png">
<img src="../assets/images/Procedure/Battery_connection.png" alt= "battery connection" width="375">
</a>
<a href="../assets/images/Procedure/External_component.png">
<img src="../assets/images/Procedure/External_component.png" alt= "external component illustration" width="375">
</a>
<!-- markdownlint-enable MD033 -->

---

## Test procedure

### SD card and Real-Time Clock

We are going to check the SD card and the RTC are ok by checking the LEDs of the device.

1. Press the main switch (pressed = On)
2. Press the switch button until the external red LED turns on. Once done, release the switch button. The external red LED should turn OFF after the startup of the device.
    * If the external red LED does not light up at all, check that the battery connector well plugged-in
    * If the external red LED does not turn OFF, open your device and check the internal red led:
        * If it is blinking 2 times, the memory card is not found or is faulty, reinsert it or replace it.
        * If it is blinking 4 times, the RTC battery might be faulty, replace it.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Procedure/Led_difference.png">
<img src="../assets/images/Procedure/Led_difference.png" alt= "led difference" width="500">
</a>
<!-- markdownlint-enable MD033 -->

### Infrared beam

We are going to check if the infrared beams are working by checking the LED of the RFID reader. Indeed the RFID reader only try to read tags (so its LED blinks) after an infrared event is detected.

1. Once the device started and the external red LED is off, set your finger on one infrared receiver. Check that the RFID reader lights turn on for a few seconds (flashing red light)
2. After a few seconds, remove your finger and check that the RFID reader lights turn on for a few seconds (flashing red light)
3. Repeat the same operation with the second infrared receiver

*NOTE* As the angle of the IR cells is wide, it's important to well cover the infrared receiver.

It's possible to differentiate the bigger diameter of the IR receiver from the emitter. In addition, The receiver is mounted on the right side of the antenna.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Procedure/RFID_led.png">
<img src="../assets/images/Procedure/RFID_led.png" alt= "RFID led" height="250">
</a>
<a href="../assets/images/Procedure/IR_receiver.png">
<img src="../assets/images/Procedure/IR_receiver.png" alt= "IR receiver" width="300">
</a>
<!-- markdownlint-enable MD033 -->

### RFID reader

We are going to check if the RFID reader is able to detect and read a RFID tag, by passing a tag into the antenna and check the led of the device.

1. Pass your hand with a tag through the antenna
2. Check that the external LED flashes briefly

*NOTE* This test must be performed within 5 minutes after the system power-on. After this delay, the external red LED will be disabled for energy saving reasons.

### Device shutdown

1. Maintain the switch button pressed until the external red LED stops blinking and remains on
2. Release the switch button
3. Press main switch (released = Off)
4. Disconnect the battery

### SD card content and date / time

We are going to check if the SD card is correctly working (write data) and if the real-time clock is up-to-date by checking the content of the saved files.

1. Once the previous tests done, turn off the device and insert the SD card into a computer.
2. Check for a text file nammed with the current date (date format : YY_MM_DD.TXT). If it's the case, open it
3. In the file, check that the different events of the tests are present and that the associated time is correct.

??? "File content"

    ```
    2023-2-24;9:25:54.107;System; Start;
    2023-2-24;9:25:54.107;System; RTC is ok;
    2023-2-24;9:26:10.895;IR 1 ; broken beam ;
    2023-2-24;9:26:14.435;IR 1 ; beam restored ;
    2023-2-24;9:26:17.211;IR 2 ; broken beam ;
    2023-2-24;9:26:21.254;IR 2 ; beam restored ;
    2023-2-24;9:26:55.319;IR 1 ; broken beam ;
    2023-2-24;9:26:55.331;IR 2 ; broken beam ;
    2023-2-24;9:26:55.429;8000F33EDD41499D; A0;
    2023-2-24;9:26:55.838;IR 1 ; beam restored ;
    2023-2-24;9:26:55.850;IR 2 ; beam restored ;
    2023-2-15;12:54:5.553;System; Shut Down Button;
    ```

*NOTE* The time base is expressed at UTC+1 in summer mode (no shift in winter)
