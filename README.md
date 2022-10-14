# PWS_schoolrooster

Genetic algorithm die ook met den database interact


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
2x zelfde vak op een dag -1000\n\n\n\n
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