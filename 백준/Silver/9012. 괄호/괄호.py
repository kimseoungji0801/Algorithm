number = int(input())
for i in range(number):
    st = input()
    stk = []
    Test = True

    for j in st:
        if j == '(':  # 여는 괄호일 경우 스택에 추가
            stk.append(j)
        elif j == ')':  # 닫는 괄호일 경우
            if len(stk) == 0:  # 스택이 비어 있으면 올바르지 않은 괄호
                Test = False
                break
            elif stk[-1] == '(':  # 짝이 맞는 여는 괄호가 있으면 제거
                stk.pop()

    if Test and len(stk) == 0:
        print('YES')
    else:
        print('NO')