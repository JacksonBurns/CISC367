import re

def checkFor(data,regex,ignorecase=False):
    """
    returns a list of 1 and 0 for whether or not the regex was found in each index of a list
    allows the option ignorecase to be added
    """
    out =[]
    if(ignorecase):
        pattern = re.compile(regex, re.IGNORECASE)    
    else:
        pattern = re.compile(regex)
    for line in data:
        # match object will be of None type if no match is found
        m = pattern.search(line)
        if m:
            out = out + [1]
        else:
            out = out + [0]
    return out