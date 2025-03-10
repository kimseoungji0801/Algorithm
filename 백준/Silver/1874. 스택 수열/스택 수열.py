import sys

number = int(sys.stdin.readline())

stk = [] # 스택 생성
asr = [] # 값을 받을 리스트 생성
count = 1 # 1로 시작해야 while문에서 올바르게 push를 할 수 있다다
for i in range(number): 

    num = int(sys.stdin.readline())
    
    while count<= num: #num 이하 숫자까지 스택에 넣기
        stk.append(count) # count값이 1씩 증가하면서 스택에 넣을 수 있다
        asr.append('+') # asr값에는 '+' 값 추가
        count +=1
    
    if stk[-1] == num: # 스택 수열의 맨 위에 값이 num과 동일하면 제거거
        stk.pop()      
        asr.append('-') # asr값에 '-' 값을 추가
    else:
        asr.clear() # clear함수를 사용해서 asr 리스트 안에 있는 요소 전부 제거
        asr.append('NO') # 'NO' 값을 추가가
        break

for j in asr: # 리스트 안에 있는 요소만큼 반복
    print(j)