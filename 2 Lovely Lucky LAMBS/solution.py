def solution(total_lambs):
    if (total_lambs>=10**9):
        return 0
    return stingy(total_lambs) - generous(total_lambs)
def generous(lambs):
    s = 0
    i = 0
    numbers = []
    while s <= lambs:
        numbers.append(pow(2,i))
        i+=1
        s = 0
        for j in numbers:
            s += j
    
    return i-1
def stingy(lambs):
    num = 1
    cur = 0
    s = 0
    numbers = []
    while s <= lambs:
        numbers.append(num)
        if (cur == 0):
            num += 0
        else:
            num = numbers[cur] + numbers[cur-1]
        cur += 1
        s = 0
        for i in numbers:
            s += i
    return cur-1