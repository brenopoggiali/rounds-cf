from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

s = input()
if (int(s[-1])%2 == 0):
	print(0)
else:
	print(1)
