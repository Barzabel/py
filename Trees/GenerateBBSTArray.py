def GenerateBBSTArray(a):
    a.sort()
    i =  len(a)//2
    if len(a)<2:
        return a
    else:
        res = [a[i]]+GenerateBBSTArray(a[0:i])+GenerateBBSTArray(a[i+1:len(a)])
    return res