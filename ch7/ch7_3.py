#ch7_3 떡볶이 떡 만들기 6:35~6:55
n,m = map(int,input().split())
lst = list(map(int,input().split()))

for cut in range(max(lst),0,-1):
    result = 0
    for elem in lst:
        if elem > cut:
            result += elem-cut
    if result >= m:
        print(cut)
        break
            
