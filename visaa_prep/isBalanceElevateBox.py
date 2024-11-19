n=int(input())
arr=list(map(int, input().split()))
ba=[]
total_sum=sum(arr)
lw=0
for i in range(n):
    rw = total_sum-lw-arr[i]
    ba.append(abs(lw-rw))
    lw+=arr[i]
print(" ".join(map(str, ba)))
