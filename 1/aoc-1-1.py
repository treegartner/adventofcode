F = "input.txt"

file1 = open(F, 'r')
linecount = 0
depthincrease = 0
prevLine = 10000 #something bigger  than anything.. 

while True:
	linecount += 1

	line = file1.readline()

	if not line:
		break

	line = int(line)
	
	if prevLine < line:
		depthincrease += 1
		print("{} < {} INCREASE\n".format(prevLine, line))
	else:
		print("{}\n".format(line))

	prevLine = line

print("\n\n------------------------------\nLines: {}\nDepth inc.: {}".format(linecount, depthincrease))
file1.close()
