from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

a, b = iis()
if a%2 == 0 and b%2 == 0:
	print("OUT")
elif a%2 == 1 and b%2 == 0:
	print("IN")
elif a%2 == 0 and b%2 == 1:
	print("OUT")
else:
	print("IN")
