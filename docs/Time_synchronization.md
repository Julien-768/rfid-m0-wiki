# Time synchronization

The main board have 2 sources of time :

* the Real-Time Clock : precise with a very small drift over time - Resolution : second
* the internal clock : drift over the time due to temperature variation or quartz precision - Resolution : millisecond or microsecond

This page describes how to use the two time sources to have a precise timestamp with millisecond resolution.

## Issue description

To build a timestamp with millisecond resolution, it's possible to get the time from the RTC and use the millis() variable modulo 1000.  
Example : 10:38:21 (RTC) & 12400 (millis) gives 10:38:21:400

But a **temporal offset** can appear between the two time sources if the main board is not turned on (so millis() is initialized at 0) at the exact moment of the RTC changes second.  

Example : Main board is turned 500ms after the RTC had passed the time 10:38:21. The different timestamps will be (4Hz acquisition) :

* 10:38:21:00
* 10:38:21:250
* 10:38:22:500
* 10:38:22:750
* 10:38:22:00
* ...

In addition of this offset, the **internal clock speed evolves over the time** (due to quartz and temperature) so that one second for the quartz can be slower or quicker than one second of the RTC. This behavior requires to apply synchronization correction over the time, and not only at startup.

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/User_description/Time_synchro_issue.jpg">
<img src="../assets/images/User_description/Time_synchro_issue.jpg" alt="Time synchronization issue" width="600" >
</a>
<!-- markdownlint-enable MD033 -->

## Parameter identification

The solution consists to periodically wait for the RTC change seconds, then save the millis() value. This will be used as an offset.

In addition, the drift of millis is estimated by making the difference between the offset just measured and the previous one. Then a slope correction factor is obtained by dividing the drift by the time elapsed from the last synchronization.

As **this operation is blocking and requires time** (up to 1 second) during which the sensors or user requests are not monitored, it should not be realized too frequently. The current delay between two synchronization operation is set to 5 minutes. In addition, this process is not realized if one acquisition is in progress.

## Correction applied

At each time the millisecond is required, a corrected value of millis is computed. It's expression :

$millisSynchro = (millis - offset) \cdot (1 - slope Correction Factor)$

Then a modulo 1000 is applied to return a value in [0 ; 999].
