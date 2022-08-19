Le programme du microcontrôleur possède des paramètres configurables. Un fichier de configuration au format texte présent sur la carte SD : "CONFIG.txt" permet d'y avoir accès. L'utilisateur peut ainsi personnaliser son programme.


## Fichier de configuration

| nom variable| fonctionnalité contrôlé | valeurs possibles |
| ------ | ------ | ------ |
| opt_IR_1 | activation du faisceau infrarouge 1 | {true , false}
| opt_IR_2 | activation du faisceau infrarouge 2 | {true , false}
| opt_temp_prec | activation du capteur de température | {true , false}
| opt_servo| activation de la porte de capture | {true , false}
| delay_loop | temps de repos avant de vérifier données capteurs | xx
| tag_type | type de TAG supporté | {"FDX", "EM4102"}
| rfid_attempts | combien de fois la RFID va vérifier la présence d'un TAG après un évènement IR| [1..xx]
| delay_tag_save | temps en secondes pour enregistrer un TAG sur l'antenne | [1..xx]
| delay_temp | période en secondes pour l'enregistrement de la température | [1..xx]
| mode_day_only | mise en sommeil durant la nuit | {true ; false} 
| start_time | heure de démarrage du système en mode_day_only | [0..23]
| stop_time | heure de mise en veille du système en mode_day_only | [1..24]
| mode_capture | sélection du mode de capture | {1,2,3,4}
| delay_loop | temps minimal en millisecondes avant interrogation des capteurs | [1..10000]
| servo_bird_release_time | temps en secondes avant le relaché d'un oiseau par sécurité | [0..xx]
| tag_1 | tag à capturer en capture mode 3 |
| tag_2 | tag à capturer en capture mode 3 |
| tag_3 | tag à capturer en capture mode 3 |
| tag_4 | tag à capturer en capture mode 3 |
| tag_5 | tag à capturer en capture mode 3 |


## Les 4 modes de fonctionnement 

### 1 : Enregistrement des passages des individus

Suivant un événement sur le capteur infrarouge , lecture RFID. Aucune Capture.

### 2 : Capture de tout individu

Suivant un événement sur le capteur infrarouge, fermeture de la porte

### 3 : Capture de certains individus

Suivant un événement sur le capteur infrarouge , lecture RFID. Si reconnaissance du TAG RFID, fermeture de la porte

### 4 : Capture des individus non taggués

Suivant un événement sur le capteur infrarouge , lecture RFID. Si non détection de TAG, fermeture de la porte.

## Manipulation du boitier

Le système s'enlève pour récupérer un oiseau comme on enlèverai la porte originelle, en soulevant le boitier et en tirant vers soi. La carte SD est accessible en dévissant le bouchon sur la surface inférieur. Un port USB étanche est également présent sur cette surface pour y placer le power bank ou la panneau solaire.