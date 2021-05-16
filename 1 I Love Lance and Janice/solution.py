def solution(s):
    output = ""
    for i in s:
        if (i in chars):
            output += inverts[chars.index(i)]
        else:
            output += i
    print(output)

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
inverts = chars[::-1]