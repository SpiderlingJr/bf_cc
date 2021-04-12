# https://open.kattis.com/problems/qaly

num_inputs = input()

input_tuples = []

for i in range(int(num_inputs)):
    tmp_input = input().split(" ")
    quality, duration = float(tmp_input[0]), float(tmp_input[1])
    input_tuples.append((quality, duration))

#print(input_tuples)

qaly = 0
for quality, duration in input_tuples:
    qaly += quality * duration

print(qaly)