import roostergen

#########################################
dagen = 5
daguuren = 6

vakken = [
    [0, 0, '-           '],
    [1, 4, 'Informatica '],
    [2, 3, 'Wiskunde    '],
    [3, 3, 'Engels      '],
    [4, 5, 'Nederlands  '],
    [5, 2, 'Natuurkunde '],
    [6, 4, 'Scheikunde  '],
    [7, 3, 'Duits       ']
]

rooster = roostergen.gen_rooster(vakken,dagen,daguuren)
###########################################

score = 10_000

print(*rooster,sep='\n')
roostergen.print_rooster_vaknaam(rooster,vakken)

### tussenuren:
for i in range(len(rooster)): #1 tussenuur
    for j in range(len(rooster[i])-2):
        if rooster[i][j+1] == 0:
            if rooster[i][j] !=0 and rooster[i][j+2] != 0:
                score -= 50
                print("Tussenuur:   " + str(i) + " : " + str(j+1))

for i in range(len(rooster)): #2 tussenuren
    for j in range(len(rooster[i])-3):
        if rooster[i][j+1] == 0:
            if rooster[i][j] !=0 and rooster[i][j+2] == 0 and rooster[i][j+3] != 0 :
                score -= 200
                print("Tussenuur:   " + str(i) + " : " + str(j+1) + "-" + str(j+2))

for i in range(len(rooster)): #3 tussenuren
    for j in range(len(rooster[i])-4):
        if rooster[i][j+1] == 0:
            if rooster[i][j] !=0 and rooster[i][j+2] == 0 and rooster[i][j+3] == 0 and rooster[i][j+4] != 0:
                score -= 500
                print("Tussenuur:   " + str(i) + " : " + str(j+1) + "-" + str(j+3))


for i in range(len(rooster)):
    for j in range(len(vakken)):
        if rooster[i].count(j) == 2:
            vakplace = rooster[i].index(j) # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list moet hier nog naar kijken
            if rooster[i][vakplace] == rooster[i][vakplace + 1]:
                score += 25
                print("Blokuur:     " + str(i) + " : " + str(vakplace) + "-" + str(vakplace+1))
            else:
                score -= 1000
                print("2Uur:        " + str(i) + " : " + str(vakplace) + " and ?")
        elif rooster[i].count(j) >= 3:
            vakplace = rooster[i].index(j)
            score -= 1000
            print("3+uur:       " + str(i) + " : " + str(vakplace) + " and ?")



print("\nscore:       " + str(score))