# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:10:07 2024

@author: Administrator
"""




Ei_auf_Brot = """Ei auf Brot, pro Portion:
Rührei-> 2 Eier, 40ml Milch, Pfeffer und Salz
Brot->   Graubrot/Kartoffelbrot/leckeres Brot dessen Namen ich vergessen habe

Kochen=> Ei zusammen mit Milch, Pfeffer, Salz und habe ich vegessen schlagen.
         Dann in die Pfanne. Sobald es fertig ist, aufs Brot!"""

Scharfe_Haenchenbrust = """Scharfe Hänchenbrust, pro Portion:
Fleisch->      125g Hähnchenbrustfilet, 1/4 Chillischote, 1/2 Zwiebel 
Reis u. Soße-> 400g Tomtaen aus der Dose, 150ml Hühnerbrühe, 3cm Ingwer, 1/2 TL Kurkuma
               1/2 TL Chillipulver, 1/2 TL Korianderpulver, 3EL Öl und Salz

Kochen=>       Hähnchenbrustfilet waschen, trocken tupfen und in Streifen schneiden. Zwiebel
               würfeln. Knoblauch schälen und durch die Presse drücken. Chilischote waschen,
               die weißen Innenhäute mit den Kernen entfernen (am besten mit Handschuhen).
               Ingwer schälen und in kleine Würfel schneiden.

               Ingwer und Knoblauch mit dem Fleisch mischen und mindestens 1 Stunde im
               Kühlschrank marinieren.

               Öl in einer Pfanne erhitzen. Zwiebelwürfel und Chili kurz anbraten. Das Fleisch
               dazugeben und anbraten. Mit Chilipulver, Kurkuma und Koriander würzen und kurz
               mit braten. Tomatenstücke und Brühe dazugeben. Etwa 5 Minuten köcheln lassen.
               Mit Salz abschmecken

               Dazu passt Reis."""


Protein = [Ei_auf_Brot, Scharfe_Haenchenbrust]
Scharf = [Scharfe_Haenchenbrust]

Rezepte__={'Protein':[Ei_auf_Brot, Scharfe_Haenchenbrust],
           'Scharf':[Scharfe_Haenchenbrust]}
L = input('Was möchten sie denn essen: ')
k1 = L.split(', ')
L = [str(pf) for pf in k1]

r1 = Rezepte__['Protein']
r2 = Rezepte__['Scharf']

liste1 = ["Apfel", "Banane", "Kirsche"]
liste2 = ["Banane", "Kirsche", "Dattel"]

set1 = set(Protein)
set2 = set(Scharf)

gemeinsame_elemente = set1.intersection(set2)
for e in gemeinsame_elemente:
    print(e)

