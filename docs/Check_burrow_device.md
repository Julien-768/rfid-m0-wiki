# Check the device

The aim of this page is to describe how to check the device once just assembled.

## Step 1 : Follow the user checking procedure

Start by following the different steps described in the [User Checking Procedure](/docs/Checking_procedure.md). Once the tests realized, check the content of the SD card in order to verify :

* Data are written into the SD memory card
* All the events are detected and written (IR events, RFID tag value, system start and shut down...)
* The RTC is up-to-date

## Step 2 : Edit the configuration file

1. Open the CONFIG.cfg file in the SD memory card
2. Edit the option "mode_time_period" to true
3. Edit the option "start_time" by setting an hour higher than the current (in UTC timezone)
4. Edit the option "stop_time" by setting start_time + 2h
5. Save the file and insert the SD card into the device
6. Turn on the device and wait a few minutes
7. Check that the system does not read the sensor by passing a RFID tag into the antenna and checking the external red led does not blink

If this test does not succeed, check the configuration file format is correct (refers to [Configuration](/docs/Software_configuration.md) for details).

## Step 3 : Check the battery management

1. Replace the battery by an external power supply and set the voltage (4v for Li-ion device / 13v for lead battery)
2. Turn on the device and wait a few minutes. Then modify the power supply voltage (2.9 for Li-ion device / 11.9v for lead battery)
3. Check that the system is automatically powered-off by passing a RFID tag into the antenna and checking the external red led does not blink. All others leds should also remain off.

If this test does not succeed or if the voltage value is not consistent with your battery, check the parameters **BATTERY_MIN_VOLTAGE** and **POWER_BOARD_BATT_RATIO** into the code.
