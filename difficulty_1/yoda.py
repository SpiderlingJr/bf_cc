# https://open.kattis.com/problems/yoda

num_1 = input()
num_2 = input()

l1 = len(num_1)
l2 = len(num_2)

num_1 = list(num_1)
num_1.reverse()

num_2 = list(num_2)
num_2.reverse()

if l1 < l2:
    pads = l2 - l1
    for _ in range(pads):
        num_1.append('0')
elif l2 < l1:
    pads = l1-l2
    for _ in range(pads):
        num_2.append('0')

out_1 = []
out_2 = []

for n1, n2 in zip(num_1, num_2):
    n1 = int(n1)
    n2 = int(n2)

    if n1 < n2:
        out_2.append(str(n2))
    elif n2 < n1:
        out_1.append(str(n1))
    else:
        out_1.append(str(n1))
        out_2.append(str(n2))

out_1.reverse()
out_2.reverse()


if not out_1:
    out_1 = "YODA"
else:
    out_1 = int("".join(out_1))
if not out_2:
    out_2 = "YODA"
else:
    out_2 = int("".join(out_2))

print(out_1)
print(out_2)