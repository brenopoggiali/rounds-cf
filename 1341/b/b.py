from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
    n, k = iis()
    A = liis()
    is_peak = [0 for i in range(n)]
    for i in range(1, n-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            is_peak[i] = 1
    cur = sum(is_peak[:k-1]) + 1
    soma = [[cur, -1]]
    for i in range(k, n):
        cur += is_peak[i-1]
        cur -= is_peak[i-k+1]
        soma.append([cur, -(i-k+2)])
    soma = sorted(soma)[::-1]
    #print(soma)
    #print(is_peak)
    print(soma[0][0], -soma[0][1])
