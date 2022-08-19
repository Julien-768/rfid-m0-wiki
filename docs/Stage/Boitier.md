# Intégration avec le nichoir

Le nichoir prévu pour accueillir le système se rapproche d'un cylindrique en béton de 33.5cm de haut et 15cm de diamètre. Il est composé de deux parties, le bâti par lequel on attache le nichoir (en marron sur la photo ci-dessous) et une porte dans laquelle est percée un trou pour permettre aux oiseaux de rentrer et sortir (en beige). Pour bloquer la sortie d'un oiseau capturé, on peut créer une nouvelle pièce à placer à coté du trou de la porte pour y bloquer la circulation, ou on peut créer une pièce qui remplace la porte entièrement.

![image](uploads/7782cd9fceb337eb6b9dd27fa04d8f03/image.png)


# Prototype V1

Dans le premier prototype réalisé, le choix a été fait de fabriquer une pièce supplémentaire à fixer sur la porte du nichoir. Le contour de la porte a été projeté pour faire le contour de la pièce, à l'exception de la partie supérieur qui a été réduite pour assurer l'ouverture de la porte. La pièce fait 5cm d'épaisseur, 10cm de large et 17cm de haut. Un conduit est prévu pour s'aligner avec le trou de la porte, et le servo moteur fait pivoter une trappe par dessus ce trou pour bloquer la circulation. Les capteurs infra rouges sont situés de part et d'autre de la surface intérieure du conduit. L'antenne RFiD est située en dessous du conduit. Voici un schéma explicatif de l'intégration du système avec le nichoir :

<img src="uploads/2e3a0d380b855450ca1d8f8fd9b680e4/schéma.png" width="500">

La pièce principale a été fabriqué en impression 3D, avec du plastique PLA. Cela permettait de réaliser facilement les petits détails sur la pièce en réduisant le coût de sa production, la résistance mécanique de la pièce n'étant pas un problème car elle aura peu d'efforts à supporter. Il faut ajouter à cette pièce un couvercle qui pourra être utilisé avec un joint d'étanchéité, ainsi que toutes les pièces relatives à la trappe de fermeture et son actionnement.

<img src="uploads/792870e2dfc381ee6365c96b4331609b/boitier_3.png" width="350">

<img src="uploads/0ebb9a5fbd680e3fd41a605928192deb/boitier_2.png" width="350">

On peut remarquer des pignons sur la base du boitier pour fixer des composants. Deux encoches accueillent l'antenne RFiD au centre et le servo moteur à gauche. Afin de rendre ce prototype complètement fonctionnel, il faut percer des trous sur la surface horizontale inférieure pour y faire passer le câble de la powerbank ou du panneau solaire, ainsi qu'un accès à la carte microSD.

La trappe est réalisé dans du plastique transparent. L'axe de la trappe est en acier. En position ouverte, la trappe est maintenue ouverte par un levier en plastique pivotant par rapport au bâti (ici en blanc). Ce levier est lui même retenu par une ficelle attaché au servomoteur. En position fermée, le servomoteur tourne de 180° pour détendre la ficelle et relâcher le levier. Un ressort de torsion monté sur l'axe de la trappe permet alors de la fermer.

<img src="uploads/ea9a8e330919c1419244bbd7db7567a8/boitier_4.png" width="350">

<img src="uploads/b6539159ec16679bbb882db7071694e7/Levier.png" width="350">

# Avantages et inconvénients

Ce prototype a l'avantage d'avoir une architecture simple et d'être robuste, la majorité des surfaces étant de 5mm de large. La pièce principale ne présente pas de porte à faux, ce qui élimine la nécessité d'imprimer avec des supports. Le conduit de passage est quasiment identique à ce que l'on peut trouver sur les nichoirs du commerce, et la surface extérieure rugueuse permet aux oiseaux de bien pouvoir s'y appuyer.

Néanmoins le boitier n'est pas très compact, et dénature l'aspect esthétique du nichoir auquel les oiseaux sont habitués. L'intégration des LEDs et photo-transistor des capteurs infrarouges est compliquée, du fait de leur placement. Il n'y a pas beaucoup de place pour la carte électronique, au vu de la surface qu'occupe chacun des composants. Le servomoteur est désaxé par rapport à l'axe de la trappe, ce qui nécessite un système de transmission de mouvement miniature qui risque de ne pas être très fiable. L'antenne RFiD vient se placer sous le conduit, ce qui pourrait être un problème au vu de sa faible distance de détection.

