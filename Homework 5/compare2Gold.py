def c2g(verbose,num_conv):
    # compare these results to the gold_set
    def helper(found,gold):
        num_convs = 1; disagree = []
        while(num_convs<len(gold) and num_convs<len(found)): # avoid out of bounds errors
            if(int(gold[num_convs].split(',')[1]) != int(found[num_convs].split(',')[1])):
                if(verbose): print("Disagreement in conv_id {}: gold set had {} algorithm found {}".format(str(num_convs),gold[num_convs].split(',')[1],found[num_convs].split(',')[1]))
                # if the two sets do not agree, append this conv id to disagree list.
                disagree.append(num_convs)
            num_convs+=1
        ### optional command line output of errors
        if(verbose):print("{} chats analyzed; {} chats incorrect; list of incorrect chats: ".format(num_convs,len(disagree)),end='')
        if(len(disagree)==0):
            if(verbose):print("None")
        else:
            for conv in disagree:
                if(disagree[-1]==conv):
                    if(verbose):print(str(conv+1))
                else:    
                    if(verbose):print(str(conv+1)+", ",end='')
        ###

    if(verbose):print("Comparing text speak automated analysis to gold set:")
    with open(r'output_files/txtspk_found.csv','r') as foundfile:
        found = foundfile.readlines()
        with open(r'input_files/txtspk_goldset.csv','r') as goldfile:
            gold = goldfile.readlines()
            helper(found,gold)
            
    if(verbose):print("Comparing # of questions automated analysis to gold set:")
    with open(r'output_files/questions_found.csv','r') as foundfile:
        found = foundfile.readlines()
        with open(r'input_files/questions_goldset.csv','r') as goldfile:
            gold = goldfile.readlines()
            helper(found,gold)