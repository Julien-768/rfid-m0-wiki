# How to restore the Feather M0 bootloader

## En cas de problème, regraver le bootloader avec J-LINK SWD

**Si le --offset a été oublié, la carte n'est pas récupérable, même avec J-LINK !**

Nous pouvons en cas de problème avec le bootloader, le regraver dans la carte. Il nous faut pour cela [le programme J-Flash](https://www.segger.com/products/production/flasher/tools/j-flash/about-j-flash/) et un boitier J-LINK.

Le boitier J-LINK et le feather M0 sont connecté par le swd. voici la [procédure et le fichier bootloader à regraver](https://learn.adafruit.com/proper-step-debugging-atsamd21-arduino-zero-m0/restoring-bootloader)

Le feather M0 est protégé par défaut. Il faudra [écrire un mot pour ôter la protection](https://roamingthings.de/posts/use-j-link-to-change-the-boot-loader-protection-of-a-sam-d21/)

## Pin out J-LINK SWD

![image](/assets/image/TO_SORT/SWD_pin.png)
