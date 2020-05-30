n = int(input())
d = int(input())
e = int(input())

ans = 0

if d != 0 and e != 0 and n != 0:
    max_d = n//d
    max_d_rest = (n%d)//(e*5)

    max_e = n//(e*5)
    max_e_rest = (n%(e*5))//d

    first = n-(max_d)*d-(max_d_rest)*e*5
    second =  n-(max_e)*e*5-(max_e_rest)*d

    ans = min(first, second)

print(ans)
