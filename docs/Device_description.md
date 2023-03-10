# Device description

The purpose of this system is to monitor and capture certain individuals.
A circular antenna, equipped with sensors and placed at the entrance of a burrow, can detect the passage of individuals and read their RFID tags (if existing).
All this data is collected on an memory card with timestamp.

Depending on the system setting, it is also possible to capture individuals who have crossed the antenna.
Several capture modes are available:

* No capture
* Capture of all individuals
* Capture individuals with a specific tag
* Capture of individuals without tags

The entire system is contained in a case for easy transport and installation.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/User_description/Complete_system.jpg">
<img src="../assets/images/User_description/Complete_system.jpg" alt= "Complete system" height="300">
</a>
<!-- markdownlint-enable MD033 -->

## Technical specifications

* Autonomy: 7 days
* Power source: 4.2v Li-ion battery or 12V lead battery (a solar panel can be added in Li-ion version)
* Compatible tag: FDX/ EM4102
* Case dimensions: 210 x 170 x 100 mm
* Memory type : Micro-SD card
* 24h operation or according to an hourly schedule

## System constitution

The system consists of a terrier antenna and a case.
The antenna incorporates two infrared transmitters / receivers as well as an RFID antenna.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/User_description/Antenna_details.png">
<img src="../assets/images/User_description/Antenna_details.png" alt= "Antenna details" height="300">
</a>
<!-- markdownlint-enable MD033 -->

The case contains all the embedded electronics, the battery, the clock, the micro-SD memory card and the start-up buttons.
On the outside of the case you'll find:

* A main switch button : Used to connect / disconnect the system with the battery
* A switch button : Used to power-on / power-off the system
* A red LED : Used by the system to interact with the user

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Procedure/External_component.png">
<img src="../assets/images/Procedure/External_component.png" alt= "External component" height="300">
</a>
<!-- markdownlint-enable MD033 -->

Inside the case is:

* A battery (4.2V Li-ion or 12V Lead version)
* A slot for the micro-SD memory card
* A CR1220 3V battery for the Real-Time Clock

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/User_description/Internal_component.png">
<img src="../assets/images/User_description/Internal_component.png" alt= "Internal component" height="300">
</a>
<!-- markdownlint-enable MD033 -->

---

## Functioning of the system

The system checks at regular intervals (delay_loop parameter) if the infrared barriers have been broken or restaured. If an infrared event has occurred, the RFID sensor is read a number of times (rfid_attempts parameter). The data (IR event and tag) are then stored on the SD card

If capture mode 2 (all individuals) has been set, the door is closed immediately after the infrared event.
If you have set the capture mode 3 (specific tags), the door is closed if the RFID tag read corresponds to one of the 5 described in the configuration file.
If you have set the capture mode 4 (untagged), the door is closed if the system has not detected a tag during the different reading attempts.

In case the infrared sensors are disabled, (opt_IR_1 & opt_IR_2 parameters set to false), the RFID reading is continuously done (Caution: this mode consumes a lot of battery).

If the temperature is required (opt_temp_prec parameter set to true), the system measures and records it at regular intervals (delay_temp parameter) only if it has varied by more than 0.02°c since the last record.

The system also measures the battery voltage, and records it if it has varied by more than 0.1V since the last recording.

## Security of the system

If the temperature exceeds 50°c or the battery voltage falls below a threshold (BATTERY_MIN_VOLTAGE = 3V for Li-ion battery or 12V for Lead battery), the device is powered-off.

In addition, if the battery voltage passes below BATTERY_MIN_VOLTAGE + 0.1V, the sensor reading is suspended until the voltage is passed above BATTERY_MIN_VOLTAGE + 0.2V.

If the door has been closed for a certain duration (release_time parameter), it is reopened. In addition, the door is opened before each system shutdown in case of overheating or under voltage.

## Error management

In case of errors, the external red LED turns on and the internal red LED blinks. Acording to the blinking frequency, it's possible to know the error :

* 2 times : Memory card not detected
* 3 times : Failed to write data on the SD card (memory can be corrupted)
* 4 times : Real-Time Clock battery has to be replaced. The program has to be compiled and uploaded again to reset the error

---

## Q & A

### How to use the device?

The antenna must be positioned at the entrance of the burrow so that individuals can pass through. Once the coil and case are installed, power-on the system and check it's working correctly.

### How to power-on / power-off the device?

Check the battery is connected then press the main switch (with power symbol, pressed = On)
Press the switch button until the external red LED turns on. Once done, release it. The external red LED should turn OFF after the startup of the device.

To power-off the device, maintain the switch button pressed until the external LED stops blinking and remains on. Once done, press the main switch (released = Off) and disconnect the battery.

### How to check the device is correctly working?

To check the system is working properly during a start-up, refers to the [Checking procedure](Checking_procedure)

### How to check that the system is still working (battery are OK)?

Quickly press and release the switch button (t < 0.5 second). If the system is still powered, the external red LED should briefly blinks.

### How to access to the recorded data?

Once the system off, open the case. Unlock the memory card (one push to lock / unlock the micro-SD card) and get it.
Insert it into a computer and access its contents. Data are stored in text format in files named with date and time (format YY_MM_DD.TXT).
Do not rename SD card files
