#4-3 Counting to 20

# don't forget the semicolon and indentation!!!!!
for values in range(1,21):
	print(values)


#4-4 One million

#million = list(range(1,1000001))
#for numbers in million:
	#print(0) #can't not have anything here - error


#4-5 Summing a million
newMillion = list(range(1,1000001))
print(min(newMillion))
print(max(newMillion))
print(sum(newMillion))


#4-6 Odd numbers
#odd_numbers = list(range(1,1000001,2))
#for numbers in odd_numbers:
	#print(numbers)


#4-7 Threes
thirds = list(range(0,31,3))
for numbers in thirds:
	print(numbers)



#4-8 Cubes
cubes = []
for values in range(1,11):
	cubes.append(values**3)

print("\nappend style:")
print(cubes)


#4-9 Cube Comprehension
newCubes = [newValue**3 for newValue in range(1,11)]
print("\nlist comprehension style:")
print(newCubes)












