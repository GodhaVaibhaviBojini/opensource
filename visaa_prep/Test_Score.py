n,x,y=list(map(int, input().split()))
if y<=n*x and y%x==0:
    print('YES')
else:
    print('NO')
