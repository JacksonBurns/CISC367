import retrieveParameters
import compare2Gold
import getStats

def main(num_conv=None, filename='input_files/merged-pythondev-help.xml', verbose=False):
    # call external scripts
    retrieveParameters.rP(filename,verbose,num_conv)
    compare2Gold.c2g(verbose,num_conv)
    getStats.gS(filename,verbose,num_conv)
    # compile all this data into a single sheet
    with open(r'output_files/out_stats.csv','r') as file:
        stats = file.readlines()
    with open(r'output_files/questions_found.csv','r') as file:
        questions = file.readlines()
    with open(r'output_files/txtspk_found.csv','r') as file:
        txtspeak = file.readlines()
    with open(r'output_files/data_summary.csv','w') as file:
        file.write("conv_id,#_questions,#_txt_spk,#_messages,#_authors\n")
        for i in range(1,len(stats)):
            file.write("{:d},{:d},{:d},{:d},{:d}\n".format(
                int(stats[i].split(',')[0]),
                int(questions[i].split(',')[1]),
                int(txtspeak[i].split(',')[1]),
                int(stats[i].split(',')[1]),
                int(stats[i].split(',')[2])
            ))
    
if __name__ == "__main__":
    # call main
    # max number of conversations for keyword argument is 2488
    main(num_conv=2488,verbose=False)
