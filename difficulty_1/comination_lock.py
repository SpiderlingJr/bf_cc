# https://open.kattis.com/problems/combinationlock

deg_per_position = 360 / 40

full_turn = 40

combination = input()

input_sequence = []
while not combination == "0 0 0 0":
    input_sequence.append(combination.split(" "))
    combination = input()
    pass

# starting first second third
# 0           30      0    30

for combo in input_sequence:
    degrees = 0
    start = int(combo[0])
    first = int(combo[1])
    second = int(combo[2])
    third = int(combo[3])

    # first number
    # CLOCKWISE
    degrees +=  2*full_turn

    first_turn = start - first

    if first_turn < 0: # TODO

        first_turn = full_turn + first_turn

    degrees += first_turn


    # second number
    # COUNTER CLOCKWISE
    degrees += full_turn#

    second_turn = second - first

    if second_turn < 0: # TODO

        second_turn = full_turn + second_turn

    degrees += second_turn


    #print("TOTAL:", degrees)

    # third number
    # CLOCKWISE
    third_turn = second - third

    if third_turn < 0: # TODO

        third_turn = full_turn + third_turn

    degrees += third_turn

    print(int(degrees*deg_per_position))
