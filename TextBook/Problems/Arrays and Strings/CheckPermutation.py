def CheckPermutation(strA, strB):
    strA = strA.lower()
    strB = strB.lower()

    strA = sorted(strA)
    strB = sorted(strB)

    return strA == strB


print(CheckPermutation("abc", "cba"))  # True
print(CheckPermutation("jack", "jacob"))  # False
