# Software configuration

The device configuration is split into two files:

* `hw_assem.cfg`: hardware and device identification parameters.
* `config.cfg`: functional and operating parameters.

These files allow the device to be adapted to the specific hardware and application requirements.

## Hardware configuration — `hw_assem.cfg`

The `hw_assem.cfg` file contains hardware identification and device specification parameters.

| Parameter name      | Description                                                                             | Default / example     |
| ------------------- | --------------------------------------------------------------------------------------- | --------------------- |
| `uid_mainboard`     | Unique identifier of the mainboard (FeatherM0), automatically retrieved by the software | Device-specific       |
| `uid_light_sensor1` | Unique identifier of light sensor 1, automatically retrieved by the software            | Installation-specific |
| `uid_light_sensor2` | Unique identifier of light sensor 2, automatically retrieved by the software            | Installation-specific |
| `uid_software`      | Unique software identifier used to identify the specific firmware version installed     | Installation-specific |
| `uid_experiment`    | Unique identifier of the experiment or project                                          | Installation-specific |
| `device_sn`         | Device serial number used to uniquely identify the physical unit                        | Empty                 |
| `battery_type`      | Type of battery used by the device                                                      | `liion_1s`            |
| `rtc_type`          | Real-Time Clock module used by the device                                               | `ds3231`              |

The `uid_light_sensor1`, `uid_light_sensor2`, `uid_software`, `uid_experiment` and `device_sn` parameters are specific to each installation and should be configured according to the deployed device.

## Functional configuration — `config.cfg`

The `config.cfg` file contains the parameters controlling the functional behavior of the device.

| Parameter name           | Description                                                                               | Values / default          |
| ------------------------ | ----------------------------------------------------------------------------------------- | ------------------------- |
| `use_buffer`             | Enables or disables the use of a temporary data buffer before writing data to the SD card | `{true, false}` — `false` |
| `enable_ir1`             | Enables or disables infrared sensor 1                                                     | `{true, false}` — `true`  |
| `enable_ir2`             | Enables or disables infrared sensor 2                                                     | `{true, false}` — `true`  |
| `enable_rfid`            | Enables or disables the RFID reader                                                       | `{true, false}` — `true`  |
| `rfid_mode`              | Defines how and when the RFID reader is activated                                         | `{0, 1, 2}` — `1`         |
| `enable_vbat`            | Enables or disables battery voltage measurement                                           | `{true, false}` — `true`  |
| `acquisition_interval_s` | Interval between two consecutive data acquisitions, in seconds                            | `[1..xx]` — `60`          |
| `schedule_start_hour`    | Operating schedule start hour                                                             | `[0..23]` — `10`          |
| `schedule_start_minute`  | Operating schedule start minute                                                           | `[0..59]` — `00`          |
| `schedule_end_hour`      | Operating schedule end hour                                                               | `[0..23]` — `18`          |
| `schedule_end_minute`    | Operating schedule end minute                                                             | `[0..59]` — `30`          |

The `schedule_start_*` and `schedule_end_*` parameters define the automatic operating period of the device. With the default values shown above, the operating period is **10:00 to 18:30**.

## RFID mode

The `rfid_mode` parameter defines how and when the RFID reader is activated.

| Value | Mode        | Behavior                                                                                                                                                                                                           | Power consumption |
| ----: | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
|   `0` | Disabled    | The RFID reader is switched off. No tag detection is performed.                                                                                                                                                    | Very low          |
|   `1` | Continuous  | The RFID reader remains continuously active and detects tags continuously.                                                                                                                                         | High              |
|   `2` | On IR event | The RFID reader is activated temporarily following a detection by an infrared sensor.This mode is suitable for relatively large or slow-moving animals that take sufficient time to pass through the RFID antenna. | Moderate          |

### Mode 0 — Disabled

The RFID reader is switched off and no RFID tag detection is performed.

This mode can be used when RFID functionality is not required.

### Mode 1 — Continuous

The RFID reader remains continuously active and can detect tags at any time.

This mode provides continuous RFID availability but results in higher power consumption.

### Mode 2 — On IR event

The RFID reader is activated temporarily following an event detected by an infrared sensor.

This mode reduces power consumption by activating the RFID reader only when an IR event occurs.

**Note:** Mode `2` requires at least one infrared sensor to be enabled (`enable_ir1` or `enable_ir2`).

## RFID activation timing

In mode `2`, the RFID reader is activated for a limited period following an IR event.

The default activation period is between **2 and 5 seconds**. A **1-second debounce period** is used to avoid repeated detections of the same tag.

These timings are predefined and do not need to be modified through the configuration file.

## Editing the configuration files

To modify a configuration file:

1. Remove the SD card from the device and insert it into a computer.
2. Locate the required configuration file (`hw_assem.cfg` or `config.cfg`).
3. Open the file with a text editor.
4. Modify the required parameters.
5. Save the file and reinsert the SD card into the device.

*NOTE:* Take care to preserve the file syntax when modifying configuration parameters. Incorrect formatting or invalid values may prevent the device from loading the configuration correctly.

If a required configuration file is not present on the SD card, the device can automatically create it with its default values.
