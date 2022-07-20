#ch6_#4 두 배열의 원소 교체 1:50~2:00
N,K = map(int,input().split())
lstA = list(map(int,input().split()))
lstB = list(map(int,input().split()))
#배열A 내림차순, 배열B 오름차순 정렬
lstA.sort()
lstB.sort(reverse =True)
#K번 바꿔치기
for i in range(K):
    if lstA[i] >= lstB[i]: #배열A 원소가 더 크면 멈춤
        break
    else:
        lstA[i],lstB[i] = lstB[i],lstA[i]
#합 출력
result = 0
for elem in lstA:
    result += elem
    
print(result)