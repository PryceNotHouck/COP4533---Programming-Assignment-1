# x-axis = n
# y-axis = runtime

#from Matcher import matcher
import random

def make_input(n):
    output = f"{n}\n"

    proposer_inputs = []
    recipient_inputs = []
    for i in range(n):
        row = [j for j in range(1, n + 1)]
        while row in proposer_inputs:
            random.shuffle(row)
        proposer_inputs.append(row)

        while row in recipient_inputs:
            random.shuffle(row)
        recipient_inputs.append(row)

    return output


if __name__ == '__main__':
    n = 3
    input = make_input(n)