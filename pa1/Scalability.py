# x-axis = n
# y-axis = runtime

import random

def make_input(n):
    output = f"{n}\n"

    proposals = []
    recipients = []
    for i in range(n):
        row = [j for j in range(1, n + 1)]
        random.shuffle(row)
        print(row)

    return output


make_input(3)