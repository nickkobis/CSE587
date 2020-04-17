import sys

for val in sys.stdin:
    split_val = val.split('\t')
    print(split_val[1],"\t",split_val[0])