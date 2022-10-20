from random import randint



def leegrooster(dagen: int,daguuren: int): # genereert een leeg rooster met 0 in alle vakken
    return [[0 for i in range(daguuren)] for j in range(dagen)]

def roosteropties(rooster: list): # genereert alle mogelijke opties voor plekken in een rooster.
    options = []
    for i in range(len(rooster)):
        for j in range(len(rooster[i])):
            tempoptions = [i,j]
            options.append(tempoptions)
    return options

def gen_rooster(vakuur: list, dagen: int, daguuren: int): #genereert een rooster met het vak nummer als plaats in list vakuur
    rooster = leegrooster(dagen,daguuren)
    options = roosteropties(rooster)
    for i in range(len(vakuur)):
        for j in range(vakuur[i]):
            place = options.pop(randint(0,len(options)-1))
            y = place[0]
            x = place[1]
            rooster[y][x] = i
    return rooster

def print_rooster_vaknaam(rooster: list, vaknaam: list): # print de rooster list met woorden ipv nummers
    naamrooster = []
    for i in range(len(rooster)):
        temprooster = []
        for j in range(len(rooster[i])):
            temprooster.append(vaknaam[rooster[i][j]])
        naamrooster.append(temprooster)
    print(*naamrooster,sep='\n')



dagen = 5
daguuren = 6
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

rooster = gen_rooster(vakuur,dagen,daguuren)
print_rooster_vaknaam(rooster,vaknaam)