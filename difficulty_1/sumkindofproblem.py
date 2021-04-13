# https://open.kattis.com/problems/sumkindofproblem

num_inputs: int = int(input())

for _ in range(num_inputs):
    k, num = input().split(" ")  # str, str
    num = int(num)
    # num = 10

    # sum of first num integers
    s1 = sum(range(num + 1))

    # sum of first num odd / even integers
    s2 = 0
    s3 = 0
    for i in range(2 * num + 1):
        if i % 2 == 0:
            s3 += i
        elif i % 2 == 1:
            s2 += i

    # n_pos_ints
    #print("s1:", s1)
    #print("s2:", s2)
    #print("s3:", s3)
    print(k, s1, s2, s3)

