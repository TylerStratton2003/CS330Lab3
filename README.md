# CS330Lab3
# Cassie Meboe, Tyler Stratton, Daniel Ma, Kevin Thompson

Our dataset is GitHubContents. We found it on Google Open dataset. 

This dataset is unique file contents of text files under 1 MiB on the HEAD branch. It has 501 lines of data.

The input for our dataset is the contents of these text files.

The output for our dataset is id (string), size (integer), content (string), binary (boolean), and copies (integer).

Id is the id of the text files. Size is the size of the text files. Content is the content of the text files. Binary is whether or not the file is in binary. Copies is how many copies there are of a text file.

The data being split is the dataset mentioned above, which contains info on commits to GitHub, called contents.csv.

The input to Lab3.py is the dataset mentioned, as well as the ratio of trainData to testData the user wants.

There are two outputs in Lab3.py: the Training Data and the Testing Data.

To run the file: type "python3 Lab3.py" and then follow the instructions provided.

