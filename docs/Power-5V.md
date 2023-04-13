# Gestion de l'alimentation

## Schéma général

TODO Power_schematic_Solar ./uploads/cc060599fc783c6a9b7c883c04c23b48/Power_schematic_Solar.png

### schéma carte électronique power

Réalisation du routage de la carte sur fritzing.

![Nichoir_power_schéma](./uploads/81bacffe2d04e76404eac895cc852ee1/Nichoir_power_schéma.png)

### Lecture de la tension de batterie

La tension d'une batterie LiPo ou de 3 piles AA en série peut monter jusqu'à 4.2V. Cependant, les pins du feather M0 n'acceptent pas plus de 3V3.
Pour s'en affranchir, un pont diviseur composé de deux résistances de 100k (R1 et R2) divise par 2 la tension. Pour éviter les variations brusques de tension pour des condensateurs (C2 et C4) stabilisent la mesure.

Au niveau informatique, la tension de batterie est mesurée à chaque boucle. Si celle-ci baisse d'un certain seuil (>0.1V) entre deux mesures, La tension de la batterie est enregistrée sur la carte SD.

### Mise hors tension du système

<--Manual-->

Pour un stockage long ou une remise à zéro complète du dispositif, un interrupteur ON / OFF coupe physiquement la connexion à la source d'alimentation. Pour une coupure propre du dispositif, un interrupteur à poussoir permet une mise hors-tension contrôlée et évite par exemple de corrompre la carte SD.

<--Manual-->

Pour cette dernière méthode nous nous sommes inspiré de ce [tuto_mise_hors_tension](https://github.com/craic/arduino_power/blob/master/PowerOnPowerOff.md)

![power_on_power_off_cycle](./uploads/dbb5399d875f8005a4195ebcb86efcf1/power_on_power_off_cycle.png)

Grâce à cette électronique, le software peut commander l'éteignage du dispositif (par exemple lorsque la lecture de la batterie est inférieure à un certain seuil).

## Materials 

### Power Boost 1000

![Picture Power Boost 1000](./uploads/0029515fed85eaf8461fe78d5a7cb2dc/image.png){: style="width:200px"}

Le power boost 1000 donne une tension fixe de sortie 5v à partir d'une **tension d'entrée** pouvant varier de **1.8V à 5.5V**. Il peut délivrer jusqu'à 1A de courant. Ceci permet d'utiliser une batterie LiPo pour notre montage.

[tutorial adafruit](https://learn.adafruit.com/adafruit-powerboost-1000-basic)

[datasheet du composant](https://www.ti.com/product/TPS61090)

### Chargeur solaire

![Picture USB Solar charger](./uploads/12ecee4b00c4c12b1f16219b8650330b/image.png){: style="width:300px"}

Cette carte permet de gérer la charge d'une batterie LiPo 3.7V, soit à l'aide d'un panneau solaire, soit à l'aide d'une entée USB. Lorsque le panneau est ensoleillé, il se peut qu'au lieu de charger la batterie le courant soit directement utilisé pour alimenter le système en aval. La **tension en sortie** de la carte peut fluctuer entre **3.7V et 5V** (tension USB ou batterie LiPo). Le connecteur Jack est prévu pour un panneau solaire 5V et directement relié à VBUS / IN du bq24074, on peut donc indépendamment relier le panneau solaire ou l'entrée USB sur la pin / tension VBUS. Pour plus de détails, se référer au schéma électronique de la carte disponible sur le [tutoriel adafruit](https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout/overview)

### Panneau solaire

Ce panneau solaire a une puissance de 2.5W, il peut délivrer un courant jusqu'à 5V et de 500mAh. Il a des dimensions de 130cm x 150cm.

![Picture Solar Panel](./uploads/bf29a7820a5c6480eda9644d8de9b0cd/image.png)

### Batterie

La batterie utilisée est une batterie Li Polymer de 3.7v et de 1.5Ah. Ces batteries ont la particularité de présenter une tension de 4.2v en charge maximale, puis elles descendent rapidement à 3.7v.
