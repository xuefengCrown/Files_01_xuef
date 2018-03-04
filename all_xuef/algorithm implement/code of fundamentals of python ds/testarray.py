from arrays import Array

a = Array(5)
print(a)
print(len(a))

for i in range(len(a)):
    a[i] = i + 1

for item in a:
    print(item)
