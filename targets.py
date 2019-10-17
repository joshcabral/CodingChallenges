import sys
import math 
rects =[]
circs = []
points = []
numTargets = 0
numPoints = 0

def inCircle(cx, cy, r, px, py):
	dist = math.sqrt((px-cx)**2 + (py-cy)**2)
	return (dist <= float(r))
	
def inRect(rx1, ry1, rx2, ry2, px, py):
	return ((rx1<=px and rx2>=px) and (ry1<=py and ry2>=py))

for line in sys.stdin:
	#if line == "\n":
	#	break
	if numTargets == 0:
		numTargets = int(line)
	else: 
		parts = line.split(' ')
		if parts[0] == "rectangle":
			rects.append([int(parts[1]),int(parts[2]),int(parts[3]),int(parts[4])])
		elif parts[0] == "circle":
			circs.append([int(parts[1]),int(parts[2]),int(parts[3])])
		elif len(parts) == 1:
			numPoints = int(parts[0])
		elif len(parts) == 2:
			points.append([int(parts[0]),int(parts[1])])
		else:
			print("Oops")
			
for point in points:
	counter = 0
	for circ in circs:
		counter += inCircle(circ[0],circ[1],circ[2], point[0], point[1])
	for rect in rects:
		counter += inRect(rect[0],rect[1], rect[2], rect[3], point[0], point[1])
	print(counter)

