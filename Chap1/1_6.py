def stngcomp(string):
    x = list(string)
    count = 1
    y = string[0]
    i = ""
    for k in list(range(1,len(x))):
        if string[k] == y:
            count += 1
            y = string[k]
        elif string[k] != y:
            i += y + str(count)
            count = 1
            y = string[k]

    ans = i+y+str(count)

    if len(ans) > len(string):
        return string
    else:
        return ans

print(stngcomp("aabcccccaaal"))
print(stngcomp("abcdef"))
