def spiralOrder(arr):
    ans=[]
    while arr:
        ans+=arr.pop(0)[::-1]
        arr= (list(zip(*arr)))[::-1]
    return ans
arr=[[1, 2, 3],[4,5,6],[7,8,9]]
print(spiralOrder(arr))
