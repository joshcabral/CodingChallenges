import sys
		
numTests = int(input())
for i in range(numTests):
	if i != 0:
		print()
	foreignD = {}
	englishD = {}
	
	for j in range(int(input())):
		input()
		foreign = input().split(' ')[1:]
		english = input().split(' ')[1:]
		for food in foreign:
			if food in foreignD:
				foreignD[food] = foreignD[food].intersection(set(english))
			else:
				foreignD[food] = set(english)
		for food in english:
			if food in englishD:
				englishD[food] = englishD[food].intersection(set(foreign))
			else:
				englishD[food] = set(foreign)
				
	for food, options in foreignD.items():
		for option in options:
			newSet = set()
			if food in englishD[option]:
				newSet.add(food)
			foreignD[food] = newSet
				
	for food, options in englishD.items():
		for option in options:
			newSet = set()
			if food in foreignD[option]:
				newSet.add(food)
			englishD[food] = newSet
					
	for food in list(foreignD.keys()).sort():
		for option in foreignD[food].sort():
			print('('+food+', '+option+')')
	
	