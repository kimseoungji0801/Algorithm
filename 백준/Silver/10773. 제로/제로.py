import sys

number = int(sys.stdin.readline())
stk = []

for i in range(number):

    money = int(input())
    if money == 0:
        stk.pop()
    else :
        stk.append(money)
print(sum(stk))
