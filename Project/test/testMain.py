from sklearn.metrics import cohen_kappa_score, f1_score
import sys, csv
# retrieve gold set 
def compareGoldAndCalculated(goldSetFile, calculatedChatids:dict):
    '''
    goldSetFile: file destination of gold set 
    calculatedChatids: dictionary of chat IDs with undetected questions in them
    '''
    with open(goldSetFile, newline='') as file:
        csvreader = csv.reader(file, delimiter=',')
         # iterate through each entry in the gold set
        gold_set = []
        chat_ids = []
        count = 0
        next(csvreader)
        for row in csvreader:
            if int(row[1]) > 0: 
                gold_set.append(1)
            else: 
                gold_set.append(0)
            chat_ids.append(row[0])
    calculated_set = []
    for chat in chat_ids: 
        if (int(chat) in calculatedChatids): 
            calculated_set.append(1)
        else: 
            calculated_set.append(0)
    score = cohen_kappa_score(gold_set, calculated_set) 
    fscore = f1_score(gold_set, calculated_set)
    print("Analysis of " + goldSetFile)
    print("Cohen Kappa: ") 
    print(score)
    print("F score: ")
    print(fscore)
    return score 

print(compareGoldAndCalculated("/Users/kristinaholsapple/Documents/CISC/367 Intro to CS Research/final/CISC367/Project/data/2017 Gold Set - Sheet1.csv", [950, 953, 976, 995, 996]))