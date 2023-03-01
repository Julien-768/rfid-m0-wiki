# Home

## Nichoir 2021 </summary>

* [contexte](Stage/contexte)
* [Stage-2021](Stage/Stage-2021)
* [Boitier](Stage/Boitier)
* [Manuel d'assemblage](Stage/Manuel-d'assemblage)

Un même projet pour deux applications:

* un nichoir "intelligent" pour mésanges
* une antenne terrier pour Hamsters sauvages

Chaque application possède sa propre conception mécanique. Mais la programmation et l'électronique sont partagées.

## Description du fonctionnement en commun

Les deux systèmes ont en commun :

* Système embarqué à placer en milieu naturel (forêt, champs)
* 1 ou 2 détections IR pour détecter la présence d'un animal
* une antenne RFID pour la lecture d'un transpondeur dans l'animal
* l'enregistrement des données sur une carte SD
* Gestion de la batterie pour un fonctionnement avec panneau solaire

## Les outils de développement

### Mécanique

* Antenne terrier sur Siemens NX
* Nichoir sur Top Solid

## Carte Electronique

* Schéma et routage des cartes sur fritzing.
* Schémas plus générals sur EasyEDA, Projet "Nichoir_RFID".

## Programmation

### Plateform IO sur VSCode

Pour le développement du programme informatique.

### Utilisation de JLink sur Plateform IO

A venir...

<!--
TODO: [Installer_JLink_sur_Arduino_Feather_M0_avec_VScode_et_platform_IO.docx](./uploads/a56c5ae2038a9a6447f9fe94b2979012/Installer_JLink_sur_Arduino_Feather_M0_avec_VScode_et_platform_IO.docx
-->

<!--
TODO: Enlever / mettre à jour les fichiers du nichoir 2021
-->