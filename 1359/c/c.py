from sys import stdin
import fractions
input = stdin.readline


def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


def eq(x):
  return F((h*x + c*(x-1)), (x+x-1))


def bin_ser(lb, ub, lv, uv, target):
  elm_mid = lb
  while abs(lb-ub) > 1:
    elm_mid = (lb+ub)//2
    mid = eq(elm_mid)
    if mid < target:
      ub = elm_mid
      uv = mid
    elif mid > target:
      lb = elm_mid
      lv = mid
    else:
      break
  return elm_mid


F = fractions.Fraction

t = ii()
for _ in range(t):
  h, c, t = iis()
  if t <= (h+c)/2:
    print(2)
  elif t >= h:
    print(1)
  else:
    i = 1
    while True:
      i *= 2
      calc = eq(i)
      if calc < t:
        mid = (bin_ser(1, i, h, calc, t))
        ops = [[mid-1, eq(mid-1)], [mid, eq(mid)], [mid+1, eq(mid+1)]]
        mini = float("inf")
        resp = float("inf")
        for i, j in ops:
          if abs(t-j) < mini:
            mini = abs(t-j)
            resp = i
        print(resp*2-1)
        break
