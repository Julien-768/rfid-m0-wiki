## Carte de développement

La Feather M0 Adalogger de Adafruit est une carte de développement de type Arduino spécialement conçue pour des applications d'enregistrement de données. Elle dispose de 256KB de mémoire flash, ce qui lui permet d'avoir un code plus volumineux que la plupart des modèles équivalents. Son slot microSD permet de ne pas manquer d'espace de stockage pour les données recueillies. **Cette carte fonctionne en niveau logique 3.3v, il faut donc faire attention à sa compatibilité avec les capteurs qui fonctionnent en 5v.**

<img src="uploads/ab0a254de9223f1644c0fdddce3d70b9/image.png" width="250">

[tutorial adafruit](https://learn.adafruit.com/adafruit-feather-m0-adalogger/pinouts)

## Servomoteur

Le servomoteur HS-53 de Hitec est adapté pour des systèmes miniaturisés ou économes en énergie. Sa vitesse de rotation est légèrement supérieure à un tour par seconde. L'alimentation optimale est de 5v, et il est commandé par PWM. Il peut délivrer un couple maximale d'environ 1,5 kg.cm

<img src="uploads/bb7554ebf1d3a945e45b4c43df6ee853/image.png" width="250">

https://asset.conrad.com/media10/add/160267/c1/-/gl/001081926ML01/mode-demploi-1081926-mini-servomoteur-analogique-hitec-hs-53-112053-1-pcs.pdf

## Module RTC

Ce capteur conserve la date, l'heure, les minutes et les secondes grâce à sa pile intégrée. Il nécessite donc une très faible alimentation. En cas de désynchronisation, une fonction du code permet de redéfinir l'instant présent pour l'horloge. Ce capteur communique en I2C. Ici aussi une alimentation 5v est recommandée, mais le capteur fonctionne aussi en 3.3v.

[page produit adafruit](https://www.adafruit.com/product/3013)

[tutorial adafruit](https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/downloads)

<img src="uploads/660ba6c3c82931b67449b63d54a7ff72/image.png" width="250">

## Module RFiD

Ce module permet à l'aide d'une antenne de détecter les tags RFiD à une portée de quelques centimètres. Il peut communiquer en TTL ou en RS-232. Cette carte est pratique comparé aux autres cartes disponible sur le marché car elle est relativement compacte et adaptée pour les projets de petite taille. Il faut aussi fournir l'antenne, mais cela peut être un avantage car on peut choisir comment l'intégrer au projet.

<img src="uploads/cc3bd4627da03c6eb6b14b72dc5d9966/carte_RFiD.png" width="350">

[pinout Connection drawing.pdf](uploads/81b7cef750505db74dd9b735ed8705fd/Connection_Drawing_TLB-30-SER.pdf)

[manuel de communication scotty.v1.4_TLB-30-Commands_.pdf](uploads/651a3e69d9c31fa0e2970c75e4627ca0/scotty.v1.4_TLB-30-Commands_.pdf)

## Capteur RTD

Le capteur RTD lit la température ambiante grâce à une résistance variable selon la chaleur. Sa plage de température est de 450 à -200 °C. Nous utiliseront une antenne à 2 fils, il faut alors souder certaines pistes sur le PCB pour adapter le capteur à ce mode de fonctionnement. On soudera les pastilles *2/3 wire* et *2 wire* et on s'assurera de connecter les fils de l'antenne aux bornes *F+* et *F-*.

<img src="uploads/a9d3760123072bac216f86adc6a7d2b9/image.png" width="250">

[page produit adafruit](https://www.adafruit.com/product/3328)
[tutorial adafruit](TODO)

## Barrière infrarouge new version

Cette nouvelle barrière infrarouge, comparée à la précédente filtre les rayonnements infrarouges ambiants naturels, et s'affranchit de la luminosité de l'environnement.

### Description
La barrière infrarouge utilise le principe et les composants destinés aux télécommandes infrarouges. En effet on émet une lumière pulsée infrarouge à une certaine fréquence (36kHz). En face on place un photo détecteur qui passe à l'état bas seulement si il détecte un rayonnement IR à cette fréquence. Ainsi Ces capteurs infrarouge fonctionnent en tout ou rien. On ne peut pas régler la distance de détection. Plus le rayonnement Infrarouge est intense plus la barrière infrarouge peut être grande (plusieurs mètres).

### Émetteur Infrarouge
Cathode (-) patte la plus courte (pas de méplat visible)

<img src="uploads/faf76029d4c4bf6ed90eff264ebd9dab/image.png" width="250">

Le code pour établir une PWM à 36kHz:

Librairie utilisé: https://github.com/ocrdu/Arduino_SAMD21_turbo_PWM

![IR_pulse_code](uploads/2c382b5486b75d76924971f6a84affcd/IR_pulse_code.PNG)

### Phototransistor TSOP34536
 Alimentation de 2.5V à 5.5V

![phototransistor](uploads/9e841f54ce27092b014421e1b7e74c72/phototransistor.PNG)

datasheet:
[datasheetTSOP34536.pdf](uploads/8c364017c2e34e7aed8ab30ff57f4c3e/datasheetTSOP34536.pdf)

## Barrière infrarouge old version

### Description

Ces capteurs infrarouge fonctionnent en tout ou rien. On règle une distance de détection avec le potentiomètre, et la sortie prend une valeur haute ou basse si un objet est respectivement plus proche ou plus loin que la distance de détection. Leur alimentation se fait généralement en 5v, mais il fonctionne aussi en 3.3v.

<img src="uploads/2116a3d83b1eb3c58dc7e8d3c8b8c6b5/image.png" width="250">
<img src="uploads/d8ad1684a7808f5a271e3d7f4a0bd68f/image.png" width="450">

### Modification à effectuer sur les cartes

![image](uploads/08557c49b6ed47a1972f5dd9f98d7b64/image.png)

- désactivation des indicateurs lumineux, suppression des résistances en série avec les LED. 
- Remplacement de la résistance de 10k en série avec le phototransistor par une d’environ 50k afin de diminuer la tension sur l'entrée + du comparateur
- Suppression de la résistance de 10k en sortie et activation de la résistance de pull-up interne coté microcontrôleur

### Émetteur Infrarouge
Même émetteur que la nouvelle version. 

### Phototransistor
Montage en Emetteur Commun donc Emetteur à la masse, Collecteur vers la sortie logique
<img src="uploads/51c599fe2181283b8a9d903a5f54943d/image.png" height="250">