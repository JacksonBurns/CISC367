import re

def checkFor(data,regex):
    out =[]
    pattern = re.compile(regex)
    for line in data:
        m = pattern.search(line)
        if m:
            out = out + [1]
        else:
            out = out + [0]
    return out