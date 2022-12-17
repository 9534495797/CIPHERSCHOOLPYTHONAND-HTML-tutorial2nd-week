# num=[1,2,3,4,5,6,7,8,9,10]
# num.pop(4)
# print(num)

num=[1,2,3,4,5,6,7,8,9]
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num))