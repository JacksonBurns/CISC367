import re, nltk

def isQuestion(message):
    """
    Given a string, this function will return True if it contains a questions and false otherwise
    There are two likely cases where a string would contain a question:
        - there is a question mark
        - they use interrogative grammar
            - invert subject and first verb in verb phrase
            - start with interrogative pronoun
    If all of these are true, it is almost definetely a question.
    If two are true, then it is probably a question.
    Otherwise, it is not.

    """
    # check first if the message has a question mark
    hasQM = False
    hasQM = regexSearch(message,r".*?(\?).*?")
    # use syntax tree to check for interrogative diction
    interG1 = False
    interG2 = False
    # starts with an interrogative pronoun
    words = nltk.word_tokenize(message)
    if(words[0] in ["who","whom","whose","what","when","where","why","which","how"]):
        interG1 = True
    # check for inversion of subject and verb in verb phrase
    pos = nltk.pos_tag(words)
    parts = [i[1] for i in pos]
    if('NN' in parts and 'PRP' in parts):
        interG2 = True
    return True if sum([hasQM, interG1, interG2]) > 1 else False


    

def regexSearch(data,regex,ignorecase=False):
    """
    Returns True if the regular expression is found in the data and False otherwise
    """
    if(ignorecase):
        pattern = re.compile(regex, re.IGNORECASE)    
    else:
        pattern = re.compile(regex)
    # match object will be of None type if no match is found
    return True if pattern.search(data) else False