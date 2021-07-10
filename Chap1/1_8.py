import copy

def zeromatrix(x):
    h = copy.copy(x)
    nnn = []
    for m in list(range(0,len(x))):
        if 0 in x[m]:
                nnn.append(m)

    for m in list(range(0,len(x))):
        for n in list(range(0,len(x[m]))):
            if 0 in x[m]:
                h[m][n] = 0
            for b in list(range(len(x))):
                if x[m][n] == 0:
                    h[b][n] = 0

    return x

print(zeromatrix([[1,2,3,4],
                  [2,4,0,4],
                  [7,0,5,4],
                  [1,1,1,1]]))
