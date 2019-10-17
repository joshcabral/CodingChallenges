variables = {}
import sys

#inputs = []
#inline = input()
for line in sys.stdin:
	
	line=line.replace('\n','')
	line = line.split(' ')
	if line[0] == 'define':
		variables[line[2]] = int(line[1])
	elif line[0] == 'eval':
		if line[1] in variables and line[3] in variables:
			var1 = int(variables[line[1]])
			var2 = int(variables[line[3]])
			if ">"==line[2]:
				print("true") if var1>var2 else print("false") 
			elif "<"==line[2]:
				print("true") if var1<var2 else print("false") 
			else: print("true") if var1==var2 else print("false")
		else:
			print("undefined")
				
	else:
		print("You messed up.")