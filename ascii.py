rotations = {' ':' ', '|':'-', '-':'|', '+':'+'}
count =0
while True:
	inline = input()
	if inline == "0":
		break
	else:
		if count != 0:
			print()
		count += 1
		numLines = int(inline)
		lines = []
		for i in range(numLines):
			lines.append(input())
		lengths = [len(line) for line in lines]
		maxLength = max(lengths)
		outputs = []
		for i in lines:
			i+=" "*(maxLength-len(i))
		for y in range(maxLength):
			outputLine = ""
			for x in lines[::-1]:
				outputLine+=rotations[x[y]]
			print(outputLine.rstrip())