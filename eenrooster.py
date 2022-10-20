from random import randint

import time
start_time = time.time()

vakuur = [ #uuren
    0,
    4,
    3,
    3,
    5,
    2,
    4
]

vaknaam = [
    "-          ",
    "Informatica",
    "Wiskunde   ",
    "Engels     ",
    "Nederlands ",
    "Natuurkunde",
    "Scheikunde "
]

rooster = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

for i in range(len(vakuur)):
    for j in range(vakuur[i]):
        y = randint(0,len(rooster)-1)
        x = randint(0,len(rooster[0])-1)
        k = rooster[y][x]
        while k != 0:
            y = randint(0,len(rooster)-1)
            x = randint(0,len(rooster[0])-1)
            k = rooster[y][x]
        rooster[y][x] = i

print(rooster)

naamrooster = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

for i in range(len(rooster)):
    for j in range(len(rooster[0])):
        naamrooster[i][j] = vaknaam[rooster[i][j]]
print(*naamrooster,sep='\n')

print("My program took", time.time() - start_time, "to run")
