# PWS_schoolrooster

Wat maakt een rooster goed?


database using SQLite


random genome ->
calc fitness ->
take highest fitness & store in best solution ->
combine parents ->
mutate child ->
repeat from calc fitness


---------------------------------------------------------------

rooster genereren doormiddel van vakken in open plekken invullen, als open plekken 0 is dan error (is beter dan kiezen dit lesuur wordt frans/duits/wiskunde/engels, want dan kan je bepalen hoeveel uur van een les)
?geen parents alleen mutatie
mutatie doomiddel van het wisselene van 0-5 *2 vakken
copieren beste 2 roosters vorige generatie naar huidige

---------------------------------------------------------------

vak-# | aantal les uren

vak-# | vak-naam | afkorting

situatie | hoeveel fitness verschill
...

---------------------------------------------------------------

situatie | hoeveel fitness verschill
2x zelfde vak op een dag -1000
tussenuur -100
1e -30
8e -50
9e -100
vrijdag 7/8/9 -30 extra
...

---------------------------------------------------------------

vak | aantal les uuren
3   wiskunde
2   nederlands
3   engels
4   natuurkunde
2   scheikunde
1   duits
3   biologie
4   informatica
...

---------------------------------------------------------------





Leerling heeft rooster heeft vakken heeft uuren


PvA:

eerst 1 rooster voor 1 persoon.
5x6

per vak positie als nummer, zo kan ik wel crossover doen
----------------------------------
foutenindex
1: 1x tussenuur
2: 2x tussenuur
3: 3x tussenuur
4: 2x op 1 dag

https://github.com/mcychan/GASchedule.py 

--------------------------------------

input:

Vak_id | Vak_naam | Uuren | (Room_eisen)
Docent_id | Docent_naam | vak_id | (beschikbaarheid)
Leerling_id | leerling_naam | vakken | 
(Room_id | Room_name | eisen)
dagen | dag_uuren

generations | populatie_grote | mutatie kans | cross-over kans
Fitness eisen | penalty



tussen:
generate een rooster:
genetic algoritm



output:

table :
[(Vak_naam, Docent, (Room)),(Vak_naam, Docent, (Room)),,,]
[]
[]
[]
[]

----------------------------------------------

website -> database -> python code -> database -> website