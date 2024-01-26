# Software configuration

The software is customizable by the user to active sensors, working time and behavior.

## Configuration file

The software options are editable in the configuration file "CONFIG.cfg" located on the SD card.

??? "Configuration file with default values"

    ```
    {
    "opt_IR_1":true,
    "opt_IR_2":true,
    "opt_temp_prec":false,
    "delay_temp":60,
    "tag_type":"FDX",
    "rfid_attempts":10,
    "delay_tag_save":1,
    "mode_time_period":false,
    "start_time":5,
    "stop_time":23,
    "delay_loop":10,
    "release_time":10,
    "close_time":1,
    "mode_capture":1,
    "tag_1":"01101728E6",
    "tag_2":"01101728E6",
    "tag_3":"01101728E6",
    "tag_4":"01101728E6",
    "tag_5":"01101728E6"
    }
    ```

The file is written as a [JSON string](https://developers.squarespace.com/what-is-json), take care to keep quotes and commas intacts when modifying the file.

## How to edit the file

To change the configuration file:

1. Take the SD card from the device and insert it into a computer
2. Look for CONFIG.cfg file and open it
3. Change the value of the required parameters
4. Save your modifications and insert back the SD card into the device

_NOTE_ If the configuration file is not present into the SD card, the device will automatically create it with default values

## Parameters description

Here is an explanation of the parameters you can tune, possible values to change in the configuration file are described.

| Parameter name   | Associated feature                                                                | Values            |
| ---------------- | --------------------------------------------------------------------------------- | ----------------- |
| opt_IR_1         | activation of infrared beam 1                                                     | {true , false}    |
| opt_IR_2         | activation of infrared beam 2                                                     | {true , false}    |
| opt_temp_prec    | activation of temperature sensor                                                  | {true , false}    |
| delay_temp       | delay (in second) between two consecutive temperature sensor checks               | [1..xx]           |
| tag_type         | TAG type supported                                                                | {"FDX", "EM4102"} |
| rfid_attempts    | how many times the RFID will check for the presence of a TAG after an IR event    | [1..xx]           |
| delay_tag_save   | delay (in second) between two consecutives records of the same TAG on the antenna | [1..xx]           |
| mode_time_period | activation only between start_time and stop_time hours                            | {true ; false}    |
| start_time       | start hour of the system in mode_day_only (UTC time)                              | [0..23]           |
| stop_time        | stop of the system in mode_day_only (UTC time)                                    | [0..23]           |
| delay_loop       | delay (in millisecond) between two consecutive sensor checks                      | [1..10000]        |
| release_time     | time in seconds for a release after any capture (security)                        | [0..xx]           |
| close_time       | time in seconds to wait before closing the door                                   | [0..xx]           |
| mode_capture     | capture mode selection                                                            | {1,2,3,4}         |
| tag_1            | part of the tag number for the capture of specific individuals                    |                   |
| tag_2            | part of the tag number for the capture of specific individuals                    |                   |
| tag_3            | part of the tag number for the capture of specific individuals                    |                   |
| tag_4            | part of the tag number for the capture of specific individuals                    |                   |
| tag_5            | part of the tag number for the capture of specific individuals                    |                   |

_Notes :_ Be careful to specify a mode compatible with the rest of the configuration. Modes 2 and 4 require at least one infrared sensor activated (**opt_IR_1** or **opt_IR_2** set to true).
