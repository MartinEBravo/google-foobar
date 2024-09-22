def solution(x, y):
    # Your code here
    result = 1
    i,j = 1,1
    while j < y:
        result += i
        i += 1
        j += 1
    i = 1
    j = y+1
    while i < x:
        result += j
        i += 1
        j += 1
    return str(result)




assert solution(1, 1) == '1'
assert solution(2, 1) == '3'
assert solution(2, 2) == '5'

