import nltk

tes = nltk.word_tokenize("Can someone explain this code to me?")
print(tes)
out = nltk.pos_tag(tes)
print(out)