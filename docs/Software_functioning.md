
# Functioning of the system

The system checks at regular intervals if the infrared barriers have been broken or restored. If an infrared event has occurred, the RFID sensor is read a number of times (**rfid_attempts** option).

Following this event, and according to the configuration (**mode_capture** option), a capture can be decided.

In case the infrared sensors are disabled, (**opt_IR_1** and **opt_IR_2** options set to false), the RFID reading is continuously done (Caution: this mode consumes a lot of battery).

If the temperature is required (**opt_temp_prec** option set to true), the system measures and records it at regular intervals (**delay_temp** option) only if it has varied by more than 0.02°c since the last record.

The battery voltage is also measured and recorded it if it has varied by more than 0.1V since the last record.

The system can operate all the day or according to an hourly schedule (**start_time** and **stop_time** options). The data (IR event, RFID tag, temperature...) are stored on the SD card with timestamp (UTC time).

## The capture mode

Be aware only advanced user should activate the capture mode! The **mode_capture** option can take a number from 1 to 4 :

1. *Recording of passages* Following an event on the infrared sensor, RFID reading. No capture.
2. *Capture any individual* Following an event on the infrared sensor, closing the door.
3. *Capture of specific tags* Following an event on the infrared sensor, RFID reading. If the tag is one of them described in parameters, closing the door.
4. *Capture untagged individuals* Following an event on the infrared sensor, RFID reading. If there is no tag, closing the door.

*Note :* For each modes, a security timeout opens the door after a certain duration (**release_time** option)

## Security of the system

The device is automatically powered-off if :

* the temperature exceeds 50°c
* the battery voltage falls below a threshold (BATTERY_MIN_VOLTAGE = 3V for Li-ion battery or 12V for Lead battery)

In addition, if the battery voltage passes below BATTERY_MIN_VOLTAGE + 0.1V, the sensor reading is suspended until the voltage is passed above BATTERY_MIN_VOLTAGE + 0.2V.

The door is automatically opened if :

* it has been closed for a certain duration (**release_time** option)
* system shutdowns in case of overheating or under voltage

## Error management

In case of errors, the external red LED turns on and the internal red LED blinks. Acording to the blinking frequency, it's possible to know the error :

* 2 times : Memory card not detected
* 3 times : Failed to write data on the SD card (memory can be corrupted)
* 4 times : Real-Time Clock battery has to be replaced. The program has to be compiled and uploaded again to reset the error

## Data description

There are several types of messages written into the SD memory card :

| Data type     | Message content                   | Comment                             |
|---------------|-----------------------------------|-------------------------------------|
| System        | Start                             |                                     |
| System        | RTC is ok                         |                                     |
| System        | RTC set time to compilation date  |                                     |
| System        | RTC lost power                    |                                     |
| System        | RTC has unknow error              |                                     |
| System        | Sleep mode                        |                                     |
| System        | Wake up mode                      |                                     |
| System        | Up                                | Still alive                         |
| System        | Shutdown : High temp              |                                     |
| System        | Shutdown : Battery low            |                                     |
| System        | Shutdown : User                   |                                     |
| Ax            | RFID tag                          |                                     |
| Irx           | Broken beam                       |                                     |
| Irx           | Beam restored                     |                                     |
| Temperature   | Temperature measurement in °c     | If temp. variation > 0.02°c        |
| Vbat          | Battery measurement in V          | If batt. variation > 0.1V          |
| Vbat          | Power saving                      | Battery < BATTERY_MIN_VOLTAGE + 0,1 |
| Vbat          | Battery restored                  | Battery > BATTERY_MIN_VOLTAGE + 0,2 |
| Vbat          | Battery check by user             |                                     |
| -             | UID mainboard & experiment        | First line of each data file        |
| Door          | Closed                            |                                     |
| Door          | Open : Init                       |                                     |
| Door          | Open : Release time               |                                     |
| Door          | Open : Security                   | High temp, Battery low, Error…      |
