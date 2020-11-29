# retrieve the other methods
from funcs import checkFor, openXML, uprint
from test import testMain
import time

def main():
    print("Starting automated message retrieval")
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
        if(checkFor.isQuestion(message[2].text)):
            questions.append(message[0])
        totalMessages += 1
    # dispaly the results
    print("""~~~ RESULTS ~~~\n# Messages: {}\n# w/ Questions: {}\nExecution Time: {:.2f} (s)"""
        .format(totalMessages,len(questions),time.time()-start))

    
    print("Starting comparison to Gold Set")
    

if __name__ == "__main__":
    main()