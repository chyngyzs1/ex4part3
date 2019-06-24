a = [1,2,3,4,6]
a.sort()
print(a)
min = a[0]
for i in a:
    if i < 0:
        min = 1
    elif i == min:
        min = min + 1
print(min)