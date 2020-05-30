from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

n = ii()
a = liis()
ans = 0
for i in range(n):
	new_a = a[:]
	start = i
	end = i
	while start > 0:
		start -= 1
		new_a[start] = min(new_a[start], new_a[start+1])
	while end < n-1:
		end += 1
		new_a[end] = min(new_a[end], new_a[end-1])
	if sum(new_a) > ans:
		new_ans = new_a[:]
		ans = sum(new_a)
	
print(" ".join(map(str, new_ans)))

