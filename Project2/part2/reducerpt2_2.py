import sys

for data in sys.stdin:
    split_data = data.split()
    print(split_data[0],"\t","Has ", len(split_data)-1," entries" )