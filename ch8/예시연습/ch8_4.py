#ch8_4 5:5~
n = int(input())
if n%2 == 0: #n짝수
    result = 3**(n//2)
else: #홀수
    result = (3**((n-1)//2))*(((n-1)//2)+1)
print(result%769796)