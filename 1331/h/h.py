from sys import exit
from math import factorial

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def doublefactorial(n):
	if n == 0 or n == 1:
		return 1
	return n*doublefactorial(n-2)

t = input()
i1 = int(t[:-3])
i2 = int(t[-3:])
print(doublefactorial(i1)%i2)
