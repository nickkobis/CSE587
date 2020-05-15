import sys

current_word = None
current_word_count = 0

for line in sys.stdin:
    #assume to be sorted
    key,value = line.split("\t")
    value = int(value)
    
    if key != current_word:
        #send the current word away
        if(current_word!=None):
            print(current_word, "\t",current_word_count)
        current_word = key
        current_word_count = value
    else:
        #keep the current word
        current_word_count = current_word_count + value
#print the last guy out
print(current_word, "\t",current_word_count)
