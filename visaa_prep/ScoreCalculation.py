T = int(input())
for _ in range(T):
    X, N = map(int, input().split())
    P = X // 10
    score = P * N
    print(score)
