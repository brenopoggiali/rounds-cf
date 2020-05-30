from sys import stdin
input = stdin.buffer.read().split(b'\n')[::-1].pop

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def soma(a, b):
	return ((b+a)*(b-a+1))//2

n, x = iis()
d = liis()
months = []	
for i in d:
	months.append(soma(1, i))
maxi = 0
days = 0
hugs = 0
month_begin = 0
day_begin = 1
for idx, i in enumerate(d):
	days += i
	hugs += months[idx]
	if days >= x:
		break
month_end = idx
day_end = d[idx]-(days-x)
if days > x:
	hugs -= soma((i-(days-x)+1), d[idx])

maxi = max(maxi, hugs)
flag = True
while flag or (day_begin != 1 or month_begin%n != 0):
	hugs -= day_begin
	day_begin += 1
	if day_begin > d[month_begin%n]:
		month_begin += 1
		day_begin = 1
	day_end += 1
	if day_end > d[month_end%n]:
		month_end += 1
		day_end = 1
	hugs += day_end
	maxi = max(maxi, hugs)
	flag = False


print(maxi)
