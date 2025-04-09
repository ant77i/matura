import math

# 3.1

f = open("./dane/liczby.txt", "r")
fOut = open("./rozwiazania/wyniki3.txt", "w")
first = -1
ans = 0

for line in f.readlines():
	if math.sqrt(int(line)) == math.floor(math.sqrt(int(line))): 
		if first == -1: first = int(line)
		ans += 1

fOut.write(str(ans) + ' ' + str(first))