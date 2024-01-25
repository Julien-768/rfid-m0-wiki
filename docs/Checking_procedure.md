# Checking procedure

This page describes a simple procedure to check your hardware, either on the field or in your office.

## Before testing

1. Plug-in the battery
2. Check the SD memory card and the RTC battery are in their slots

<a href="../assets/images/Procedure/Battery_connection.png">
<img src="../assets/images/Procedure/Battery_connection.png" alt= "battery connection" width="375">
</a>
<a href="../assets/images/Procedure/External_component.png">
<img src="../assets/images/Procedure/External_component.png" alt= "external component illustration" width="375">
</a>

---

## Test procedure

### SD card and Real-Time Clock

We are going to check the SD card and the RTC are in order by checking the LEDs of the device.

1. Press the main switch (with power symbol, pressed = On)
2. Press the switch button until the red LED turns on. Once done, release it. The red LED should turn OFF after the startup of the device.
   - If the red LED does not light up at all, check that the battery connector is well plugged-in
   - If the red LED is blinking 2 times, the memory card is not found or is faulty, reinsert it or replace it.
   - If the red LED is blinking 4 times, the CR1220 coil cell battery might be faulty, replace it. Then the main board must be [reprogrammed](./programming.md)

### Infrared beam

We are going to check if the infrared beams are working by checking the RFID reader's LED. The RFID reader only tries to read tags after an infrared event is detected, and this causes its LED to blink.

1. Once the device is started and the red LED is off, set your finger on one of the infrared receivers. Check that the RFID reader light turns on for a few seconds (flashing red light)
2. After a few seconds, remove your finger and check that the RFID reader light stays on for a few seconds (flashing red light)
3. Repeat the same operation with the second infrared receiver

_NOTE_ As the angle of the IR cells is wide, it is important to properly cover the infrared receiver.

It is possible to differentiate the bigger diameter of the IR receiver from the emitter. In addition, The receiver is mounted on the right side of the antenna.

<a href="../assets/images/Procedure/RFID_led.png">
<img src="../assets/images/Procedure/RFID_led.png" alt= "RFID led" height="250">
</a>
<a href="../assets/images/Procedure/IR_receiver.png">
<img src="../assets/images/Procedure/IR_receiver.png" alt= "IR receiver" width="300">
</a>

### RFID reader

We are going to check if the RFID reader is able to detect and read a RFID tag, by passing one into the antenna and checking the red LED.

1. Pass your hand with a tag through the antenna
2. Check that the red LED flashes briefly

_NOTE_ This test must be performed within 5 minutes after the system power-on. After this delay, the red LED will be disabled for energy saving reasons.

### Device shutdown

1. Maintain the switch button pressed until the red LED stops blinking and remains on
2. Release the switch button
3. Press main switch (released = Off)
4. Disconnect the battery

### SD card content and date / time

We are going to check if the SD card is correctly working (write data) and if the real-time clock is up-to-date by checking the content of the saved files.

1. Once the previous tests are done, turn off the device and insert the SD card into a computer
2. Check for a text file nammed with the current date (date format : YY_MM_DD.TXT). If it is the case, open it
3. In the file, check that the different events of the tests are present and that the associated time is correct
   - If the time is not correct
     - [Reprogram](./programming.md) the micro-controller to set up the time
     - check the RTC battery

??? "File content"

    ```
    2023-5-4;13:4:3.123;MB202303001;inv_mainboard;uid_experiment;202303YH001;
    2023-5-4;13:4:3.123;MB202303001;inv_mainboard;System;Start;
    2023-5-4;13:4:10.123;MB202303001;inv_mainboard;System;RTC is ok;
    2023-5-4;13:4:28.301;2303002591056;inv_rfid_sensor;IR 2;broken beam;
    2023-5-4;13:4:31.870;2303002591056;inv_rfid_sensor;IR 2;beam restored;
    2023-5-4;13:4:33.871;2303002591056;inv_rfid_sensor;IR 1;broken beam;
    2023-5-4;13:4:35.263;2303002591056;inv_rfid_sensor;IR 1;beam restored;
    2023-5-4;13:4:38.71;2303002591056;inv_rfid_sensor;IR 2;broken beam;
    2023-5-4;13:4:38.94;2303002591056;inv_rfid_sensor;IR 1;broken beam;
    2023-5-4;13:4:38.586;2303002591056;inv_rfid_sensor;A0;972-270000015773;
    2023-5-4;13:4:41.198;2303002591056;inv_rfid_sensor;IR 1;beam restored;
    2023-5-4;13:4:41.308;2303002591056;inv_rfid_sensor;IR 2;beam restored;
    2023-5-4;13:4:44.267;MB202303001;inv_mainboard;Vbat;Battery check by user;
    2023-5-4;13:4:44.267;MB202303001;inv_mainboard;Vbat;3.62V;
    2023-5-4;13:4:50.871;MB202303001;inv_mainboard;System;Shutdown : User;
    ```

_NOTE_ The time base is expressed in UTC time period
