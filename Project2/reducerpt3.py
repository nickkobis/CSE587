import sys

current_word = None
current_locations = None

for line in sys.stdin:
    #assume to be sorted
    key,value = line.split("\t")
    key = key.strip()
    value = value.strip()
    
    if key != current_word:
        #send the current word away
        if(current_word!=None):
            print(current_word, "\t",current_locations)
        current_word = key
        current_locations = value
    elif not(value in current_locations):
        #keep the current word
	
        current_locations = current_locations + ", " + value
#print the last guy out
print(current_word, "\t",current_locations)

