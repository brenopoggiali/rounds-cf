b = int(input())
g = int(input())
n = int(input())

if n-g > 0:
    aux = n-g
else:
    aux = 0

count = 0
for i in range(0+aux, n+1):
    count += 1
    if i >= min(b, n):
        break

print(count)
