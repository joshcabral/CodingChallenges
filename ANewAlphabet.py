dictionary = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#', 'g':'6', 'h':'[-]', 'i':'|', 'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\/[]', 'n':'[]\[]', 'o':'0', 'p':'|D', 'q':'(,)', 'r':'|Z', 's':'$', 't':"']['", 'u':'|_|', 'v':'\/', 'w':'\/\/', 'x':'}{', 'y':'`/', 'z':'2'}

plain = input().lower()
output = ""

for char in plain:
	if char in dictionary:
		output += dictionary[char]
	else:
		output += char
	
print(output)