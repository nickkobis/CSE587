import sys

top10_array =[]
for line in sys.stdin:
    #assume 000000000000xxx(tab)hello_$_world
    key,value = line.split("\t")
    key = int(key)
    if len(top10_array)<10:
        top10_array.append((key,value))
    else:
        for i in range(10):
            minimum = 999999999999999
            min_index =-1
            if(minimum>top10_array[i][0]):
                minimum = top10_array[i][0]
                min_index = i
            if(key>minimum):
                top10_array[min_index]=(key,value)


for number in range(10):
    maximum =0
    max_index =-1
    for i in len(top10_array):
        if top10_array[i][0] > maximum:
            maximum = top10_array[i][0]
            max_index = i
    print(top10_array[max_index][1],'\t',top10_array[max_index][0])
    top10_array.pop(max_index)