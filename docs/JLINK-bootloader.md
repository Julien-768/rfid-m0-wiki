# How to restore the Feather M0 bootloader

## In case of problem, reburn the bootloader with J-LINK SWD

**If the --offset was forgotten, the card is not recoverable, even with J-LINK!**

In case of problem with the bootloader, the feather board can be reburned. To do this, it's required to have :

- [the J-Flash program](https://www.segger.com/products/production/flasher/tools/j-flash/about-j-flash/)
- [a J-LINK Debug probe](https://www.segger.com/products/debug-probes/j-link/models/j-link-base/)

The J-LINK Debug probe and the Feather M0 are connected together by an SWD connector on the SWDIO / SWCLK pins (back side of the Feather). Follow the [procedure](https://learn.adafruit.com/proper-step-debugging-atsamd21-arduino-zero-m0/restoring-bootloader) to burn the bootloader.

<a href="../assets/images/Tech_doc/Feather_SWD_pin.jpg">
<img src="../assets/images/Tech_doc/Feather_SWD_pin.jpg" alt= "SWD pinout" height="200">
</a>

Note: The Feather M0 is write protected. It will be necessary to [write a word to remove the protection](https://hackaday.io/page/5997-programming-a-samd-bootloader-using-jlink-linux).
