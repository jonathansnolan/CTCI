def oneaway(x,y):
    # INSERT
    x = list(x)
    y = list(y)
    if (len(x)+1) == len(y):
        for k in x:
            if k in y:
                continue
            else:
                return "1 FUCK"

    # REMOVAL
    if (len(x)-1) == len(y):
        for k in y:
            if k in x:
                continue
            else:
                return "2 FUCK"

    # REPLACE
    count = 0
    if len(x) == len(y):
        x = list(dict.fromkeys(x))
        y = list(dict.fromkeys(y))
        for k in x:
            if k in y:
                count += 1
        if len(x) != (count+1):
            return "3 FUCK"

    return "WE ARE LAUGHING"


###############################
print(oneaway("pale", "ple"))
print(oneaway("pales", "pale"))
print(oneaway("pale", "bale"))
print(oneaway("pale", "bake"))
