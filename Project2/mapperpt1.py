import sys
import string
punctuation = string.punctuation
for data in sys.stdin:
    data = data.lower()
    list_of_chars = list(data)
    for char in list_of_chars:
        for punc in punctuation:
            if char == punc:
                char = " "
                break
    new_string = ''.join(list_of_chars)
    #words is a list
    words = new_string.split() 
    for word in words:

        print(word, "\t1")