La conception et la fabrication de ce prototype V1 n'a pas été aboutie, et a mené à la conception et la fabrication du prototype V2.

# Prototype V2

## Forme globale

Une volonté de concevoir une deuxième version du boitier était d'en diminuer sa taille, mais aussi d'y faciliter l'intégration des composants. le choix a donc été fait de créer une pièce qui viendrait remplacer totalement la porte pour gagner de l'espace. Le boitier a une forme incurvée qui épouse la surface extérieure du nichoir, et présente une protrusion sur sa partie supérieure pour assurer l'assemblage avec le bâti du nichoir. Des modèles du boitier ont été réalisés pour qu'il soit imprimable en deux fois, par des imprimante 3D à petit volume d'impression. 

<img src="uploads/42e97ae2cdd9faf9a487247d90a92fe7/Capture.PNG" width="350">

<img src="uploads/b07d259aa16cca8e191e390cb9042f84/Capture2.PNG" width="350">

## Conduit de passage

La majorité des capteurs et des actionneurs se situent autour du conduit de passage. Les nichoirs à mésanges présentent habituellement un conduit circulaire, le diamètre dépendant de l'espèce recherchée. Ici un conduit circulaire imposait une motorisation de la trappe peu avantageuse. On pourrait conserver le mouvement de porte du prototype V1 mais il aurait fallu réaliser un système de transmission de mouvement complexe et peu fiable. On pourrait également utiliser une fermeture de type guillotine, mais il faudrait alors placer le servomoteur selon un autre axe, ce qui élargirait significativement le boitier. Le choix a donc été fait d'utiliser un trou circulaire sur la partie inférieure et carré sur la partie supérieure. Ainsi la forme du trou n'est pas trop dénaturée, et la trappe a de la place pour pivoter. Le trou a une hauteur et une largeur de 32mm pour s'apparenter à un trou de diamètre équivalent.

L'axe du servomoteur est aligné avec l'axe de la trappe pour faciliter son intégration et pour assurer une durée de vie plus longue au système. Les LEDs et photo-transistors des capteurs infrarouges sont montés dans la surface du conduit, et les fils de l'antenne RFiD s'y enroulent. Une pièce séparée accueille les LEDs, photo-transistors, et antenne pour faciliter l'assemblage de ces composants. Elle a une forme cylindrique et se place en continuité du conduit présent sur le boitier principal.

<img src="uploads/6a338645c4eeaa493b08e5aff6d9bca2/Capture4.PNG" width="500">

<img src="uploads/deb88ce2d00aac9d61aa6151d717be30/Capture5.PNG" width="350">

## Interface inférieur

La surface inférieure du boitier se démarque comme interface avec l'extérieur, de par son accessibilité. On y retrouve un port USB-C étanche pour y brancher le power bank ou le panneau solaire, un anneau qui permettra de fixer ces dispositifs à l'aide d'un mousqueton, et un trou avec un bouchon à cran d'arrêt pour accéder à la carte microSD.

<img src="uploads/a1a7ce65e480f92394b8d4da72d93ba5/Capture3.PNG" width="500">

<img src="uploads/0945b5fe53a7546b51560e865c5b6f5b/Capture7.PNG" width="350">

## Capot

Le capot vient refermer le boitier. De la colle adaptée est utilisée pour assurer l’étanchéité. 4 vis permettent de maintenir le capot en position. Une surface est prévue pour fixer une plaque de métal de quelques centimètres de long pour fixer le système au bâti du nichoir.

<img src="uploads/44c246af996de4bd8d608b4714d6ed8d/Capture6.PNG" width="350">

## Remarques critiques

Après impression du boitier, il a été remarqué que la plupart des jeux fonctionnels et espacements entres pièces n'étaient pas bons et certaines pièces ont du être rabotées pour pouvoir être assemblées. Le capot n'a pas été imprimé mais risque d'être un peu trop épais au vu de l'espace entre le boitier principal et le nichoir quand on les assemble.