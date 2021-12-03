def forward(curr, num):
	return curr + num


def up(curr, num):
	return curr-num


def down(curr, num):
	return curr+num


# main program
F = "input.txt"

file1 = open(F, 'r')
linecount = 0
posho = 0  # horizontal position
depth = 0  # depth

while True:
	linecount += 1

	line = file1.readline()

	if not line:
		break

	splitline = line.split(" ")
	cmd = splitline[0]
	val = int(splitline[1])

	if cmd == "forward":
		posho = forward(posho, val)
	elif cmd == "up":
		depth = up(depth, val)
	elif cmd == "down":
		depth = down(depth, val)
	else:
		print("We all live in a yellow submarine!\n")

print("\n\n------------------------------\nHorzPos: {}\nDepth: {}\nResult: {}".format(posho, depth, (posho * depth)))
file1.close()
