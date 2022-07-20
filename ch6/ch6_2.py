#ch6_2 위에서 아래로 #5:18~5:23
N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

#내림차순 정렬
lst.sort(reverse = True)

for i in lst:
    print(i, end =' ')