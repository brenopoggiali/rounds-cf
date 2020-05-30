from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

n, k = iis()
p = liis()
a = n-k+1
b = n
ans1 = (((b-a+1)*(b+a))//2)
positions = []
for idx, i in enumerate(p):
	if i >= a:
		positions.append(idx)
ans2 = 1
for i in range(1, len(positions)):
	ans2 *= positions[i]-positions[i-1]

print(ans1, ans2%998244353)
