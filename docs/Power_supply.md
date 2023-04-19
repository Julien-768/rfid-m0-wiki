# 1

## 2

### Lecture de la tension de batterie

La tension d'une batterie LiPo ou de 3 piles AA en série peut monter jusqu'à 4.2V. Cependant, les pins du feather M0 n'acceptent pas plus de 3V3.
Pour s'en affranchir, un pont diviseur composé de deux résistances de 100k (R1 et R2) divise par 2 la tension. Pour éviter les variations brusques de tension pour des condensateurs (C2 et C4) stabilisent la mesure.

Au niveau informatique, la tension de batterie est mesurée à chaque boucle. Si celle-ci baisse d'un certain seuil (>0.1V) entre deux mesures, La tension de la batterie est enregistrée sur la carte SD.

### Mise hors tension du système

<--Manual-->

Pour un stockage long ou une remise à zéro complète du dispositif, un interrupteur ON / OFF coupe physiquement la connexion à la source d'alimentation. Pour une coupure propre du dispositif, un interrupteur à poussoir permet une mise hors-tension contrôlée et évite par exemple de corrompre la carte SD.

<--Manual-->

Pour cette dernière méthode nous nous sommes inspiré de ce [tuto_mise_hors_tension](https://github.com/craic/arduino_power/blob/master/PowerOnPowerOff.md)

<!-- markdownlint-disable MD033 -->
<a href="../assets/images/Power_board/power_on_power_off_cycle.png">
<img src="../assets/images/Power_board/power_on_power_off_cycle.png">
</a>
<!-- markdownlint-enable MD033 -->

Grâce à cette électronique, le software peut commander l'éteignage du dispositif (par exemple lorsque la lecture de la batterie est inférieure à un certain seuil).
