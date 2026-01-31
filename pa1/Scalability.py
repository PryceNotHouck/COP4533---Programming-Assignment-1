import copy
import Matcher
import Verifier
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
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    matcher_times = []
    verifier_times = []

    for n in sizes:
        input_text = make_input(n)

        #sections are titled using hashes, my coding parter says it looks like AI but I think it looks epic
        ############################
        # Run Matcher
        ############################
        start = time.perf_counter()
        recipients, proposers = Matcher.format_preferences(input_text)
        temp = Matcher.matcher(recipients=recipients, proposers=proposers)

        end = time.perf_counter()
        matcher_times.append(end - start)

        ############################
        # Verifier Formatting
        ############################

        # Map the matches in order to push into our Verifier function
        h_match = {match[0]: match[1] for match in temp}
        a_match = {match[1]: match[0] for match in temp}

        # Grab preferences
        h_prefs, a_prefs = Matcher.format_preferences(input_text)

        # convert the preference list to a list of dictionaries
        h_prefs_dict_list = []
        for prefs in h_prefs:
            d = {}
            for pref, a in prefs:
                d[a] = pref
            h_prefs_dict_list.append(d)

        a_prefs_dict_list = []
        for prefs in a_prefs:
            d = {}
            for pref, h in prefs:
                d[h] = pref
            a_prefs_dict_list.append(d)

        ############################
        # Run Verifier
        ############################
        start = time.perf_counter()
        Verifier.verifier(h_prefs_dict_list, a_prefs_dict_list, h_match, a_match)
        end = time.perf_counter()
        verifier_times.append(end - start)

    ############################
    # Graph Matcher
    ############################
    plt.scatter(sizes, matcher_times, color='red', label='Matcher Runtime')
    z = np.polyfit(x=sizes, y=matcher_times, deg=len(sizes))
    p = np.poly1d(z)
    plt.plot(sizes, p(sizes), color='red')
    plt.title('Gale-Shapley Matcher Scalability')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Runtime (s)")
    plt.legend()
    plt.grid(True)
    plt.show()

    ############################
    # Graph Verifier
    ############################
    plt.scatter(sizes, verifier_times, color='blue', label='Verifier Runtime')
    z_v = np.polyfit(x=sizes, y=verifier_times, deg=len(sizes))
    p_v = np.poly1d(z_v)
    plt.plot(sizes, p_v(sizes), color='blue')
    plt.title('Gale-Shapley Verifier Scalability')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Runtime (s)")
    plt.legend()
    plt.grid(True)
    plt.show()
