def swapping(newlist,pos1,pos2):

    temp = newlist[pos1]
    newlist[pos1] = newlist[pos2]
    newlist[pos2] = temp
    return newlist

print(swapping([1,2,3,4,5,6],2,3))
