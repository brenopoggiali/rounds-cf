from sys import stdin, exit
input = stdin.readline

def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


t = ii()
for _ in range(t):
    a, b, q = iis()
    a, b = min(a, b), max(a, b)
    ans = []
    if a % b == 0 or b % a == 0:
        for i in range(q):
            l, r = iis()
            ans.append(0)
        print_array(ans)
        continue
    for i in range(q):
        l, r = iis()
        c = 0
        for x in range(l, min(r+1, 4000)):
            if (x % a) % b != (x % b) % a:
                c += 1
        c2 = 0
        for x in range(4000, min(r+1, 8000)):
            if (x % a) % b != (x % b) % a:
                c2 += 1
        c += c2*(r//4000)
        for x in range(max(r//4000*4000, 8000), r+1):
            if (x % a) % b != (x % b) % a:
                c += 1
        ans.append(c)
    print_array(ans)
