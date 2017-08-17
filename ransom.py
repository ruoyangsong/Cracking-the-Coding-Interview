def ransom_note(magazine, ransom):
    dic = {}
    for i in magazine:
        if(i in dic):
            dic[i] +=1
        else:
            dic[i] = 1
    for i in ransom:
        if(i in dic):
            dic[i] -= 1 
            if (dic[i] < 0):
                return False
        else:
            return False
    return True
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")