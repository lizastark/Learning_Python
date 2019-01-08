

for value in range(1,10):
	print(value)

print("\n")


lower = 0
higher = 4

for value in range(lower, higher):
	print(value)


numbers = list(range(lower, higher))
print(numbers)

#even numbers

even_numbers = list(range(2,11,2))
print(even_numbers)


#create the empty list
squares = [] 
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)


#get rid of the extra variable
squares = [] #create the empty list
for value in range(1,11):
	squares.append(value**2)

print(squares)


#simple stats
digits = list(range(1,10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))


#list comprehension
squaresComp = [value**2 for value in range(1,11)]
print(squaresComp)






