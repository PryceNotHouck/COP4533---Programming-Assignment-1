with open("input.txt", "r") as file:
    input = file.read()

flag = 0
if input == "":
    print("please input a valid (non-empty) set of data")
    flag = 1

def format_preferences(input_text):
    applicants = []
    hospitals = []
    count_index = input_text[1:].find('\n')
    count = int(input_text[1: count_index + 1])
    split = input_text[count_index + 1:].split()

    # hospital
    for i in range(1, len(split) // 2, count):  # O(n)
        row = split[i: i + count]
        temp = []
        for j in range(0, len(row)):
            temp.append((int(row[j]), j + 1))
        hospitals.append(temp)
    #print("Hospitals:", hospitals)

    # applicant
    for i in range(len(split) // 2 + 1, len(split), count):  # O(n)
        row = split[i: i + count]
        temp = []
        for j in range(0, len(row)):
            temp.append((int(row[j]), j + 1))
        applicants.append(temp)
    #print("Applicants:", applicants)
    return applicants, hospitals

if(flag == 0):
    applicants, hospitals = format_preferences(input)

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

    p_choice = 1
    num_proposals = 0
    while len(unpaired_p) > 0:
        if p_choice > len(recipients):
            raise IndexError("proposer has exhausted possible choices")

        p = unpaired_p[0]
        r = -1
        for pref in proposers[p - 1]:  # O(1)
            if pref[1] == p_choice:
                r = pref[0]
                break
        if r == -1:
            raise ValueError("proposer has no selected preference")

        num_proposals += 1
        if r in unpaired_r:
            pairs.append([p, r])
            unpaired_p.pop(0)
            unpaired_r.remove(r)
            p_choice = 1
        else:
            current_p = -1
            current_p_pref = -1
            candidate_p_pref = -1
            pair_i = -1

            for i in range(len(pairs)):
                if pairs[i][1] == r:
                    current_p = pairs[i][0]
                    pair_i = i
                    break
            for pref in recipients[r - 1]:
                if pref[0] == p:
                    candidate_p_pref = pref[1]
                if pref[0] == current_p:
                    current_p_pref = pref[1]
                if candidate_p_pref != -1 and current_p_pref != -1:
                    break

            if candidate_p_pref < current_p_pref:
                pairs[pair_i][0] = p
                unpaired_p.remove(p)
                unpaired_p.append(current_p)
                p_choice = 1
            else:
                p_choice += 1
                continue  # reject
    #print("Number of Proposals:", num_proposals)
    return pairs # [h, a]

if __name__ == '__main__':
    if(flag == 0):
        matchings = matcher(recipients = applicants, proposers = hospitals)
        with open("output.txt", "w") as writefile:
            for match in matchings:
                print(match[0], match[1])
                writefile.write(f"{match[0]} {match[1]}\n")