# Contexte et cahier des charges

**1 - Cahier des charges**

Le but du projet est de concevoir et réaliser un dispositif d'identification et de capture d'oiseaux. Le dispositif devra réaliser les tâches principales suivantes :

- Être facilement montable et démontable sur les nichoirs préconçus
- Être résistant aux conditions extérieures
- Détecter l'entrée et la sortie de mésanges

- identifier les TAGs RFID, les horodater précisément et les enregistrer
- nigh time sleep mode
- paramétrable par l'utilisateur à l'aide d'un fichier texte
- Mesurer une température précise

- En capturer certaines selon leur identité


**2 - Valeurs clés et contraintes matérielles**

Voici quelques valeurs clés et contraintes matérielles qui détermineront la conception du dispositif :

- Dimensions d'environ 15x20cm avec profondeur déterminée par la capacité de l’oiseau à traverser cette profondeur dans le conduit de passage
- Utilisation d'une carte de développement Feather Adalogger pour la gestion des capteurs, actionneurs, et traçage sur carte SD
- Utilisation d'une paire de capteurs infra-rouge pour détecter les entrées/sorties
- Utilisation de la technologie RFID pour l'identification des oiseaux
- Utilisation d'un servomoteur pour actionner la fermeture du conduit de passage
- Utilisation d'une alimentation solaire