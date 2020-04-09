import sys

for data in sys.stdin:
    data = data.strip()
    #words is a list
    words = data.split() 
    for word in words:
        print(word, "\t1")