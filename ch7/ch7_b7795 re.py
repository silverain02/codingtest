#ch7_b2 new 7795 먹을 것인가 먹힐 것인가 // 시간초과
#이진탐색(재귀함수)
import sys

def binary_search(arr,t,s,e):
    if s>e:
        return None
    mid = (s+e) //2
    if arr[mid] == t:
        return mid
    elif arr[mid]>t:
        return binary_search(arr,t,s,mid-1)
    else:
        return binary_search(arr,t,mid+1,e)
    return None #t가 없는 경우
t = int(sys.stdin.readline())
for i in range(t):
    #입력받기
    n,m = [int(x) for x in sys.stdin.readline().split()]
    lstA = [int(x) for x in sys.stdin.readline().split()]
    lstB = [int(x) for x in sys.stdin.readline().split()]
    #이진탐색을 위한 정렬
    lstA.sort()
    lstB.sort()
    stack = [0]*n
    for i in range(len(lstA)):
        if binary_search(lstB,lstA[i],0,m-1) == None:
            if max(lstB) < lstA[i]: 
                stack[i] = m
            elif min(lstB) > lstA[i]:
                stack[i] = 0
            else: #min,max사이 값인데 lstB에 없는 경우
                lstB.append(lstA[i])
                lstB.sort()
                stack[i] = binary_search(lstB,lstA[i],0,m-1)
                lstB.remove(lstA[i])
        else:
            stack[i] = binary_search(lstB,lstA[i],0,m-1)
    #stack리스트 합 출력
    print(sum(stack))
