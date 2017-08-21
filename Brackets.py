def pair(ex):
    if(ex=="{"):
        return "}"
    elif(ex=="["):
        return "]"
    elif(ex=="("):
        return ")"
    elif(ex=="]"):
        return "["
    elif(ex=="}"):
        return "{"
    elif(ex==")"):
        return "("
def is_matched(expression):
    if ((len(expression)%2)!=0):
        return False
    else:
        full = int(len(expression))
        half = int(len(expression)/2)
        for i in range(half):
            if(pair(expression[i])!=expression[full-i-1]):
                return False
    return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")