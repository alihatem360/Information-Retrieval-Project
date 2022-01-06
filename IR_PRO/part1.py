import nltk
import os
import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# for i in range(2):
#     text=input("Enter the file name: ")
#     fileName.append(text)

# Open a file
path = "D://الكليه/Level_three/Projects/IR/IR_PRO/"
fileName = os.listdir(path)
print(fileName)
print("\n____________________________________\n")
print("\nRead 10 files\n")
for key in fileName:
    if key.endswith(".txt"):
        with open(key, 'r') as inFiles:
            rFile = inFiles.read()
            print(rFile)
print("\n____________________________________\n")

print("\nApply tokenization\n")

for took in fileName:
    if took.endswith(".txt"):
        with open(took,'r') as openFile:
            readFile = openFile.read()
            print(word_tokenize(readFile))
print("\n____________________________________\n")

print("\nApply Stop words \n")

englishStop = stopwords.words('english')
for stopT in fileName:
    if stopT.endswith(".txt"):
        openFile = open(str(stopT), "r")
        readFile = openFile.read()
        words = word_tokenize(readFile)
        print([word for word in words if word not in englishStop])
print("\n_________________________________\n")