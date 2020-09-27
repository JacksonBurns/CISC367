from checkFor import checkFor
from getData import getData

def main(num_conv=None, filename='merged-pythondev-help.xml', verbose=False):
    def retrieve_data():
        # create output files
        outQs = open(r'questions_found.csv','w')
        outQs.write("conv_id,#_questions\n")
        outTxtSpk = open(r'txtspk_found.csv','w')
        outTxtSpk.write("conv_id,#_txt_abbreviations\n")
        # read data in from xml
        data = getData(filename)
        # group data by conversation id
        conversations = {}
        for message in data[4:]:  # ignore starting info
            conv_id = int(message.items()[0][1])  # conversation number
            if(conv_id not in conversations):
                conversations[conv_id] = [message[2].text]
            else:
                conversations[conv_id] = conversations[conv_id] + [message[2].text]
        if num_conv is None:
            num_conv = len(conversations.keys())
        for i in range(1,num_conv+1):
            if(verbose):print("Conversation Number {}:".format(i))
            messages = conversations[i]
            # check for questions
            result = checkFor(messages,r'.*\?.*')
            num_questions = sum(result)
            outQs.write(str(i)+","+str(num_questions)+"\n")
            if(verbose):print("{} question(s)".format(num_questions))
            # check for text speak
            result = [0]*num_conv
            for reg in text_speak:
                temp = checkFor(messages,reg,ignorecase=True)
                result = [sum(x) for x in zip(result, temp)]
            num_text_speak = sum(result)
            outTxtSpk.write(str(i)+","+str(num_text_speak)+"\n")
            if(verbose):print("{} text abbreviation(s)".format(num_text_speak))
            if(verbose):print("End Conversation {}.".format(i))
            if(verbose):print("")
    retrieve_data()

    def compare_to_gold():
        print("")
    

if __name__ == "__main__":
    # this list picks up too many parts of other words
    # text_speak = [r'.*2F4U.*',r'.*4YEO FYEO.*',r'.*AAMOF.*',r'.*ACK.*',r'.*AFAIK.*',r'.*AFAIR.*',r'.*AFK.*',r'.*AKA.*',r'.*B2K.*',r'.*BTT.*',
    #     r'.*BTW.*',r'.*B/C.*',r'.*C&P.*',r'.*CU.*',r'.*CYS.*',r'.*DIY.*',r'.*EOBD.*',r'.*EOD.*',r'.*EOM.*',r'.*EOT.*',r'.*FAQ.*',r'.*FACK.*',
    #     r'.*FKA.*',r'.*FWIW.*',r'.*FYI.*',r'.*FTW.*',r'.*HF.*',r'.*HTH.*',r'.*IDK.*',r'.*IIRC.*',r'.*IMHO.*',r'.*IMO.*',r'.*IMNSHO.*',
    #     r'.*IOW.*',r'.*ITT.*',r'.*LOL.*',r'.*DGMW.*',r'.*MMW.*',r'.*N/A.*',r'.*NaN.*',r'.*NNTR.*',r'.*NOYB.*',r'.*NRN.*'r'.*LOL.*',
    #     r'.*OP.*',r'.*OT.*',r'.*OTOH.*',r'.*PEBKAC.*',r'.*POV.*',r'.*ROTFL.*',r'.*RSVP.*',r'.*RTFM.*',r'.*SCNR.*',r'.*SFLR.*',r'.*SPOC.*',
    #     r'.*TBA.*',r'.*TBC.*',r'.*TIA.*',r'.*TGIF.*',r'.*THX.*',r'.*TQ.*',r'.*TYVM.*',r'.*TYT.*',r'.*TTYL.*',r'.*w00t.*',r'.*WFM.*',r'.*WRT.*',
    #     r'.*WTH.*',r'.*WTF.*',r'.*YMMD.*',r'.*YMMV.*',r'.*YAM.*',r'.*ICYMI.*',r'.*Np.*']
    
    # this list seems to match the gold set better
    text_speak = [r'.*Np.*',r'.*op.*'r'.*tbd.*',r'.*THX.*',r'.*lol.*']
    
    # call main
    main(num_conv=10)
