# Software configuration

The microcontroller program has some parameters that can be configured by a configuration file. User can then personnalize its program.
The file is located into the SD card ("CONFIG.txt") and respects the [JSON format](http://json.com/).

---

## Parameters description

| Parameter name | Associated feature | Values |
| ------ | ------ | ------ |
| opt_IR_1 | activation of infrared beam 1 | {true , false}
| opt_IR_2 | activation of infrared beam 2 | {true , false}
| opt_temp_prec | activation of temperature sensor | {true , false}
| delay_temp | delay (in second) between two consecutive temperature sensor checks | [1..xx]
| tag_type | TAG type supported | {"FDX", "EM4102"}
| rfid_attempts | how many times the RFID will check for the presence of a TAG after an IR event | [1..xx]
| delay_tag_save | delay (in second) between two consecutives records of the same TAG on the antenna | [1..xx]
| mode_time_period | activation only between start_time and stop_time hours | {true ; false}
| start_time | start hour of the system in mode_day_only | [0..23]
| stop_time | stop of the system in mode_day_only  | [0..23]
| delay_loop | delay (in millisecond) between two consecutive sensor checks | [1..10000]
| release_time | time in seconds for a release after capture (security) | [0..xx]
| mode_capture | capture mode selection | {1,2,3,4}
| tag_1 | tag to captur in mode 3 (National Identification Code format) |
| tag_2 | tag to captur in mode 3 (National Identification Code format) |
| tag_3 | tag to captur in mode 3 (National Identification Code format) |
| tag_4 | tag to captur in mode 3 (National Identification Code format) |
| tag_5 | tag to captur in mode 3 (National Identification Code format) |

---

## Edit parameters

To change the values of the parameters :

1. Insert the SD card into a computer
2. Check for CONFIG.txt file and open it
3. Change the value of the required parameters
4. Save your modifications and insert the SD card into the device

*NOTE* If the CONFIG.txt file is not present into the SD card, the device will automatically create it with default values

??? "File content example with default values"

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
    "mode_capture":1,
    "tag_1":"01101728E6",
    "tag_2":"01101728E6",
    "tag_3":"01101728E6",
    "tag_4":"01101728E6",
    "tag_5":"01101728E6"
    }
    ```

---

## The 4 operating modes

### 1 : Recording of passages

Following an event on the infrared sensor, RFID reading. No capture.

### 2 : Capture everyone

Following an event on the infrared sensor, closing the door.

### 3 : Capture of specific tags

Following an event on the infrared sensor, RFID reading. If the tag is one of them described in parameters, closing the door.

### 4 : Capture untagged individuals

Following an event on the infrared sensor, RFID reading. If there is no tag, closing the door.

*NOTE* For each modes, a security timeout opens the door after a certain duration (parameter release_time)

---

## Parameters incompatibility

Be careful to specify a mode compatible with the rest of the configuration. The mode 2 and 4 requires at least one infrared sensor activated (opt_IR_1 or opt_IR_2 set to true).
