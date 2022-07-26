#ch7_b10816 숫자카드2 // 시간초과 
import sys
#입력받기
n = int(sys.stdin.readline())
lst1 = [int(x) for x in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
lst2 = [int(x) for x in sys.stdin.readline().split()]
#정렬
lst1.sort()
#이진탐색(재귀)
def binary_search(arr,t,s,e):
    if s>e:
        return 0
    mid = (s+e) //2
    if arr[mid] == t:
        return arr.count(t)
    elif arr[mid]>t:
        return binary_search(arr,t,s,mid-1)
    else:
        return binary_search(arr,t,mid+1,e)

for i in range(m):
    cnt = binary_search(lst1,lst2[i],0,n-1) 
    print(cnt, end=' ')

