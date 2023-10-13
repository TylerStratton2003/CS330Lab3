"""
 Name: Your Name
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: 20xx
 Instructor: Dr. Cao
 Date: the current date
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program

"""
import sys
import argparse
import math
import random

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    # your code here
    pass

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
    # your code here
    # copy the data into temp
    temp = []
    # These lists will hold lines of data that will be written later
    train, test = [], []
    with open(data, 'r') as file:
            file.readline() # Remove the header
            for line in file:
                    # Make each line of data a separate element
                    temp.append(file.readline()) #
            # Shuffle temp
            random.shuffle(temp)
            # Allocate the data based on the ratio
            
            # Integers to determine how many lines to write
            
            # The train file gets the ratio percent
            trainAllocation = round(ratio * len(temp))
            # The test file gets the remainder
            testAllocation = len(temp) - trainAllocation
            
            # Now write the file for train
            with open(trainData, 'w'):
                for i in range(trainAllocation): # Each allocated line of data
                        train.append(temp.pop()) # is taken from temp
           
            # Now write the data for test
            with open(testData, 'w'):
                for i in range(testAllocation): # Each allocated line of data
                        test.append(temp.pop()) # is taken from temp
            
            # Both files should be written now
    # End of method splitDataRandom

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    # your code here
    pass

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    # your code here

    sys.exit(0)


if __name__ == "__main__":
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
    # your code here
    if len(sys.argv)<3:
        showHelper()
    main()
