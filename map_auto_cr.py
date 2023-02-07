#Diamond-Square-Algorithm
#takes 20min

import sys


sqr_point = 4
def dia_sqr_algo(number):
    line = 2
    if number <= 0:
        return 2**2
    for i in range(number):
        #print(f'i is {i}')
        line = line + 2**i
        #print(f'internal line is {line}')
    return line**2



step_n = int(sys.stdin.readline())
print(dia_sqr_algo(step_n))

