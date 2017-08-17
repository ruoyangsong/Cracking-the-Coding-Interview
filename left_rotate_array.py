def array_left_rotation(a, n, k):
    b = []
    b.extend(a[k:])
    b.extend(a[0:k])
    return b

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')