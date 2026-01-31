import copy
import Matcher
from matplotlib import pyplot as plt
import time
import numpy as np
import random

def make_input(n):  # O(n!) (not part of matcher/verifier so that's fine)
    output = f"\n{n}\n"

    proposer_inputs = []
    recipient_inputs = []
    for i in range(n):
        row = [j for j in range(1, n + 1)]
        while row in proposer_inputs:
            random.seed(time.time())
            random.shuffle(row)
        proposer_inputs.append(copy.deepcopy(row))

        random.seed(time.time())
        random.shuffle(row)
        while row in recipient_inputs:
            random.seed(time.time())
            random.shuffle(row)
        recipient_inputs.append(copy.deepcopy(row))

    for row in proposer_inputs:
        for index, value_p in enumerate(row):
            output += f"{value_p}"
            if index != len(row) - 1:
                output += " "
        output += "\n"

    for index_i, row in enumerate(recipient_inputs):
        for index_j, value_r in enumerate(row):
            output += f"{value_r}"
            if index_j != len(row) - 1:
                output += " "
        if index_i != len(row) - 1:
            output += "\n"

    return output


if __name__ == '__main__':
    # sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    times = []
    for n in sizes:
        input_text = make_input(n)
        start = time.perf_counter()
        ###########################
        recipients, proposers = Matcher.format_preferences(input_text)
        temp = Matcher.matcher(recipients = recipients, proposers = proposers)
        ###########################
        end = time.perf_counter()
        times.append(end - start)

    plt.scatter(sizes, times, color = 'red')

    sizes = np.array(sizes)
    times = np.array(times)
    z = np.polyfit(x = sizes, y = times, deg = len(sizes))
    p = np.poly1d(z)
    plt.plot(sizes, p(sizes))

    plt.title('Gale-Shapely Matcher Scalability')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Runtime (s)")
    plt.legend()

    plt.show()