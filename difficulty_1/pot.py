# https://open.kattis.com/problems/pot
import math

num_inputs: int = int(input())

input_sequence = []
summe = 0

for _ in range(num_inputs):
    curr_input = input()
    # a = "212" [2,1,2]
    exp: int = int(curr_input[-1])
    num: int = int(curr_input[0:-1])
    summe += num ** exp  # close enough

print(summe)
# C: for (i=0; i < num_inputs; i++) { continue }

# python: for i in range(num_inputs):
#    pass
