#ch8-2 1로만들기//탑다운

x =int(input())
#메모라이제이션 리스트
d = [0]*100
#탑다운 다이나믹(재귀)
def make(n):
    #1이 되면 멈춤
    if n == 1:
        return 0
    #이전에 연산한 적 있음
    if d[n] != 0:
        return d[n]
    #이전에 연산한 적 없음
    d[n] = make(n-1)+1
    if n%5 == 0:
        d[n]=min(d[n],make(n//5)+1)
    if n%3 == 0:
        d[n]=min(d[n],make(n//3)+1)
    if n%2 == 0:
        d[n]=min(d[n],make(n//2)+1)
    return d[n]
make(x)
print(d[x])