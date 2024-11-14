x,y,z=list(map(int, input().split()))
a=x*y
b=z*24*60
if a<=b:
    print('YES')
else:
    print('NO')
