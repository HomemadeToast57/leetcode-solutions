def OneAway(str1, str2):

    if abs(len(str1) - len(str2)) > 1:  # check if difference in length of more than 1 char
        return False

    madeEdit = False  # keep track if we made an "edit" already
    # init pointers to 0 (we will use these pointers to step through the strings)
    p1, p2 = 0, 0

    while p1 < len(str1) and p2 < len(str2):  # loop through both strings (uses )
        if str1[p1] == str2[p2]:  # if char is same, we can step to next pair
            p1 += 1  # step
            p2 += 1
        # if we have not made an edit yet at this point, we will enter. Otherwise, we will return False.
        elif not madeEdit:
            madeEdit = True  # mark that we made an edit

            # Represents replacement (we got here because str1[p1] != str2[p2])
            if len(str1) == len(str2):
                p1 += 1
                p2 += 1
            # We "delete" the char at p2 and increment p2 while not incrementing p1
            elif len(str1) > len(str2):
                p1 += 1
            # Same for p1
            elif len(str1) < len(str2):
                p2 += 1
        else:
            return False
    return True


print(OneAway("whale", "wrale"))  # True
print(OneAway("rake", "care"))  # False
print(OneAway("rake", "rake"))  # True

# Time Complexity - O(n)
