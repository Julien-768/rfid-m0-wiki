# Technical specifications

The system is designed to be integrated into a [1150 hard case Pelicase](https://www.peli.com/eu/fr/product/cases/protector/1150) (210 x 170 x 100 mm).

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/User_description/1150_pelicase.jpg">
<img src="../assets/images/User_description/1150_pelicase.jpg" alt= "1150 Pelicase" width="350">
</a>
<!-- markdownlint-enable MD033 -->

The operating tempererature range is 0°c to 50°c.

## Memory

The system stores its data on a Micro-SD card. The maximal supported size is 32GB (SD and SDHC card supported).

## Powering

Several powering options are proposed :

1. 4.2v Li-ion battery
2. 12v Lead battery
3. 4.2v Li-ion battery and solar panel

## Consumption & Autonomy

TO DO : Ajouter autonomie + indiquer dans quel mode (24h ou période) + détail des consommations


## Consommation

### Mesures

Test consommation effectué avec une alimentation programmable (KEYSIGHT
N6705C).

Alimentation 5V du Feather M0 + RTC + RFID en acquisition

![D:\\screencapture2.gif](./media/image10.gif)

<object id="current" data="../media/current.htm" width="600" height="250"></object>

Puis test avec l'alim à la place de la batterie en 3.6V branchée sur le
PowerBoost

Tout compris RFID au repos

![D:\\screencapture3.gif](./media/image12.gif)

Tout compris RFID en acquisition

![D:\\screencapture4.gif](./media/image13.gif)

|                          |                 |                          |
|--------------------------|-----------------|--------------------------|
| Carte Feather M0 + RTC   |                 | <14mA>                     |
| Carte RFID Tectus + antenne   | Allumée au repos| <15mA>                     |
|                          | En acquisition  | 100mA sur 150ms          |
| Système Total            | RFID éteinte    | <0.18W>                    |
|                          | RFID au repos   | <0.26W>                    |
|                          | Acquisition (10 lectures RFID) | <0.38W>           |

Système Total:

* Carte Feather M0 + RTC
* Carte RFID Tectus + antenne
* 2 barrières IR
* Power Boost

### Calcul Autonomie

<object id="consumption" data="../media/consumption.htm" width="600" height="250"></object>

### Carte moyenne Puissance

Dakota 2010-0 TLB-30-BB LF

\\Projets\\RFID Tectus

![Clipboard - 23 février 2022 11_25](./media/image21.png)
