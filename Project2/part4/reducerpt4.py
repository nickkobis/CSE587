import sys
keys = []
values = []

# current_word = None
# current_word_count = 0
store = {}
for line in sys.stdin:
    #assume to be sorted
    # key,value = line.split("\t")
    
    entrys = (line.rstrip()).split("\t")
    key = entrys[0]
    value = entrys[1:]
    # print(type(value))
    # print(value)
    
    if key in store:
        # join 1 got stored first
        if len(value)>1:
            store[key].extend(value)
        # join 2 got stored firest
        else:
            value.extend(store[key])
            store[key] = value            
    else:
        store[key] = value

for key, value in store.items():
    if len(value) == 4:
        print(key + "\t"+ value[0]+"\t"+ value[1]+"\t"+ value[2]+"\t"+ value[3])
#     if key != current_word:
#         #send the current word away
#         # if(current_word!=None):
#         #     print(current_word, "\t",current_word_count)
#         keys.append(current_word)
#         values.append(current_word_count)
#         current_word = key
#         current_word_count = value

#     else:
#         #keep the current word
#         current_word_count = current_word_count + value
# #print the last guy out
# valkey = list(zip(values,keys))
# valkey.sort(reverse = True)



# for i in range(10):
#     print(valkey[i][1], "\t",valkey[i][0])

