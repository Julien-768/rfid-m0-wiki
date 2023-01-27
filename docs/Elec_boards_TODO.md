---
comments: true
---

# Electronique

## Main board 12V

* Passer le projet sous KICAD
* Passer le maximum de composants en CMS et s'assurer de l'assemblage par le sous-traitant
* Noter sur le schéma le nom des pins des connecteurs (actuellement vide, seul est noté le nom du connecteur)

## Power board 5V

* Passer le projet sous KICAD
* Passer le maximum de composants en CMS et s'assurer de l'assemblage par le sous-traitant
* Les capacités C2 100 nF et C3 100 nF sont à remplacer par des CMS du type 0805 105K X7R 50V SMD.
* Une piste de la carte power doit être coupée: celle qui connecte la tension batterie au power boost. Normalement un interrupteur d'arrêt doit permettre de couper l'alimentation entre batterie et le reste du système. Or cette piste fait une connexion permanente. [EDIT: Modif déjà apportée sur fritzing le 04/08/2022]
* La position des 4 trous est à changer. Deux sont trop proches du chargeur solaire (court circuit avec les vis), l'un trop proche du condensateur (court circuit) et l'autre trop proche du bornier à vis.

![Capture](./assets/image/TODO/Power_board%205V%20trous.png){: style="width:400px"}

## Power board 12V

* Passer le projet sous KICAD
* Passer le maximum de composants en CMS et s'assurer de l'assemblage par le sous-traitant

## Interface board

* Passer le projet sous KICAD
