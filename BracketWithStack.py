def is_matched(expression):
    stack = []
    dic = {'(':')', '[':']', '{':'}'}
    for x in expression:
        if x in dic:
            stack.append(dic[x])
        else:
            if len(stack) == 0 or x != stack[len(stack)-1]:
                return False
            stack.pop()
    return len(stack) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")