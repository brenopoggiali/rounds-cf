from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

n = ii()
b = liis()

maxi = [0]
a = [b[0]]
maxi_a = a[0]
for i in range(len(b)-1):
	maxi_a = max(maxi_a, a[i])
	maxi.append(maxi_a)
	a.append(b[i+1]+maxi[i+1])
print_array(a)
