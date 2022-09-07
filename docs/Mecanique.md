# Mécanique

## Vue d'ensemble

![](./media/image2.jpeg){width="6.891771653543307in"
height="3.8652777777777776in"}

### Nomenclature

Extrait de la nomenclature mécanique :

  ------------------------------------------------------------------------------------
  1   Mamelons court  mamelons réduits à visser  Leroy Merlin [65814385]{.underline}
                      laiton M 12 x 17 pour tube              
                      en cuivre                               
  --- --------------- -------------------------- ------------ ------------------------
  2   écrou large     contre-écrous à visser     Leroy Merlin 65816345
                      laiton M 12 x 17 pour tube              
                      en cuivre                               

  3   Gaine Inox      Flexible Inox Ff15x21      Leroy Merlin [84420925]{.underline}
                      Longueur 800 Mm - Dn8                   

  4   Capuchon        Couvercle de protection    RS PRO       **134-6527**
      poussière       pour Bouton-poussoir série              
                      MSM 19\                                 
                      série AV Transparent                    

  5   Mamelon Long    Adaptateur Laiton Droit    RS PRO       3108781
                      Legris R Mâle 1/2pouce -                
                      Mâle 3/8pouce                           

  6   écrou laiton    Écrou de tube Norgren      RS PRO       226-763
                      série 22 G 3/8 Laiton                   

  7   malette         Malette de transport Peli  RS PRO       **2963098**
      Pelicase        1120 en\                                
                      Polypropylène, Dimensions               
                      externes 90 x\                          
                      206 x 167mm, étanche                    

  8   joint torique   joint torique support       RS PRO       **1964872**
                      gaine (dima ??)                         
  ------------------------------------------------------------------------------------

## Partie Antenne

La partie Antenne est en 2 pièces :

-   Une pièce qui forme les bords intérieurs. On y insert les capteurs
    IR et on y câble directement l'antenne. Pièce **« Socle.stl »**

-   Une pièce qui forme les bords extérieurs et vient se visser sur la
    première, avec un joint étanche pour assurer l'étanchéité entre
    les 2. Pièce **« Socle_couvercle.stl »**

![](./media/image3.png){width="5.276119860017498in"
height="3.3286537620297465in"}

![](./media/image4.png){width="2.183905293088364in"
height="2.9092869641294836in"}![](./media/image6.png){width="2.208954505686789in"
height="2.9421052055993in"}

![](./media/image7.jpeg)

###  

## Partie Malette

PHOTO Mamelons + bouton sur malette

## Assemblage Mecanique

#### Partie Antenne :

-   **Impression 3D** du « Socle.stl » et du ~~« Couvercle_creux.stl »~~
    **« Socle_couvercle.stl »**en ABS

-   **1^ère^ couche de résine époxy d'imprégnation** sur les parois qui
    recevront la coulée. Prendre une résine prise longue (par ex 24h)
    pour avoir le temps d'étaler la résine au pinceau sur les parois.
    (Exemple Araldite DBF et son durcisseur HY956)

Socle :

-   **Câblage Antenne** pour une impédance de 190uH (+ ou - 29 spires)

-   **Câblage IR** (récepteurs et led émetrices)

-   **Collage (étanche) des IR sur Socle**

    -   LED IR à emmancher de force + colle chaude pour être sûre

    -   Récepteur IR à maintenir en position par colle chaude

    -   Couche de colle polyuréthane (Araldite 2028-1 au pistolet ) pour
        former un bulbe sur la partie intérieur (et éviter la terre de
        s'accumuler au passage des hamsters).

-   **Soudure câbles IR sur plaquette** de jonction. Couper les fils IR
    au plus court pour éviter qu'ils dépassent de la coulée. Attention à
    dénuder le moins possible les fils du côté de la plaquette pour
    éviter des court-circuits entre les câbles.

Couvercle :

-   **Préparation câble Ethernet** : dénuder et étamer les deux
    extrémités des fils.

-   **Usiner deux méplats** sur l'écrou large en laiton

-   **Visser les fils sur bornier à vis**

-   **Vérifier fonctionnement de la partie antenne**

-   **Visser** mamelons laitons + joint torique avec l'écrou large sur
    le couvercle.

-   **Installation joint** en mousse dans le mamelon qui assure
    étanchéité entre câble et mamelon.

-   **Passer le câble** dans l'entrée du couvercle (donc dans le joint
    en mousse + mamelon + écrou)

Coulée

-   **Application du Silicone** (LOCTITE SI 595 Superflex transparent
    application à la seringue) sur toute la jonction socle/couvercle

    -   Visser le couvercle sur le socle à l'aide de vis
        auto-taraudeuses (6mm)

    -   Attendre le séchage complet avant nouvelle manipulation

-   **Doubler l'étanchéité** à l'aide de pâte à fixe au niveau du
    mamelon et partout où cela semble nécessaire

-   **Maintenir le câble** en hauteur et installer **la partie antenne
    bien à plat**

-   **Couler la résine époxy** prise rapide et opaque dans l'antenne.
    ( Rencast FC 52 Polyol + isocyanate chez Samaro OU chez Résine et
    moulage : KIT RESINE EPOXY DE COULEE DIELECTRIQUE NOIRE 1060/68 )

#### Partie Malette

-   **Peindre en blanc la malette** : 1 couche d'apprêt plastique sur
    toutes les faces avant de faire au moins 3 couches de peinture
    blanche.

-   **Perçages** et fixation des différents composants en sortie de la
    malette.

-   **Etanchéifier** avec un joint torique pour le mamelon en laiton,
    avec du silicone la fixation des boutons avec capuchons poussières.
    En effet les joints toriques prévus pour les boutons ne peuvent être
    utilisés avec en plus les capuchons de poussière.

-   **Passage du câble Ethernet** dans gaine inox + mamelon long

-   **Collage écrou de la gaine** inox sur les 2 mamelons, côté antenne
    et malette, pour éviter que la gaine se dévisse. (Araldite 2028-1 au
    pistolet) /!\\ Ne pas trop serré pour permettre à l'antenne de
    tourner sur elle-même

-   **Fixation des supports** de cartes dans malette

-   **Découpe mousse** de la malette, au format de la batterie, avec
    cutter.

## Test température au soleil

Test réalisé le 04 août 2022 sur « l'herbe » devant le bâtiment 24.

Thermomètre utilisé : thermomètre infrarouge sans-contact pouvant
mesurer de 0° à 100°C.

  --------------------------------------------------------------------------
                 Valise      Valise      Valise      Sol au      Sol à
                 carton      blanche     noire       soleil      l'ombre
  -------------- ----------- ----------- ----------- ----------- -----------
  Avant          30          30          30                      
  installation                                                   
  13h25                                                          

  13h45          40          48          58          31          40

  14h45          **52°**     **52°**     **66°**     60          **33**

  15h45          51          51          65          57          35

  16h45          48          50          66          60          35
  --------------------------------------------------------------------------

La Peli-case sous le carton st noire.

![](./media/image8.jpeg)![](./media/image9.jpeg)
