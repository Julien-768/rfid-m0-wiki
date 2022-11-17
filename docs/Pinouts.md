# Pinout feather M0 Adalogger

![Pinout_Feather_M0](./uploads/27c35323531a6092eb5c8f3a0b34f158/Pinout_Feather_M0.png)

## Schéma du circuit d'acquisition

Le système électronique est constitué de composants fonctionnant à différentes tensions:

* 5v (rouge) pour le servomoteur, le module RFiD, le feather M0 et un régulateur 3V3
* 3V3 provenant du feather (marron) qui alimente de manière permanente la RTC
* 3V3 provenant du régulateur (orange) qui alimente émetteurs et récepteurs IR, et le module MAX31865

On distingue les IO en bleu, l'alimentation de la carte en 5V en rouge, et la masse en noir. Plusieurs pins de communication de la carte Feather M0 sont utilisés, notamment les pins de communication I2C pour le RTC, SPI pour le RTD et UART pour le module RFiD.

![Nichoir_main_schéma](./uploads/7d0519200c182f8dde2e305f0a5f2c08/Nichoir_main_schéma.png)

Pour l'alimentation de cette carte d'acquisition se référer à la section [Power Supply](https://gitlab.in2p3.fr/Julien/feather_m0/-/wikis/Power-supply)
