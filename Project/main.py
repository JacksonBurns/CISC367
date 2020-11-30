# retrieve the other methods
from funcs import checkFor, openXML, uprint
from test import testMain
import time, csv, json

def main(pullFromJSON=True):
    if(pullFromJSON):
        print("Loading results from JSON")
        results = json.load(open('automated_results.dict'))
    else:
        print("Starting automated message retrieval")
        print("")
        results = getQuestions()

    print("Starting comparison to Gold Set")
    testMain.compareGoldAndCalculated('data/2017 Gold Set - Sheet1.csv', results[0])
    testMain.compareGoldAndCalculated('data/2018 Gold Set - Sheet1.csv', results[1])
    testMain.compareGoldAndCalculated('data/2019 Gold Set - Sheet1.csv', results[2])
    testMain.compareGoldAndCalculated('data/Kaggle Gold Set - Sheet1.csv', results[3])
def getQuestions():
    results = {}
    print("Analyzing Slack data sets")
    for data in ['2017_Slack_Data.xml','2018_Slack_Data.xml','2019_Slack_Data.xml']:
        print("Filename: " + data)
        # start a timer for this analysis
        start = time.time()
        # retrieve the data
        allData = openXML.getData('data/'+data)
        # truncate irrelevant data
        allData = allData[4:]
        # iterate through each message in the data set
        totalMessages = 1
        questions = []
        for message in allData:
            if(checkFor.isQuestion(message[2].text,checkUnpuncuated=True)):
                questions.append(totalMessages)
            totalMessages += 1
        # dispaly the results
        print("""~~~ RESULTS ~~~\n# Messages: {}\n# w/ Unpuncuated Questions: {}\nExecution Time: {:.2f} (s)"""
            .format(totalMessages-1,len(questions),time.time()-start))
        results[data] = questions
    print("")
    print("Analyzing Kaggle data set")
    # reset timer
    start = time.time()
    # retrieve the data
    with open('data/KaggleData.csv','r',errors='ignore') as file:
        reader = csv.reader(file)
        # iterate through each message in the data set
        totalMessages = 1
        questions = []
        for row in reader:
            if(checkFor.isQuestion(row[1],checkUnpuncuated=True)):
                questions.append(totalMessages)
            totalMessages += 1
    # dispaly the results
    print("""~~~ RESULTS ~~~\n# Messages: {}\n# w/ Unpuncuated Questions: {}\nExecution Time: {:.2f} (s)"""
        .format(totalMessages-1,len(questions),time.time()-start))
    results['KaggleData.csv'] = questions

    json.dump(results, open("automated_results.dict",'w'))
    print("")
    return results
    
if __name__ == "__main__":
    main(pullFromJSON=True)