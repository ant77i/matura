f = open("dane\prostokaty.txt")

d = [[int(line.split(' ')[0]),int(line.split(' ')[1][:-1])] for line in f.readlines()]
d.sort(key= lambda x : (x[0], -x[1]))

mx = [-1, -1, -1, -1, -1, -1]

n = len(d)
for i in range(n):
    v = d[i]
    h, w = v

    for z in [2, 3, 5]:
        if i+z < n:
            sum = 0
            for j in range(i, i+z):
                localH, localW = d[j]
                if (localH != h): break

                sum += localW
            
            mx[z] = max(mx[z], sum)

print(mx)
