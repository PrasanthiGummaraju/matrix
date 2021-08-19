def spiral(arr):
    ans=[]
    while arr:
        ans+=arr.pop(0)
        arr=list(zip(*arr))[::-1]
    return ans
arr=[]
r,c=[int(v) for v in input().split()]
for i in range(r):
    cur=[int(v) for v in input().split()]
    arr.append(cur)
print(spiral(arr))
[9:53 PM, 8/19/2021] Janu: Em cedam
