#ch3_2
N,M,K = map(int,input().split())
count1 = 1
result = 0
#리스트로 N개의 자연수 입력받기
L = list(map(int,input().split()))
#리스트 내립차순 정렬
L.sort(reverse=True)
x = L[0] #가장 큰 수
y = L[1] #두번째로 큰 수

while count1 <= M: #M개의 숫자 구성
    for i in range(K):
        result += x
        count1 += 1
    result += y
    count1 += 1

print(result)