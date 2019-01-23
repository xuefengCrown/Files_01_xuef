def trans():
    import re
    pat  = re.compile(r"print (.*$)")
    for line in s.split("\n"):
        subed = re.sub(pat, r"    print(\1)", line)
        print(subed)
