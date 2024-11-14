a,b=input().split()
if a==b:
    print('NULL')
elif (a=='R' and b=='S') | (a=='P' and b=='R') | (a=='S' and b=='P'):
    print('Vignesh')
else:
    print('Charan')
