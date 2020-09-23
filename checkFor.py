import re

def checkFor(data,regex,ignorecase=False):
    out =[]
    if(ignorecase):
        pattern = re.compile(regex, re.IGNORECASE)    
    else:
        pattern = re.compile(regex)
    for line in data:
        m = pattern.search(line)
        if m:
            out = out + [1]
        else:
            out = out + [0]
    return out