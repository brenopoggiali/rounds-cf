from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

ans = [0]
start = 0
for i in range(1, 5*10**5+1, 2):
	ans.append(ans[-1]+(i*4-4)*start)
	ans.append(ans[-1])
	start += 1

t = ii()
for _ in range(t):
	n = ii()
	print(ans[n])
