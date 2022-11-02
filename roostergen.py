from random import randint


def leegrooster(
    dagen: int, daguuren: int
):  # genereert een leeg rooster met 0 in alle vakken
    return [[0 for i in range(daguuren)] for j in range(dagen)]


def roosteropties(
    rooster: list,
):  # genereert alle mogelijke opties voor plekken in een rooster.
    options = []
    for i in range(len(rooster)):
        for j in range(len(rooster[i])):
            tempoptions = [i, j]
            options.append(tempoptions)
    return options


def gen_rooster(
    vakken: list, dagen: int, daguuren: int
):  # genereert een rooster met het vak nummer als plaats in list vakuur
    rooster = leegrooster(dagen, daguuren)
    options = roosteropties(rooster)
    for i in range(len(vakken)):
        for j in range(vakken[i][1]):
            place = options.pop(randint(0, len(options) - 1))
            y = place[0]
            x = place[1]
            rooster[y][x] = i
    return rooster


def print_rooster_vaknaam(
    rooster: list, vakken: list
):  # print de rooster list met woorden ipv nummers
    naamrooster = []
    for i in range(len(rooster)):
        temprooster = []
        for j in range(len(rooster[i])):
            temprooster.append(vakken[rooster[i][j]][2])
        naamrooster.append(temprooster)
    print(*naamrooster, sep="\n")


# dagen = 5
# daguuren = 6

# vakken = [
#     [0, 0, '-           '],
#     [1, 4, 'Informatica '],
#     [2, 3, 'Wiskunde    '],
#     [3, 3, 'Engels      '],
#     [4, 5, 'Nederlands  '],
#     [5, 2, 'Natuurkunde '],
#     [6, 4, 'Scheikunde  '],
#     [7, 3, 'Duits       ']
# ]

# rooster = gen_rooster(vakken,dagen,daguuren)
# print(*rooster,sep='\n')
# print_rooster_vaknaam(rooster,vakken)
