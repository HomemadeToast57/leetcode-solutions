def PalindromePermutation(str):
    str = str.lower()
    str = str.strip()
    str = str.replace(" ", "")

    map = {}

    bad = 0

    for e in str:
        if not e in map:
            map[e] = 1
        else:
            map[e] += 1

    for key in map:
        if not map[key] % 2 == 0:
            bad += 1

    return not bad > 1


print(PalindromePermutation("abcccdagba"))
