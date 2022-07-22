#ch7_2 부품 찾기 6:15~6:25
#입력받기
n = int(input())
storage = list(map(int,input().split()))
m = int(input())
search = list(map(int,input().split()))

for i in search:
    for j in storage:
        if i == j:
            print('yes', end=' ')
            break
        elif storage.index(j) == n-1: #마지막 원소
            print('no', end=' ')