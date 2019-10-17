import sys
import math
count = 0
inputs = []


def logs(plist):
	newList = []
	i = 0
	#print(len(plist))
	while i<len(plist):
		newList+=[math.log10(int(plist[i]))]
		i+=1
	return newList

def powers(l):
	value= (l[-1])+.00001
	for i in range(len(l)-1):
		value = value**(l[-(i-1)])
	return value

def evaluate(str):
	nums = str.split("^")
	nums[-1] = nums[-1].strip('\n')
	#print(nums)
	return powers(logs(nums))

for line in sys.stdin:
	if line == "\n":
		break
	if count == 0:
		count = 1
	else:
		inputs.append([evaluate(line), line])

print('Case 1:')
inputs.sort(reverse=True)
#inputs = inputs[::-1]
for i in inputs:
	print(i[1].strip('\n'))
	#print(i)

		
