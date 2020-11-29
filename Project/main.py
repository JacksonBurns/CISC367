# retrieve the other methods
from funcs import checkFor, openXML, uprint
from test import testMain
import time, csv

def main():
    print("Starting automated message retrieval")
    print("Analyzing Slack data set")
    # start a timer for this analysis
    start = time.time()
    # retrieve the data
    allData = openXML.getData("data/merged-pythondev-help.xml")
    # truncate irrelevant data
    allData = allData[4:]
    # iterate through each message in the data set
    totalMessages = 0
    questions = []
    for message in allData:
        if(checkFor.isQuestion(message[2].text,checkUnpuncuated=True)):
            questions.append(totalMessages)
        totalMessages += 1
    # dispaly the results
    print("""~~~ RESULTS ~~~\n# Messages: {}\n# w/ Unpuncuated Questions: {}\nExecution Time: {:.2f} (s)"""
        .format(totalMessages,len(questions),time.time()-start))
    print("Analyzing Kaggle data set")
    # reset timer
    start = time.time()
    # retrieve the data
    with open('data/KaggleData.csv','r',errors='ignore') as file:
        reader = csv.reader(file)
        # iterate through each message in the data set
        totalMessages = 0
        questions = []
        for row in reader:
            if(checkFor.isQuestion(row[1],checkUnpuncuated=True)):
                questions.append(totalMessages)
            totalMessages += 1
    # dispaly the results
    print("""~~~ RESULTS ~~~\n# Messages: {}\n# w/ Unpuncuated Questions: {}\nExecution Time: {:.2f} (s)"""
        .format(totalMessages,len(questions),time.time()-start))

    
    print("Starting comparison to Gold Set")
    

if __name__ == "__main__":
    main()