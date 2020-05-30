from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


n = ii()
for i in range(2, n):
	if n%i == 0:
		print(str(i)+str(n//i))
		break
