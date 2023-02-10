---
comments: true
---

# Electronique

## Toutes les cartes

* Passer le projet sous KICAD
* Passer le maximum de composants en CMS
* Noter le nom des pins sur les 2 côtés des cartes

## Main board

* Noter sur le schéma le nom des pins des connecteurs (actuellement vide, seul est noté le nom du connecteur)
* Une fois les composants montés, la désignation de certains n'est plus visible : Q12 / Q13 / R8 / C3
* Le condensateur Q13 est monté plié avec sa référence vers le dessous, ce qui ne permet pas de connaître le composant une fois monté. Idéalement il faudrait inverser son sens de montage.
* Le connecteur JST PW_mng est trop près du condensateur Q12, ce qui rend délicate sa manipulation. Il faudrait remonter ce connecteur de quelques millimètres (ça pourrait d'ailleurs laisser de la place pour mettre la désignation de Q12).
* Le condensateur C1 gêne le passage du câble micro-USB. Il faudrait le décaler de 5 à 10 mm (et faire suivre sa désignation) vers la gauche pour avoir la place de passer l'USB et le manipuler avec les doigts.

![Capture](./assets/images/TODO/Main_board_mods.png){: style="width:400px"}

## Power board 5V

* Les capacités C2 100 nF et C3 100 nF sont à remplacer par des CMS du type 0805 105K X7R 50V SMD en taille 1206. C2 ne doit pas être un composant discret (génant une fois la carte fille placée).
* Une piste de la carte power doit être coupée: celle qui connecte la tension batterie au power boost. Normalement un interrupteur d'arrêt doit permettre de couper l'alimentation entre batterie et le reste du système. Or cette piste fait une connexion permanente. (Modif déjà apportée sur fritzing le 04/08/2022).
* La position des 4 trous est à changer. Deux sont trop proches du chargeur solaire (court circuit avec les vis). Un autre est trop proche du condensateur C4 (court circuit) . Un dernier est trop proche du bornier à vis.
* supprimer la double rangée du connecteur PW, une simple rangée suffit
* les pin PW GND et 5V ne sont pas visibles avec le condensateur plié, les mettre en bord de carte / agrandir de 2.54 mm la carte.

![Capture](./assets/images/TODO/Power_board%205V%20trous.png){: style="width:400px"}

## Power board 12V

* Prévoir les emplacements pour connecter les câbles des émetteurs infrarouge et des photo-transistors: 4 x 3V3 et 4 x GND.
* Enlever les empreintes sous les cartes Adafruit.

## Interface board

* Passer le projet sous KICAD
