The program should run on any python 2.7 installation.

run.sh launches src/main.py file, which calls tweets_cleaned.py and average_degree.py with the provided arguments (paths to the input and two output files)

Each tweet is processed line by line and output to both files is written simultaneously.

For average degree we keep track of number of every unique vertex and edge in dictionaries. Therefore removing old tweets edges should on average cost O(1).