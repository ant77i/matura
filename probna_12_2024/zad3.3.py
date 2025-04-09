
f = open("./dane/liczby.txt", "r")
fOut = open("./rozwiazania/wyniki3.txt", "a")

mn = 0
wi = 0
row = 0

for num in f.readlines():
	num = num[:-1]
	roz = int("".join(sorted(num, reverse=True))) - int("".join(sorted(num)))

	n = int(num)
	if (roz > n): wi += 1
	elif (roz < n): mn += 1
	else: 
		row += 1
		print(n)
fOut.write(f"\n{mn} {wi} {row}")