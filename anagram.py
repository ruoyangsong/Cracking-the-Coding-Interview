def number_needed(a, b):
    c = list(a)
    d = list(b)
    if(len(c)<=len(d)):
        num = 0
        for i in c:
            if (i in d):
                d.remove(i)
            else: 
                num += 1
        num += len(d)
        return num
    else:
        num = 0
        for i in d:
            if (i in c):
                c.remove(i)
            else:
                num +=1
        num +=len(c)
        return num

a = input().strip()
b = input().strip()

print(number_needed(a, b))
