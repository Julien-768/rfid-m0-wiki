# Carte de développement

## Choix de la carte

Voici quelques cartes de développement de la gamme Feather Adafruit envisagées pour mener le projet :

| Nom carte | Microcontrôleur | Stockage Flash | Cadence | Slot microSD | RTC intégré | Fournisseur | Prix |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Adafruit Feather M4 | ATSAMD51J19 | 512KB | 120MHz | non | non | Mouser | 22.95€ |
| Adafruit Feather 32u4 | ATmega32u4 | 32KB | 8MHz | non | non | Farnell | 19.44€ |
| Adafruit Feather 32u4 Adalogger | ATmega32u4 | 32KB | 8MHz | oui | non | RS | 19.19€ |
| Adafruit Feather M0 Adalogger | ATSAMD21G18 | 256KB | 48MHz | oui | non | RS | 17.43€ |
| Adafruit Feather M0 | ATSAMD21G18 | 256KB | 48MHz | non | non | RS | 17.43€ |
| Shield RTC et microSD FeatherWing | pas de microcontrôleur | - | - | oui | oui | RS | 7.82€ |

Le projet sera mené avec une carte Adafruit Feather M0 Adalogger, qui offre un port microSD directement sur la carte. La première version du code utilise 34KB. L'espace de stockage de la carte semble suffisant pour le reste du projet. Nous utiliserons l'IDE Arduino pour coder notre projet. Voir ce lien pour plus d'informations sur la carte : https://learn.adafruit.com/adafruit-feather-m0-adalogger/overview .

## Notes d'utilisations

### Reconnaissance et conversion d'une carte sous Python

Les cartes Feather M0 ont la possibilité d'être développées sous Python, en y installant une version de CircuitPython. Si c'est le cas, la carte branchée apparaîtra comme une disque externe dans l'explorateur de fichier de l'ordinateur, et n’apparaîtra pas comme étant connecté à un port COM dans l'IDE Arduino. Pour désinstaller CircuitPython et continuer le développement sur l'IDE Arduino, il faudra connecter la carte à l'ordinateur et double cliquer sur le bouton reset de la carte jusqu'à ce que la carte apparaisse dans l'IDE. On peut alors y téléverser un programme et l'utiliser sous Arduino. Voir ce lien pour plus de détails : https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/uninstalling-circuitpython .

# Panneau solaire

Un des objectifs du projet est qu'il soit alimenté grâce à un panneau solaire. Un panneau solaire se choisit en général selon la puissance qu'il est capable de délivrer. Cette puissance doit être supérieure à la puissance nécessaire du système alimenté. Il faut aussi considérer les pertes du chargeur de batterie.

## Estimations théoriques

Pour nous approcher de cette puissance, nous pouvons faire des estimations théoriques. Elle est déterminée en estimant la durée d'ensoleillement du système dans les pires conditions et la consommation moyenne du système. 

Voici un tableau des consommations de chacun des composants de notre système

| Composant | Consommation passive | Régime particulier | Courant moyen |  Puissance moyenne |
| ------ | ------ | ------ | ------ | ------ |
| Feather M0 Adalogger | 11mA | 50mA pendant 1 seconde lors de l'écriture sur carte SD | 11.65mA | 0.039W |
| Capteur infrarouge | 20mA | on utilise deux capteur IR, 21.8mA mesuré, 10mA en enlevant les LEDs | 20mA | 0.066W |
| Module RTC | 0.3mA | mesurée : 0.09mA | 0.3mA | 0.001W |
| Servo moteur | 10mA | 500mA max selon la notice, à ~1 tr/s, fonctionne en 5v| 1.6mA | 0.008W |
| Module RFID | 17mA | 230mA pendant lecture, activation pendant 1 seconde, fonctionne en 5v | 3.9mA | 0.019W |
| Adafruit MAX31865 | 3.5mA | - | 3.5mA | 0.012W |


Pour calculer la puissance moyenne, on considère les régimes particuliers de fonctionnement de chaque composant. On fait les hypothèses suivantes :
- On utilise les capteurs infrarouge sans la LED d’allumage 
- Lorsque le système est en mode capture, le servomoteur fonctionne 6 fois par heure, avec 2 secondes de fonctionnement à chaque fois (2 tours). Son alimentation est coupé lorsqu'il ne fonctionne pas.
- Le module RFID est activé 60 fois pendant 1 secondes toutes les heures. Son alimentation est coupé lorsqu'il ne fonctionne pas.
- L'écriture de données sur la carte SD est activé 60 fois pendant 1 seconde toutes les heures
Les puissances sont toutes calculées pour une tension de 3.3V, sauf pour le servomoteur qui fonctionne à 5V.
- On différentie la consommation normale et la consommation lorsque le mode économie d'énergie est activé.

On estime alors une puissance moyenne de 0.145W en consommation normale, et de 0.11W pour une économie d'énergie de 8 heures.

## Choix panneau solaire

Nous avons maintenant une estimation de la puissance nécessaire pour faire fonctionner notre système. Les panneaux solaires fournissent de l'énergie de manière instable et dépendent de leur ensoleillement. On utilise alors un calculateur solaire pour déterminer la puissance du panneau. On sait que notre batterie LiPo est à 1.5Ah. On obtient alors les autonomies suivantes :

|  | Mode éco désactivé | Mode éco activé (22h-6h) | 
| ------ | ------ | ------ |
| Utilisation solaire (batterie complètement chargée et pas d'exposition au soleil) | 36 heures | 2 jours |
| Utilisation d'une power bank (10 Ah) | 10 jours | 11 jours |

La puissance de panneau varie dans chaque situation. Un panneau 1.5W est suffisant pour les différents cas d'utilisation. On choisit un panneau 5v pour ne pas endommager le boost 5v en sortie de la carte de chargement.