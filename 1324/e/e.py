from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


def new_time(h, d, s):
	return (d-s)%h

def binarySearch(limit, h, time, max_sobra):
	l = 0
	r = max_sobra
	while l < r:
		middle = (l+r)//2
		if new_time(h, time, middle) < limit:
			r = middle
		else:
			l = middle+1
	return l
	

n, h, l, r = iis()
a = liis()
time = 0
good = 0
min_sobra = 0
max_sobra = 0
for i in a:
	time += i
	time %= h
	max_sobra += 1
	#print(time, sobra, l, r)
	if new_time(h, time, max_sobra) <= r and time >= l:
		min_sobra += binarySearch(l, h, time, max_sobra)
		max_sobra -= binarySearch(r, h, time, max_sobra)
		good += 1
	max_sobra -= min_sobra
	time -= min_sobra
	min_sobra = 0
	
print(good+1)

