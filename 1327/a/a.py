from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def sum_of_odds_until(n):
	n *= 2
	return ((n+(n%2))//2)**2

t = ii()
for _ in range(t):
	n, k = iis()
	can = False
	if n%2 == 1 and k%2 == 1 and sum_of_odds_until(k) <= n:
		can = True
	elif n%2 == 0 and k%2 == 0 and sum_of_odds_until(k) <= n:
		can = True
	if can:
		print("YES")
	else:
		print("NO")
