a,b,c,x=list(map(int, input().split()))
if (a+b>=x) | (a+c>=x) | (b+c>=x):
    print('YES')
else:
    print('NO')
