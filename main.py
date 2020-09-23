from checkFor import checkFor
from getData import getData

def main(num_conv=10, filename='merged-pythondev-help.xml'):
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
    for i in range(1,num_conv+1):
        messages = conversations[i]
        result = checkFor(messages,r'Ok')
        print(result)


if __name__ == "__main__":
    main(num_conv=50)