# x-axis = n
# y-axis = runtime

from Matcher import matcher
import random

def make_input(n):  # O(n!) (not part of matcher/verifier so that's fine)
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

    for row in proposer_inputs:
        for index, value in enumerate(row):
            output += f"{value}"
            if index != len(row) - 1:
                output += " "
        output += "\n"

    for index_i, row in enumerate(recipient_inputs):
        for index_j, value in enumerate(row):
            output += f"{value}"
            if index_j != len(row) - 1:
                output += " "
        if index_i != len(row) - 1:
            output += "\n"

    return output


if __name__ == '__main__':
    n = 5
    test_input = make_input(n)
    print(test_input)