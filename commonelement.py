def common_finder(x, y):
    output=[]
    for i in x:
        if i in y:
            output.append(i)
    return output
print(common_finder([1,2,5,8],[1,2,7,6]))