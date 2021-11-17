def StringRotation(x1, x2):
    str = x2 + x2
    return str.find(x1) != -1

print(StringRotation("waterbottle", "erbottlewat")) # True
print(StringRotation("Test", "est")) # False
print(StringRotation("CodingInterview", "erviewCodingInt")) # True