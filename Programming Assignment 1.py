input = """
3
1 2 3
2 3 1
2 1 3
2 1 3
1 2 3
1 2 3
"""

applicants = []
hospitals = []
count = int(input[1])
split = input[1:].split()

# hospital
for i in range(1, len(split) // 2, count):  # O(n)
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    hospitals.append(temp)
print(hospitals)

# applicant
for i in range(len(split) // 2 + 1, len(split), count):  # O(n)
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    applicants.append(temp)

# while (some hospital is free and hasn't been matched to every applicant) {
    # Choose such a hospital h
    # a = 1st applicant on h's list to whom h has not been matched
    #
    # if (a is free)
    #   assign h to a
    # else if (a prefers h to their current assignment h')
    #   assign a and h, and h' is marked as free
    # else
    #   a rejects h
# }

def matcher(applicants, hospitals):
    pairs = []
    unpaired_h = []
    unpaired_a = []
    for i in range(0, len(hospitals)):
        unpaired_h.append(i + 1)
        unpaired_a.append(i + 1)  # same length and indexes
    print(unpaired_h)

    while (len(unpaired_h) > 0):
        h = unpaired_h[0]
        a = -1
        for pref in hospitals[h]:  # O(1)
            if pref[1] == 1:
                a = pref[0]

        # if (a is unpaired)
            # pairs.append([ h , a ])
            # unpaired_h.pop(0)
            # unpaired_a.remove(a)
        # else:
            # if (a prefers h):
                # find pair for a in pairs
                # set h` in pair as h
                # unpaired_h.append(h)
            # else:
                # continue

    return pairs # [h, a]

def verifier(applicants, hospitals, output):
    checked = [0, 0]  # [matched to one partner no duplicates, stable], ex [1, 1] for both true

    # 6 7 i love code formatting

    return checked

if __name__ == '__main__':
    output = matcher(applicants, hospitals)
    verifier(applicants, hospitals, output)