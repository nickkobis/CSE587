import sys

for data in sys.stdin:
    #words is a list
    words = data.split() 
    for word in words:
        print(word, "1")