from math import sqrt

n = int(input())

count = 1
for i in range(2, int(sqrt(n))+1):
	if n%i == 0:
		count += 1
print(n//count)
