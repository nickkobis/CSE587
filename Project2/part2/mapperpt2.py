import sys
import string
punctuation = string.punctuation
special = ["science", "sea","fire"]
for data in sys.stdin:
    data = data.lower()
    words = data.split()
    avalible = [1,1,1]
    length= len(words)
    for i in range(length):
        if words[i] in special:
            if i+2 < length:
                word = "$" + "_" + words[i+1] + "_" + words[i+2]
                print(word, "\t1")
            if i+1 < length and i-1 >= 0:
                word = words[i-1] + "_" + "$" + "_" + words[i+1]
                print(word, "\t1")
            if i-2 >= 0:
                word = words[i-2] + "_" + words[i-1] + "_" + "$"
                print(word, "\t1")

        