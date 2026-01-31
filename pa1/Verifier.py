with open("input.txt", "r") as file:
    input = file.read()

applicants = []
hospitals = []
count = int(input[1])
split = input[1:].split()

# hospital input parsing
for i in range(1, len(split) // 2, count):  # O(n)
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    hospitals.append(temp)


# applicant input parsing
for i in range(len(split) // 2 + 1, len(split), count):  # O(n)
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    applicants.append(temp)

#converts the cursed arrays of pairs into lists of dictionaries to make interating easier
#using maps instead because the input parsing was making me wanna kms (okay I guess its a dictionary, sue me)
h_prefs = []
a_prefs = []
n = len(hospitals)
for lines in range(n):
    h_pref = {}
    h_prefs.append(h_pref)
for h in range(n):
    for a, pref in hospitals[h]:
        h_prefs[h][a] = pref

for lines in range(n):
    a_pref = {}
    a_prefs.append(a_pref)
for a in range(n):
    for h, pref in applicants[a]:
        a_prefs[a][h] = pref

h_match = {}
a_match = {}
match_verifier = 0

with open("output.txt", "r") as f:
    for line in f:
        h, a = map(int, line.split())
        h_match[h] = a
        a_match[a] = h
        match_verifier += 1

duplicate_verifier_set_h = set(h_match.values())
duplicate_verifier_set_a = set(a_match.values())

def verifier(h_pref_raw, a_pref_raw, h_match, a_match):
    n = len(h_pref_raw)
    #h_pref_raw = list of raw hospital preference
    #a_pref_raw = list of raw applicant preferences
    #h_match = list of all hospitals and their corresponding a matches
    #a_match = list of all applicants and their corresponding h matches

    #DUPLICATE or MISSING PAIR CHECKER
    if (len(h_match) != n) or (len(a_match) != n):
        print("INVALID")
        print("missing pair")
        return False

    if (len(duplicate_verifier_set_h) != match_verifier) or (len(duplicate_verifier_set_a) != match_verifier):
        print("INVALID")
        print("duplicate pairing")
        return False

    print("VALID", end='')

    #STABILITY CHECKER
    #note we have to be careful with the indexing because we're swapping between indexing lists and dictionaries
    #a blocking pair is when we have an a and an h whomst both prefer each other over their current match

    #for all hospitals indexed from 1->n
    for h_curr in range(1, n+1):
        #store the current a matched to the current h
        matched_a_to_h_curr = h_match[h_curr]
        #for all applicants in a given hospitals preference list
        for a_curr in h_pref_raw[h_curr-1]:
            #if there exists an applicant which the current hospital prefers more than its current applicant
            if h_pref_raw[h_curr-1][a_curr] < h_pref_raw[h_curr-1][matched_a_to_h_curr]:
                #flag hospital with the eclipsing preference
                flagged_h = a_match[a_curr]
                #does the corresponding flagged hospital's greater-preference-applicant prefer the flagged hospital over its current matching?
                if a_pref_raw[a_curr - 1][h_curr] < a_pref_raw[a_curr - 1][flagged_h]:
                    print(" UNSTABLE")
                    # print("current h: ", h_curr)
                    # print("its corresponding a: ", h_match[h_curr])
                    # print("higher preference a: ", a_curr)
                    # print("flagged h: ", flagged_h)
                    print("h:", h_curr, " prefers a:", a_curr, " over a:", h_match[h_curr], sep='')
                    print("a:", a_curr, " prefers h:", h_curr, " over h:", a_match[a_curr], sep='')
                    return False
    print(" STABLE")
    return True


if __name__ == '__main__':
    verifier(h_prefs, a_prefs, h_match, a_match)

