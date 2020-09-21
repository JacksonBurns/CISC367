import re

def checkFor(data,regex,name):
    pattern = re.compile(regex)
    for line in data:
        m = pattern.search(line)
        if m:
            return True
    return False