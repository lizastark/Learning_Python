
#slicing a list
players = ['delgado', 'abrams', 'beto', 'gillam']
print("slice 1 = ")
print(players[0:3]) #don't forget to use [], not ()

print("slice 2 = ")
print(players[2:4])

print("slice without a beginning = ") #starts at beginning of list
print(players[:4])

print("slice without an end = ")
print(players[2:])

print("slicing from a distance = ")
print(players[-2:]) #last two
print(players[:-2]) #first two


#looping through a slice
print("All of these people should have won the midterms: ")
for player in players[:4]:
	print(player.title())


pokemon = ['pikachu','oddish','pidgey','rattata','clefairy','psyduck']
print("team 1 = ")
print(pokemon[0:3])

print("team 2 = ")
print(pokemon[-4:])

print("team 3 = ")
print(pokemon[:-2])

n