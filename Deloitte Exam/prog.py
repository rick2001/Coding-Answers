def answer(string):
    count=0
    hashmap={}
    for i in range(len(string)):
        if string[i] in hashmap:
            hashmap[string[i]]+=1
        else:
            hashmap[string[i]]=1
    # print(hashmap)
    
    for val in hashmap:
        if hashmap[val] >=2:
            count+=hashmap[val]//2
    
    return count


string="abcabcd"
v=answer(string)
print(v)
