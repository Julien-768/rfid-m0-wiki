# How to reset the Real-Time-Clock without computer

When the RTC loses the time (caused by low voltage of the CR1220 coin cell battery or electromagnetic noise), the led flashes 4 times and the program refuses to start. The normal procedure to correct this issue is to reprogram the system (see [Programming section](./programming.md))

When the programming operation cannot be done (example: in the field without computer access), the RTC can be **set to a default date & time (00h00m00s the January 1st 2099)** so that the program continues to run. Then the clock will increment from that time.

The procedure to do it :

* Turn on the device
* Wait the LED blinks 4 times (indication that an issue occurs with the clock)
* Press the switch button at least 2 seconds : The LED should blink two times to indicate you that the reset is done
* Turn off the device (On / Off button) and restart it

Note : This procedure is only considered if an error with the clock occurs (blink 4 times). If there is no error, a long press will turn off the device (normal behavior).

This operation has to be considered as a back-up option, and the RTC still need to be reprogrammed at the correct date & time when it's possible.
