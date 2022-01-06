# importing libraries
import numpy as np
import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from natsort import natsorted
from nltk.corpus import stopwords
import string

def preprocessing(final_string):
    # Tokenize.
    token_list = nltk.word_tokenize(final_string)
    # Removing stopwords.
    sw = stopwords.words('english')
    need = ['in', 'to', 'where']
    sw = [word for word in sw if word not in need]
    token_list = [word for word in token_list if word not in sw]
    # Change to lowercase.
    token_list = [word.lower() for word in token_list]
    return token_list


# Initialize the file no.
fileno = 0
# Initialize the dictionary.
pos_index = {}
# Initialize the file mapping (fileno -> file name).
file_map = {}

for file in os.listdir("D://الكليه/Level_three/Projects/IR/IR_PRO/"):
    if file.endswith(".txt"):
        with open(file, 'r') as inFiles:
            rFile = inFiles.read()
            final_token_list = preprocessing(rFile)
            for pos, term in enumerate(final_token_list):
                # If term already exists in the positional index dictionary.
                if term in pos_index:
                    # Increment total freq by 1.
                    pos_index[term][0] = pos_index[term][0] + 1
                    # Check if the term has existed in that DocID before.
                    if fileno in pos_index[term][1]:
                        pos_index[term][1][fileno].append(pos)
                    else:
                        pos_index[term][1][fileno] = [pos]
                # If term does not exist in the positional index dictionary
                # (first encounter).
                else:
                    # Initialize the list.
                    pos_index[term] = []
                    # The total frequency is 1.
                    pos_index[term].append(1)
                    # The postings list is initially empty.
                    pos_index[term].append({})
                    # Add doc ID to postings list.
                    pos_index[term][1][fileno] = [pos]

            # Map the file no. to the file name.
            file_map[fileno] = file
            # Increment the file no. counter for document ID mapping
            fileno += 1


# Positional index display.
for query in pos_index:
    sample_pos_idx = pos_index[query]
    print("\nPositional Index:\n")
    print(query + " " + str(sample_pos_idx))
    file_list = sample_pos_idx[1]
    print("\nFilename, [Positions] : \n")
    for fileno, positions in file_list.items():
        print(file_map[fileno], positions)
    print("\n____________________________________\n")

print("Enter your phrase query:")
pQuery = []
pQuery = input().lower()
# pQuery = "antony"
pQuery = preprocessing(pQuery)

for query in pQuery:
    sample_pos_idx = pos_index[query]
    print(query)
    file_list = sample_pos_idx[1]
    print("\nFilenames:")
    for fileno, positions in file_list.items():
        print(file_map[fileno])
    print("\n____________________________________\n")      
