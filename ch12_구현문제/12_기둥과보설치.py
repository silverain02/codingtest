#12_기둥과 보 설치 // 실
import copy
answer = []
#'보' 설치 가능 여부 확인
#한쪽 끝이 기둥 위 or 양쪽끝 보
def ck_bmp(x,y,answer):
    if ([x,y-1,0] in answer) or ([x+1,y-1,0] in answer) or ([x-1,y,1] in answer and [x+1,y,1] in answer):
        return True
# '기둥' 설치 가능 여부 확인
def ck_plr(x,y,answer):
    if y==0 or ([x-1,y,1] in answer) or ([x,y,1] in answer) or ([x,y-1,0] in answer):
        return True
    
#선택정렬 함수
def srt(lst,c):
    for i in range(len(lst)):
        min_index=i
        for j in range(i+1,len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
    lst[i],lst[min_index] = lst[min_index],lst[i]

def solution(n, build_frame):
    ck = 1
    
    #buil_frame 순회
    for elem in build_frame:
        
        x,y,a,b=elem[0],elem[1],elem[2],elem[3]
        
        #설치모드
        if b:
            #보의 설치 조건 확인 // 한쪽 끝이 기둥 위 or 양쪽끝 보
            if a and not(ck_bmp(x,y,answer)):
                continue #작업무시
            #기둥의 설치 조건 확인// 바닥 or 보의 한쪽 끝 위 or 기둥 위
            elif not(a) and not(ck_plr(x,y,answer)): 
                continue #작업무시
            #설치 > answer삽입
            answer.append([x,y,a])
        #삭제모드
        else:
            copied_answer = copy.deepcopy(answer)
            #전체 answer돌면서 조건 맞는지 확인
            copied_answer.remove([x,y,a])
            for elem2 in copied_answer:
                if elem2[2] and ck_bmp(elem2[0],elem2[1],copied_answer): #보
                    continue
                elif not(elem2[2]) and ck_plr(elem2[0],elem2[1],copied_answer): #기둥
                    continue
                else: #조건 틀린 경우
                    ck = 0
                    break
            if ck: #조건이 맞은 경우
                answer.remove([x,y,a])
            
    #결과리스트 정렬
    #x 기준 오름차순 정렬
    answer.sort(key=lambda answer: answer[0])
    #x 똑같은 경우 > y 기준 정렬
    cnt1 = 1
    for i in range(len(answer)-1):
        if answer[i][0] == answer[i+1][0]:
            cnt1 +=1
        else:
            answer[i-cnt1:i+1].sort(key=lambda answer: answer[1])
            cnt1 = 1
    #x,y모두 똑같은 경우 > a기준 정렬
    cnt2 = 1
    for i in range(len(answer)-1):
        if answer[i][0] == answer[i+1][0] and answer[i][1] == answer[i+1][1]:
            cnt2 +=1
        else:
            answer[i-cnt2:i+1].sort(key=lambda answer: answer[2])
            cnt2 = 1
    return answer
print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))