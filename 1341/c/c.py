from sys import stdin, exit
import bisect
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
    n = ii()
    p = liis()
    P = [[i, idx] for idx, i in enumerate(p)]
    P = sorted(P)
    used = [0 for i in range(n)]
    numbers = set()
    can = True
    last = n
    for j in P:
        i = j[0]
        idx = j[1]
        for k in range(idx, last):
            last = idx
            if k == idx:
                if used[k]:
                    can = False
                    break
                used[k] = 1
            elif used[k] or p[k] != p[k-1]+1:
                can = False
                break
            used[k] = 1

    if can:
        print('Yes')
    else:
        print('No')
