# Calculateur d'emprunts 

Ce script permet de calculer les durées et couts d'emprunt en fonction du prix du bien à acheter, de vos revenus et de vos charges pour un taux d'intérêt que vous pouvez choisir. 
***Le taux d'interet annuel moyen en France en Janvier 2025 est de l'ordre de 3.5% (soit 0.035)***

## Fonctionnement 
Lors de l'exécution du script, une fenêtre s'ouvre. Celle-ce contient plusieurs champs permettant d'entrer des informations relatives à votre situation financière.
Le script utilise ensuite ces données pour calculer la durée ainsi de l'emprunt ansi que le prix total du bien en fonction de votre apport actuel et du temps que vous attendez avant d'acheter. Ce temps d'attente peut, dans certaines situations, permettre d'augmenter votre apport et ainsi réduire le montant à emprunter. Toutefois, pendant cette attente, si vous êtes locataires, les loyer peuvent contrebalancer l'effet positif de l'augmentation de l'apport. 
Ce script permet d'identifier le meilleur moment pour acheter un bien en fonction de son prix et de votre situation actuelle.

### Liste des entrées
***Prix min et max du bien***: Permettent de choisir une fourchette de prix du bien que vous souhaitez acheter. Ces valeurs en euros serviront de bornes aux axes verticaux des graphiques.

***Revenus mensuels***: Vos revenus mensuels en euros permettent de calculer le montant max de vos mensualités conformément aux *recommandations de taux d'endêtement de 33% en France*.

***Epargne mensuelle***: Correspond au montant en Euros que vous parvenez à épargner chaque mois en ce moment. Cela servira à calculer l'augmentation de votre apport en fonction du nombre d'années d'attente avant d'emprunter.

***Mensualité (max par défaut)***: Correspond au montant des mensualités en euros à rembourser une fois le prêt contracté. Par défaut cette valeur est fixée à sa valeur max calculée pour un tax d'endêtement de 33%. Cette valeur est modifiable à la hausse ou à la baisse. 

***Loyer moyen***: Correspond à votre loyer en euros. Cela correspond à la valeur moyenne estimée de votre loyer sur la période d'attente avant la contraction de l'emprunt.

***Taux d'intérêt annuel***: Correspond au taux d'intéret annuel qui est à définir avec la banque au moment de la signature du contrat. Cette valeur varie en fonction de la durée du prêt (plus l'emprunt est long, plus le taux est élevé) et dans le temps, pour un montant et une durée donnée, en fonction de l'état du marché. *Indication*: le taux moyen en janvier 2025 est autour de 3.5%. (Valeur à rentrer = 0.035).

***Apport actuel***: Montant en euro de votre apport à l'heure actuelle. Cela permet de calculer le montant à emprunter pour acheter un bien dans la gamme de prix renseignée. 

### Détails des calculs
***Apport au moment de l'achat***: Votre apport actuel + votre loyer x le nombre de mois d'attente avant l'achat d'un bien.

***Durée du prêt***: Calculée a partir de la formule classique pour un prêt à taux annualisé, fixe et sans intérêts composés duree = (Log(mensualite / (mensualite - pret * taux_interets / 12)) / Log(1 + taux_interets / 12))/12

***Prix total du bien***: Apport au moment de l'achat + duree d'emprunt(annes) * 12 * mensualité +loyer * 12 * temps d'attente avant l'achat

### Remarque importante
Lorsque les mensualités sont basses par rapport au montant total emprunter, vous pouvez recevoir un message d'erreur disant que certaines prix dépassent votre capacité d'emprunt.

1) Dans ce script cela peut s'expliquer de la façon suivante: Le montant max des mensualités est fixé à environ 33% de vos revenus (si vous n'avez aucun autre prêt connu de votre banque en cours). Lorsque vous empruntez une grosse somme, la durée de remboursement augmente. Ce faisant le montant total à rembourser augmente également car les intérêts s'appliquent à une durée plus longue. De plus, plus la durée de remboursement augmente, plus le taux de remboursement est élevé. Au dela d'un certain montant emprunté, le montant mensualisé des intérêts peut dépasser la valeur maximale autorisée de vos mensualités. Ainsi il devient impossible de rembourser l'emprunt.

2) Dans le cas général des banques, lors d'un emprunt très long les premières mensualités sont majoritairement composées des intérêts et le remboursement du capital est moins rapide. Ainsi, au dessus d'un certain seuil d'emprunt, la durée de remboursement pourrait augmenter très rapidement. Les banques refusent donc ces prêts
   
La limite de capacité d'emprunt calculée par le script n'est donc pas identique à celle des banques mais donne une limite légèrement surestimée.

## Comment lire les graphs ?
Le script permet de générer deux graphs

### Description des graphs
#### Graph de gauche
Donne le montant total déboursé pour l'achat du bien en fonction du temps attendu avant d'acheter (temps pendant lequel vous restez locataire) et du prix du bien (frais de notaire inclus). 
Pour lire ce graph il faut choisir un prix, un temps d'attente et relever la couleur du graph à l'intersection des deux valeurs. Cette couleur doit ensuite etre reportée sur l'échelle colorée a froite du graph pour connaitre le coût total du bien. 

#### Graph de droite
Donne la durée de remboursement de l'emprunt en fonction du temps attendu avant d'acheter (temps pendant lequel vous restez locataire) et du prix du bien (frais de notaire inclus). 
Pour lire ce graph il faut choisir un prix, un temps d'attente et relever la couleur du graph à l'intersection des deux valeurs. Cette couleur doit ensuite etre reportée sur l'échelle colorée a froite du graph pour connaitre la durée de l'emprunt. Il peut arriver qu'attendre cinq ans en avant d'acheter réduise la durée de l'emprunt de 7 ou 8 ans. Ainsi en attendant il est parfois possible de finir de rembourser le bien plus tôt. 

### Astuce 

1) Pour savoir à quel moment il est le plus avantageux d'acheter, il suffit de choisir un prix et de tracer une ligne horizontale sur le grpahique. Identifiez ensuite sur cette ligne la position à laquelle la couleur du graph est la plus sombre: Cela vous donne le temps optimal pendant lequel vous devriez continuer d'épargner avant d'acheter.

2) Gardez bien en tête ces deux valeurs : **Le prix du bien** et **le temps d'attente en années** et reportez-vous au graph de droite. Reportez les deux valeurs sur le graph puis relevez la couleur correspondante et reportez-la sur l'échelle de droite pour connaitre la durée de l'emprunt correspondant aux consitions optimales identifées dans l'étape 1)


## Limitations et impacts sur les prévisions
Le montant de l'assurance sur l'emprunt n'est pas pris en compte dans les calculs.
Le marché est fluctuant pour un bien dooné, le prix peut descendre ou monter pendant le temps d'attente. 
