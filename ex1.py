#11047
N,K = map(int,input().split())
L = []
result = 0
cnt = 0
for i in range(N):
    L.append(int(input()))
#내림차순 정렬
L.sort(reverse=True)
for i in L:
    while K>=i:
        K -= i
        cnt += 1
    if K == 0:
        break

print(cnt)