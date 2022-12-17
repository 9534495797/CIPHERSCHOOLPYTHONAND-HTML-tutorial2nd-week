def reverse_element(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
words=["abc","def","ghi"]
print(reverse_element(words))