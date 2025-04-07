def F(x, p):
	if x == 0: return 0
	else:
		c = x % p
		if c % 2 == 1:
			return F(x // p, p) + c
		else:
			return F(x // p, p) - c


for i in range(99, 0, -1):
	if F(i, 3) == 0: print(i, F(i, 3))