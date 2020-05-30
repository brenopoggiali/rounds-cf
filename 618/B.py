t = int(input())

for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	a = sorted(a)
	A, B = [], []
	for i in range(0, len(a), 2):
		A.append(a[i])
		B.append(a[i+1])
	if len(A)%2 == 0:
		A.append(B.pop())
	print(abs(A[len(A)//2]-B[len(B)//2]))

