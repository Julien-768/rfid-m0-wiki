# Checking procedure

This page describes a simple procedure to check your hardware, either on the field or in your office.

## Before testing

1. Plug-in the battery
2. Check the SD memory card and the RTC battery are in their slots

<!-- markdownlint-disable MD033 -->
<a href="../media/Procedure_battery_connection_illustration.png">
<img src="../media/Procedure_battery_connection_illustration.png" alt= "battery connection" width="400">
</a>
<a href="../media/Procedure_external_component_illustration.png">
<img src="../media/Procedure_external_component_illustration.png" alt= "external component illustration" width="400">
</a>
<!-- markdownlint-enable MD033 -->

---

## Test procedure

### SD card and Real-Time Clock

We are going to check the SD card and the RTC are ok by checking the LEDs of the device.

1. Press the On/Off button (button pressed = On)
2. Press the switch button until the external red LED turns on. Once done, release the switch button. The external red LED should turn OFF after the startup of the device.
    * If the external red LED does not light up at all, check that the battery connector well plugged-in
    * If the external red LED does not turn OFF, open your device and check the internal red led
        * If it is blinking 2 times, the memory card is not found or is faulty, reinsert it or replace it.
        * If it is ON and fixed, the RTC battery might be faulty, replace it.

<!-- markdownlint-disable MD033 -->
<a href="../media/Procedure_led_illustration.png">
<img src="../media/Procedure_led_illustration.png" alt= "led difference" width="400">
</a>
<!-- markdownlint-enable MD033 -->

### Infrared beam

We are going to check if the infrared beams are working by checking the LED of the RFID reader. Indeed the RFID reader only reads tags (so its LED blinks) after an infrared event was detected.

1. Once the device started and the external red LED is off, pass your hand through the antenna. Check that the RFID reader lights turn on for a few seconds (flashing red light)
2. After a few seconds, remove the hand from the antenna Check that the RFID reader lights turn on for a few seconds (flashing red light)

*NOTE* As the angle of the IR cells is wide, it's important that the obstacle was quite large (hand, wrist - no small object)

<!-- markdownlint-disable MD033 -->
<a href="../media/Procedure_RFID_led_illustration.png">
<img src="../media/Procedure_RFID_led_illustration.png" alt= "RFID led" height="250">
</a>
<!-- markdownlint-enable MD033 -->

### RFID reader

We are going to check if the RFID reader is able to detect and read a RFID tag, by passing a tag into the antenna and check the led of the device.

1. Once the device started and the red LED is off, pass your hand with RFID tag through the antenna
2. Check that the external LED flashes briefly

*NOTE This test must be performed within 5 minutes after the system power-on. After this delay, the external red LED will be disables for energy saving reasons.*

&nbsp;

### SD card content and date / time

We are going to check if the SD card is correctly working (write data) and if the real-time clock is up-to-date by checking the content of the saved files.

1. Once the previous tests done, turn off the device and insert the SD memory card into a computer.
2. Check for a text file nammed with the current date (date format : YY_MM_DD.TXT). If it's the case, open it
3. In the file, check that the different events of the tests are present and that the associated time is correct.  
   At least 7 events should be present in the file :
      * "System start"
      * 2 events during infrared test : "broken beam" and "beam restored"
      * 3 events during RFID test : "broken beam", RFIG tag value and "beam restored"
      * "Shut Down Button"

*NOTE* The time base is expressed at UTC+1 in summer mode (no shift in winter)

## Device shutdown

1. Maintain the switch button pressed until the red LED stops blinking and remains On
2. Release the switch button
3. Press the On/Off button (button released = Off)
4. Disconnect the battery
