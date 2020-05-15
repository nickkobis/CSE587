import sys
import string
import os
import re
from collections import deque
N = 3
special = ["science", "sea","fire"]

word_queue = deque()

#breaks string into list of words that is cleaned
def break_string(data):
    data = data.lower()
    data = re.sub(r'[^\w\s]',"",data)
    #words is a list
    words = data.split()
    return words 

#stage 1, fill queue with some data
while len(word_queue) < N:
    try:
        word_queue.extend(break_string(input()))
    except EOFError:
        break

#stage 2, read line, then crunch queue
for data in sys.stdin:
    word_queue.extend(break_string(data))
    
    while len(word_queue) >= N:
        editable_queue = []
        for i in range(N):
            editable_queue.append(word_queue[i])
        #does it have a special word?
        found_one =False
        for i in range(len(editable_queue)):
            word = editable_queue[i]
            for special_word in special:
                if(word == special_word):
                    editable_queue[i] = "$"
                    found_one = True
        if(found_one):
            print("_".join(editable_queue),"\t1")
        word_queue.popleft()

