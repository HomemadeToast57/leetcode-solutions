def URLify(str):

    str = str.strip()  # strip string of leading/trailing spaces to insure we are in char limit

    str = str.replace(" ", "%20")  # swap space for "%20"

    return str


print(URLify("Mr John Smith"))
