def isUnique(str):
    hash = {}
    str = str.lower()
    
    for i in str:
        if i in hash:
            return False
        else:
            hash[i] = 1
    return True
    
    

print(isUnique("Adele"))