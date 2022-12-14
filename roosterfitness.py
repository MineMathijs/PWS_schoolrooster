import roostergen

#########################################
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

# rooster = roostergen.gen_rooster(vakken,dagen,daguuren)
###########################################


# print(*rooster,sep='\n')
# print()
# roostergen.print_rooster_vaknaam(rooster,vakken)
# print()

### tussenuren:
def calc_fitness(rooster: list, vakken: list):
    fouten = []
    score = 10_000
    for i in range(len(rooster)):  # 1 tussenuur
        for j in range(len(rooster[i]) - 2):
            if rooster[i][j + 1] == 0:
                if rooster[i][j] != 0 and rooster[i][j + 2] != 0:
                    score -= 50
                    # print("Tussenuur:   " + str(i) + " : " + str(j+1))
                    fouten.append([i, j + 1, 1])

    for i in range(len(rooster)):  # 2 tussenuren
        for j in range(len(rooster[i]) - 3):
            if rooster[i][j + 1] == 0:
                if (
                    rooster[i][j] != 0
                    and rooster[i][j + 2] == 0
                    and rooster[i][j + 3] != 0
                ):
                    score -= 200
                    # print("Tussenuur:   " + str(i) + " : " + str(j+1) + "-" + str(j+2))
                    fouten.append([i, j + 1, 2])
                    fouten.append([i, j + 2, 2])

    for i in range(len(rooster)):  # 3 tussenuren
        for j in range(len(rooster[i]) - 4):
            if rooster[i][j + 1] == 0:
                if (
                    rooster[i][j] != 0
                    and rooster[i][j + 2] == 0
                    and rooster[i][j + 3] == 0
                    and rooster[i][j + 4] != 0
                ):
                    score -= 500
                    # print("Tussenuur:   " + str(i) + " : " + str(j+1) + "-" + str(j+3))
                    fouten.append([i, j + 1, 3])
                    fouten.append([i, j + 2, 3])
                    fouten.append([i, j + 3, 3])

    # for i in range(len(rooster)): # NIET VERWIJDEREN, DEZE RUNNED IETS SNELLER MAAR KRIJG NIET ALLE PLEKKEN VAN DE SLECHTE VAKKEN
    #     for j in range(len(vakken)):
    #         if rooster[i].count(j) == 2:
    #             vakplace = rooster[i].index(j) # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list moet hier nog naar kijken
    #             if rooster[i][vakplace] == rooster[i][vakplace + 1]:
    #                 score += 25
    #                 print("Blokuur:     " + str(i) + " : " + str(vakplace) + "-" + str(vakplace+1))
    #             else:
    #                 score -= 1000
    #                 print("2Uur:        " + str(i) + " : " + str(vakplace) + " and ?")
    #         elif rooster[i].count(j) >= 3:
    #             vakplace = rooster[i].index(j)
    #             score -= 1000
    #             print("3+uur:       " + str(i) + " : " + str(vakplace) + " and ?")

    # zelfde vak meerdere keren op dezelde dag
    for i in range(
        len(rooster)
    ):  # runned iets slomer maar is beter als ik een beter algoritme ga maken
        for j in range(len(vakken)):
            if rooster[i].count(j) >= 2:
                vakplace = [k for k, e in enumerate(rooster[i]) if e == j]
                if len(vakplace) == 2:
                    if vakplace[0] == (vakplace[1] - 1):
                        score += 25
                        # print("blokuur vak " + str(j) + " op " + str(i) + " : " + str(vakplace))
                    else:
                        score -= 1000
                        # print("2x vak " + str(j) + " op " + str(i) + " : " + str(vakplace))
                        fouten.append([i, vakplace[0], 4])
                        fouten.append([i, vakplace[1], 4])
                else:
                    score -= 1000
                    # print("3+x vak " + str(j) + " op " + str(i) + " : " + str(vakplace))
                    for l in range(len(vakplace)):
                        fouten.append([i, vakplace[l], 4])
    return score, fouten


# score = fitness(rooster,vakken)
# print("\nscore:       " + str(score))
