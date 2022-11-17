# Home

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

  mkdocs.yml    # The configuration file.
  docs/
      index.md  # The documentation homepage.
      ...       # Other markdown pages, images and other files.

## mkdocs.yml layout

```yml
  site_name: RFID_M0 *The name displayed at the top of your tab in the navigator*
  site_url:  'https://rfid_m0.pages.in2p3.fr/Doc_M0/'
  nav:
      - Section 1:
        - Title1: page1.md
        - Title2: page2.md
        - Sub-section:
          - Title3: page3.md
          - Title4: page4.md

  theme: readthedocs
```

## Gitlab CI / CD

use `.gitlab-ci.yml` and `requirements.txt`

Be sure not to have any warning on mkdocs. Test it with `mkdocs build --strict --verbose`

## Nichoir 2021 </summary>

* [contexte](Stage/contexte)
* [Stage-2021](Stage/Stage-2021)
* [Boitier](Stage/Boitier)
* [Liste des composants](Stage/composants)
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