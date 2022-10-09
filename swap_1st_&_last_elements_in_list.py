#swapping the first and last elemnets of a list
def swaplist(new_list,n):
    temp = new_list[0]
    new_list[0]= new_list[n-1]
    new_list[n-1]= temp
    return new_list

lis = [1,2,3,4]
n = len(lis)
print(swaplist(lis,n))