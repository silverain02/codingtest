#ch12_8문자열 재정렬
#입력받기
import sys
import copy
input = sys.stdin.readline().rstrip
lst = list(input()) #str타입
copy_lst = copy.deepcopy(lst)
result = 0
for elem in copy_lst: #리스트 전체 순회하며 숫자 제거
    if 48<=ord(elem)<=57: #0~9숫자인 경우
        result += int(elem)
        lst.remove(elem)
        
#남은 문자 알파벳 순서로 정렬
lst.sort()

#출
for elem in lst:
    print(elem,end='')
print(result)