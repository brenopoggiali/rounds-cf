from sys import exit
#from bisect import bisect
#from collections import deque

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

n = ii()
a = liis()
b = liis()
v = []
for i in range(len(a)):
	v.append(a[i]-b[i])
v = sorted(v)[::-1]
count = 0
#print(v)
last = len(v)-1
for idx, i in enumerate(v):
	while last > idx and i+v[last] <= 0:
		last -= 1
	#print(i, last, i-v[last], last-idx)
	#print(v[idx], v[last])
	if last > idx:
		count += last-idx


print(count)


