f = open("dane\prostokaty.txt")

prevH = float('inf')
prevW = float('inf')
c = 1
maxC = -float('inf')

for line in f.readlines():
    h,w = line.split(' ')
    w = w[:-1]
    h = int(h); w = int(w)

    if (h <= prevH and w <= prevW):
        c += 1
    else:
        if (c >= maxC):
            print(c, prevH, prevW)
            maxC = c
    
        c = 1

    prevH = h
    prevW = w