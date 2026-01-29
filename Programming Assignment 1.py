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
print("Hospitals:", hospitals)

# applicant
for i in range(len(split) // 2 + 1, len(split), count):  # O(n)
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    applicants.append(temp)
print("Applicants:", applicants)

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

def matcher(recipients, proposers):
    pairs = []
    unpaired_p = []
    unpaired_r = []
    for i in range(0, len(proposers)):
        unpaired_p.append(i + 1)
        unpaired_r.append(i + 1)  # same length and indexes

    h_choice = 1
    num_proposals = 0
    while len(unpaired_p) > 0:
        if h_choice > len(recipients):
            raise IndexError("h has exhausted possible choices")

        h = unpaired_p[0]
        a = -1
        for pref in proposers[h - 1]:  # O(1)
            if pref[1] == h_choice:
                a = pref[0]
                break
        if a == -1:
            raise ValueError("h has no selected preference")

        num_proposals += 1
        if a in unpaired_r:
            pairs.append([h, a])
            unpaired_p.pop(0)
            unpaired_r.remove(a)
            h_choice = 1
        else:
            current_p = -1
            current_p_pref = -1
            candidate_p_pref = -1
            pair_i = -1

            for i in range(len(pairs)):
                if pairs[i][1] == a:
                    current_p = pairs[i][0]
                    pair_i = i
                    break
            for pref in recipients[a - 1]:
                if pref[0] == h:
                    candidate_p_pref = pref[1]
                if pref[0] == current_p:
                    current_p_pref = pref[1]
                if candidate_p_pref != -1 and current_p_pref != -1:
                    break

            if candidate_p_pref < current_p_pref:
                pairs[pair_i][0] = h
                unpaired_p.append(current_p)
                h_choice = 1
            else:
                h_choice += 1
                continue  # reject
    print("Number of Proposals:", num_proposals)
    return pairs # [h, a]

def verifier(applicants, hospitals, output):
    checked = [0, 0]  # [matched to one partner no duplicates, stable], ex [1, 1] for both true

    # 6 7 i love code formatting

    return checked

if __name__ == '__main__':
    matchings = matcher(recipients = applicants, proposers = hospitals)
    for match in matchings:
        print(match[0], match[1])
    # 1 2
    # 2 3
    # 3 1
    # [[1, 2], [2, 3], [3, 1]]

    verifier(applicants, hospitals, matchings)