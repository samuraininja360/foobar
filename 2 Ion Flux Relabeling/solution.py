import math

def calcsize(height):
    return int(math.pow(2, height) - 1)

def shiftright(value, bits):
    return (value & 0xffffffffL) >> bits

def findparent(height, node):
    size = calcsize(height)
    if node == size:
        return -1

    previous = 0
    while True:
        size = shiftright(size, 1)
        left = previous + size
        right = left + size
        current = right + 1
        if left == node or right == node:
            return current

        if node > left:
            previous = left

    return 0

def solution(h, q):
    return [findparent(h, n) for n in q]