
def permutation(n):

    if n == 3:
        fix = n+1
        mainlist = []

    sublist = []
    for x in range (1, fix):
        if x != n:
            sublist.append(x)
    sublist.append(n)
    mainlist.append(sublist)

    for y in range (1, fix, -1):
        if y != n:
            sublist.append(y)
    sublist.append(n)
    mainlist.append(sublist)

    minvalue = fix-1
    if minvalue != 0:
        permutation(minvalue)
    else:
        print(mainlist)

permutation(3)