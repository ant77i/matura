from math import sqrt

f = open("./dane/liczby.txt", "r")
fOut = open("./rozwiazania/wyniki3.txt", "a")
toAdd = ""

for num in [int(line) for line in f.readlines()]:
	n = num
	ans = 0
	print(num)
	for i in range(2, n):
		if num % i != 0: continue

		while num % i == 0: num /= i
		print(f"\t{num}")
		ans += 1
	print(ans)
	if ans > 4: toAdd += f"{n} "

fOut.write(f"\n{toAdd}")

