# 스택(stack) 이란?
# 후입선출(LIFO : List in,First Out) 선형 자료구조.
# 마지막에 추가된 항목이 가장 먼저 제거되는 구조, 상단에서만 데이터를 삽입하고 삭제할 수 있다.
# 스택은 컴퓨터 과학에서 매우 중요한 개념으로, 다양한 알고리즘과 데이터 처리 과정에 활용

# stack 은 리스트로 []
# push -> append 함수를 사용하여 stack에 값을 추가
# push : 스택 맨 윗부분에 추가할 항목이 들어감
# pop : pop 함수를 사용하여 스택에 가장 위에 있는 값을 꺼냄
# pop : len(길이)를 사용하여 스택 안에 값이 있는지 없는지 확인 
# size : len(길이) 함수를 사용하여 스택에 들어있는 정수의 개수를 출력
# empty : len(길이) 함수를 사용하여 스택 값이 있는지 없는지에 따라 출력


# import sys 를 사용하는 이유?
# -> input함수를 사용할 경우, 입력 받을 때 느리기 때문에 시간 초과가 뜰 수 있어서
import sys

# print("시작값을 입력하세요: ")  # 안내 메시지를 출력
number = int(sys.stdin.readline())
# sys.stdin.readline() 한줄 전체 출력 코드
# sys.stdin.readline()을 사용하면 input 보다 속도가 빠르게 출력 된다다

stk = []
# stack 을 리스트로 저장시킨다
# 리스트로 할경우 추가, 삭제를 할 수있음
# 튜플로 저장할 경우 안에 요소를 추가 및 변경, 삭제가 불가능하기 떄문

def push(n):
    stk.append(n)
# push는 append 함수를 사용해서 스택에 값을 추가가

def pop():
    if len(stk) == 0:
        print(-1)
    else:
        print(stk.pop())

# pop 함수는 스택에서 가장 위에 있는 요소를 꺼내고 그 값을 출력
# pop 함수는 가장 위에 있는 항목을 제거하고 반환한다

def size():
    print(len(stk))
    
def empty():
    if len(stk) == 0:
        print(1)
    else:
        print(0)
        
def top():
    if len(stk) == 0:
        print(-1)
    else:
        print(stk[-1])

# print(stk[-1]) 이유?
# 스택 안에 요소가 얼마나 들어있는지 모르기 때문에
# top 명령어는 가장 위에 있는 정수를 출력

for i in range(number):
    text = sys.stdin.readline().split()
    if text[0] in 'push':
        push(int(text[1]))
    if text[0] in 'pop':
        pop()
    if text[0] in 'size':
        size()
    if text[0] in 'empty':
        empty()
    if text[0] in 'top':
        top()

#     if text[0] in 'push':
#       push(text[1])
# split을 사용해서 입력받은 값에 공백이 있을경우 split으로 나눔
# text[0] == push로 들어갈거고 뒤에 숫자가 text[1]로 들어감
# 그럼 자연스럽게 push (입력받은 값) push함수를 호출 할 수 있다
# 그러나 입력받은 값은 문자열이므로 앞에 int를 사용하면 숫자로 변환된다
