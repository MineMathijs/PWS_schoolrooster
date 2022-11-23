from random import randint

vakuur = [0, 4, 3, 3, 5, 2, 4, 3]  # #uuren per #vak

vaknaam = [  # naam per #vak
    "-          ",
    "Informatica",
    "Wiskunde   ",
    "Engels     ",
    "Nederlands ",
    "Natuurkunde",
    "Scheikunde ",
    "Duits      ",
]

daguuren = 6
dagen = 5

rooster = [[0 for i in range(daguuren)] for j in range(dagen)]  # leeg rooster

print(rooster)

options = []

for i, r in enumerate(rooster):
    for j, s in enumerate(r):
        tempoptions = [i, j]
        options.append(tempoptions)

print(options)

for i in range(len(vakuur)):
    for j in range(vakuur[i]):
        place = options.pop(randint(0, len(options) - 1))
        y = place[0]
        x = place[1]
        rooster[y][x] = i

print(rooster)

naamrooster = []

for i in range(len(rooster)):
    temprooster = []
    for j in range(len(rooster[i])):
        temprooster.append(vaknaam[rooster[i][j]])
    naamrooster.append(temprooster)

print(*naamrooster, sep="\n")
