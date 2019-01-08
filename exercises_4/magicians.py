# for loops in python

magicians = ['candice', 'duque', 'jess', 'ali']
for magician in magicians:
	print(magician.title())


revelers = ['candice', 'duque', 'jess', 'ali']
costumes = ['wayne', 'garth', 'clown', 'edie gray']

#this doesn't work the way I want it to
for reveler in revelers:
	print(reveler.title() + ", you looked so great as ")
	for costume in costumes:
		print(costume)

print("\n")


############## Exercises

# 4.1

pizzas = ['green lantern', 'margherita', 'heart throb']
for pizza in pizzas:
	#print(pizza)
	print("I could eat " + pizza.title() + " pizza anytime at all.")
	print(pizza.title() + " pizza is the bestest.\n")

print("\nI just <3 the za.\n")


# 4.2
imaginary_animals = ['narwhal', 'dragon', 'unicorn']
for imaginary_animal in imaginary_animals:
	print("People say that " + imaginary_animal + "s aren't real, but I don't believe them.")
print("\nI think they're all based in reality at least.")
