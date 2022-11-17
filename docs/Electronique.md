# Electronique

## Circuit général

Voir wiki sur Gitlab

## Consommation

### Mesures

Test consommation effectué avec une alimentation programmable (KEYSIGHT
N6705C).

Alimentation 5V du Feather M0 + RTC + RFID en acquisition

![D:\\screencapture2.gif](./media/image10.gif)

![Tableau courants](./media/image11.emf)

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

![Tableau autonomie](./media/image14.emf)

### Carte moyenne Puissance

Dakota 2010-0 TLB-30-BB LF

\\Projets\\RFID Tectus

![Clipboard - 23 février 2022 11_25](./media/image21.png)

## IR module

### Exemples/Tuto

* Comptage par franchissement d'une barrière infrarouge avec Arduino
UNO
<http://makerspace56.org/comptage-par-franchissement-dune-barriere-infrarouge/>

* Youtube la grotte du geek, code écrit par l\'environnement
STM32CubeIDE
<https://www.youtube.com/watch?v=\_tcBtZZDsCE>

* Adafruit "Using an Infrared Library on Arduino"
<https://learn.adafruit.com/using-an-infrared-library/sending-ir-codes>
