file1 = open("input.txt", 'r')
linecount = 0
depthincrease = 0
window = 3
prevLine = 10000 #something larger
prevWindowCnt = 10000 # something larger

lines = file1.readlines()

for line in lines:
	linecount += 1
	windowCnt = 0
	for i in range(1,window+1):
		if len(lines) > (linecount+i):
			line = int(lines[linecount+i])
			windowCnt += line
			print("{}: {} --> {}".format(i, line, windowCnt))


	if prevWindowCnt < windowCnt:
		depthincrease += 1
		print("{} < {} INCREASE\n".format(prevWindowCnt, windowCnt))

	prevWindowCnt = windowCnt

print("\n\n------------------------------\nLines: {}\nDepth inc.: {}".format(linecount, depthincrease))
file1.close()