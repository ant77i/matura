# 1.2
n = int(input())

i = 1
while n > 0:
	if n % 2 == 1: print(i)

	n //= 2
	i += 1