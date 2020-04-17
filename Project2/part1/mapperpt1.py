import sys
import string
import os
import re
punctuation = string.punctuation
for data in sys.stdin:
    data = data.lower()
    data = re.sub(r'[^\w\s]',"",data)
    #words is a list
    words = data.split() 
    for word in words:

        print(word, "\t1")