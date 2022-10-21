# testing sandbox
import roostergen
import roosterfitness
import roosterpopulation

population_size = 1000
dagen = 5
daguuren = 6
top_ammount = 10
multiplier = 100
vakken = [
    [0, 0, "-           "],
    [1, 4, "Informatica "],
    [2, 3, "Wiskunde    "],
    [3, 3, "Engels      "],
    [4, 5, "Nederlands  "],
    [5, 2, "Natuurkunde "],
    [6, 4, "Scheikunde  "],
    [7, 3, "Duits       "],
]
mutatie_rate = 2
generations = 30

for i in range(generations):
    if i == 0:
        gen = roosterpopulation.gen_first_population(
            population_size, vakken, dagen, daguuren
        )
    else:
        gen = roosterpopulation.next_generation(
            gen, top_ammount, multiplier, vakken, dagen, daguuren, mutatie_rate
        )
    print("\nGeneration " + str(i) + ":")
    print(*roosterpopulation.get_top_populations(gen, 10), sep="\n")
