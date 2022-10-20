from random import randint

vakuur = [ # #uuren per #vak
    0,
    4,
    3,
    3,
    5,
    2,
    4,
    3
]

vaknaam = [ # naam per #vak
    "-          ",
    "Informatica",
    "Wiskunde   ",
    "Engels     ",
    "Nederlands ",
    "Natuurkunde",
    "Scheikunde ",
    "Duits      "
]

rooster = [ # leeg rooster 
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

options = []

for i in range(len(rooster)):
    for j in range(len(rooster[i])):
        tempoptions = [i,j]
        options.append(tempoptions)

print(options)

# for i in range(len(vakuur)):
#     for j in range(vakuur[i]):
#         y = randint(0,len(rooster)-1)
#         x = randint(0,len(rooster[0])-1)
#         k = rooster[y][x]
#         while k != 0:
#             y = randint(0,len(rooster)-1)
#             x = randint(0,len(rooster[0])-1)
#             k = rooster[y][x]
#         rooster[y][x] = i

for i in range(len(vakuur)):
    for j in range(vakuur[i]):
        place = options.pop(randint(0,len(options)-1))
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

print(*naamrooster,sep='\n')

#in het maken van rooster een lijst met opties gebruiken
# misschien numpy arrays gebruiken?