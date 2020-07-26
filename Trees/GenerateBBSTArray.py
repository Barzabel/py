def GenerateBBSTArray(a):
    a.sort()
    res = [None]*len(a)
    ur = 0
    l = len(a) - 1
    while l > 1:
        ur = ur + 1
        l = l//2


    li = [a]
    indexlist2 = [0]

    indexlist1 = []
    li1 = []

    for x in range(ur+1):

        for y in range(len(indexlist2)):

            res[indexlist2[y]]=li[y][len(li[y])//2]

        for y in range(len(indexlist2)):
            indexlist1.append(indexlist2[y] * 2 + 1)
            indexlist1.append(indexlist2[y] * 2 + 2)




            li1.append(li[y][:len(li[y])//2])
            li1.append(li[y][len(li[y])//2+1:])

        indexlist2 = indexlist1
        li = li1

        indexlist1 = []
        li1 = []

    return res
