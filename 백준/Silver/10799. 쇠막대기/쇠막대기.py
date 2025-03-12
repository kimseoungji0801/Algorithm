stk = []
bar = 0
par = list(input())

for i in range(len(par)) :
    if par[i] == '(':
        stk.append('(')
    else :    
        if par[i-1] == '(':
            stk.pop()
            bar += len(stk)
        else:
            stk.pop()
            bar += 1    

print(bar)