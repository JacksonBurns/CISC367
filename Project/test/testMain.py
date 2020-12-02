from sklearn.metrics import cohen_kappa_score, f1_score
import sys, csv
# retrieve gold set 
def compareGoldAndCalculated(goldSetFile, calculatedChatids:dict):
    '''
    goldSetFile: file destination of gold set 
    calculatedChatids: dictionary of chat IDs with un-punctuated questions in them
    '''
    with open(goldSetFile, newline='') as file:
        csvreader = csv.reader(file, delimiter=',')
        gold_set = []
        chat_ids = []
        count = 0
        # iterate through each entry in the gold set to create list of un-punctuated questions per chat id
        # 1 indicates un-punctuated questions while 0 represents no un-punctuated questions 
        # also creates list of chat ids in the gold set 
        next(csvreader)
        for row in csvreader:
            if int(row[1]) > 0: 
                gold_set.append(1)
            else: 
                gold_set.append(0)
            chat_ids.append(row[0])
    calculated_set = []
    # iterate through each chat id in gold set and check if it is in parameter list of chat ids with un-punctuated questions 
    # 1 indicates un-punctuated questions while 0 represents no un-punctuated questions  
    for chat in chat_ids: 
        if (int(chat) in calculatedChatids): 
            calculated_set.append(1)
        else: 
            calculated_set.append(0)
    #calculated Cohen Kappa and F-score
    score = cohen_kappa_score(gold_set, calculated_set) 
    fscore = f1_score(gold_set, calculated_set)
    print("Analysis of " + goldSetFile)
    print("Cohen Kappa: ") 
    print(score)
    print("F score: ")
    print(fscore)
    score_list = [score, fscore]
    return score_list
