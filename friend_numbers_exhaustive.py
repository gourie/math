from itertools import combinations
import numpy as np
import time

def friend_numbers_exhaustive_count(count_till_number):
    friend_numbers_cnt = 0
    for pair in combinations(np.arange(1,count_till_number),2):
        str_1 = str(pair[0])
        str_2 = str(pair[1])
        # print(str_1, str_2)
        if np.any([digit in str_2 for digit in str_1]):
            friend_numbers_cnt +=1
    return friend_numbers_cnt

N=1000
start = time.time()
result = friend_numbers_exhaustive_count(N)
end = time.time()

print("Counting friend numbers exhaustively till %s yields %s, took %0.5f seconds" %(N,result, end-start))