f = open("dane\prostokaty.txt")

mn = float('inf')
mx = -float('inf')

for line in f.readlines():
    h,w = line.split(' ')
    w = w[:-1]
    mn = min(mn, int(h)*int(w))
    mx = max(mx, int(h)*int(w))

print(mn, mx)