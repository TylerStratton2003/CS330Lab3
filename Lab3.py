"""
 Name: Tyler Stratton, Cassie Meboe, Daniel Ma, Kevin Thompson
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2023
 Instructor: Dr. Cao
 Date: 10/12/23
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program

"""
import sys
import argparse
import math

def load_data(arg_f):
    lbls = [];
    with open(arg_f, "r") as file:
        lbls = file.readline().split(",")[:-1];
        entries = [];
        for line in file:
            entries.append(line.split(",")[:-1]);
    tmp_data = {};
    tmp_data["labels"] = lbls;
    tmp_data["entries"] = entries;
    return tmp_data;

def save_data(arg_f, arg_lbl, arg_e):
    txt = "";
    with open(arg_f, "w") as file:
        line = "";
        for lbl in arg_lbl:
            line += lbl + ",";
        line = line[:-1] + "\n";
        txt += line;
        for entry in arg_e:
            line = "";
            for val in entry:
                line += val + ",";
            line = line[:-1] + "\n";
            txt += line;
        file.write(txt);
            

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, 
            ratio is 0.7, so you will split the whole dataset 
            and store the first 7000 of them in trainData, 
            and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, 
            because different group may select different 
            dataset depending on their course project, 
            but generally you should make sure that you 
            code can divide the dataset correctly, 
            since you may use it for the course project
    """
    
    ratio = float(ratio);
    #Load the data, get the labels and entries.
    tmp_data = load_data(data);
    entries = tmp_data["entries"];
    lbls = tmp_data["labels"];
    
    #Get the values for splitting.
    data_count = len(entries);
    train_count = math.floor(data_count * ratio);
    
    #Finally, save the two parts of the data to files.
    save_data(trainData, lbls, entries[:train_count]);
    save_data(testData, lbls, entries[train_count:]);
    

def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    pass;

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    if mode == "N":
      """
      The normal mode
      """
      inputFile = options.input
      outModel1 = options.output1
      outModel2 = options.output2
      ratioNum = options.ratio
      if inputFile == '' or outModel1 == '' or outModel2 == '':
        showHelper()
      splitData(inputFile , outModel1, outModel2, ratioNum)

    if mode == "R":
      """
      The random mode
      """
      inputFile = options.input
      outModel1 = options.output1
      outModel2 = options.output2
      ratioNum = options.ratio
      if inputFile == '' or outModel1 == '' or outModel2 == '':
        showHelper()
      splitDataRandom(inputFile , outModel1, outModel2, ratioNum)
    pass

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    print("Please provide input augument. Here are examples:")
    print("python " + sys.argv[0] + " --mode N --input Github.cvc --output1 trainData.txt --output2 testData.txt --ratio 0.7")
    print("python " + sys.argv[0] + " --mode R --input Github.cvc --output1 trainData.txt --output2 testData.txt --ratio 0.7")

    sys.exit(0)


if __name__ == "__main__":
    '''
    sys.argv.append("--mode");
    sys.argv.append("N");
    sys.argv.append("--input");
    sys.argv.append("DATA/test.csv");
    sys.argv.append("--output1");
    sys.argv.append("trainData.txt");
    sys.argv.append("--output2");
    sys.argv.append("testData.txt");
    sys.argv.append("--ratio");
    sys.argv.append("0.7");
    '''
    
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: R for random splitting, and N for the normal splitting')

    """
    Similar to Lab 2, please update the argument, and add as you need
    """
    parser.add_argument('--input', dest='input',
    default = '',    # default empty!
    help = 'The input file. This is the data to be split')
    parser.add_argument('--output1', dest='output1',
    default = '',    # default empty!
    help = 'The first output file. This is the training data')
    parser.add_argument('--output2', dest='output2',
    default = '',    # default empty!
    help = 'The second output file. This is the testing data')
    parser.add_argument('--ratio', dest='ratio',
    default = 0.7,    # default 0.7!
    help = 'The percentage of the data that is used for training ')
    if len(sys.argv)<3:
        showHelper()
    main()
