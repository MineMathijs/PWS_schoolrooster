# testing sandbox
import roostergen

rooster = roostergen.leegrooster(5,6)
opties = roostergen.roosteropties(rooster)
print(*rooster,sep='\n')
print(opties)