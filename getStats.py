from getData import getData

def gS(filename,verbose,num_conv):
    # create output file
    outStats = open(r'output_files/out_stats.csv','w')
    # write header
    outStats.write("conv_id,#_messages,#_authors\n")
    # read data in from xml
    data = getData(filename)
    # list of all conversations in the data set
    conversations = range(1,2489)
    # determine how many conversations to to the analysis on.
    if num_conv is None:
        num_conv = len(conversations)
    for i in range(1,num_conv+1):
        # iterate through the requested number of conversations
        authors = {}
        num_messages=0
        for msg in data[4:]:
            # increment number of messages
            num_messages+=1
            # if not the number we want, skip to next message
            if(int(msg.items()[0][1])!=i): continue
            # if we have passed the message, break for efficiency
            if(int(msg.items()[0][1])>i): break
            # author of the message is given in the first index
            auth = msg[1].text
            if(auth not in authors):
                authors[auth] = 1
            else:
                authors[auth] += 1
        # number of authors is given by the number of keys in the authors dict, which are all unique
        num_authors = len(authors.keys())
        # write to output file
        outStats.write("{:d},{:d},{:d}\n".format(i,num_messages,num_authors))
        # optional command line output.
        if(verbose):
            print("Conversation Number {}:".format(i))
            print("{} total message(s)".format(str(num_messages)))
            print("{} total author(s)".format(str(num_authors)))
            print("End Conversation {}.".format(i))
            print("")
