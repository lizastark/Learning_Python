#4-10 Slices
colors = ['red','magenta','teal','chartreuse','green','gray']
print("The first three items in this list are: ")
print(colors[0:3])

print("Three items from the middle of this list are: ")
print(colors[2:-2])

print("The last three items in this list are: ")
print(colors[-3:])


#4-11 My games, Your games
my_games = ['catan','dominion','love letter','chess']
friends_games = my_games[:]

friends_games.append('ticket to ride')
del friends_games[1]
my_games.append('sushi go')
my_games.remove('chess')

print("My fav games are ")
print(my_games)

print("My friends fav games are ")
print(friends_games)


#4-12 Looping
print("Here are the museums I want to go to ")
museums = ('guggenheim','the met','the whitney','MAD','MoMA')
for museum in museums[:2]:
	print(museum.title())