import sys


for val in sys.stdin:
    split_val = val.split('\t')
    str_num = format(int(split_val[1]),'016d')
    print(str_num,'\t',split_val[0].strip())