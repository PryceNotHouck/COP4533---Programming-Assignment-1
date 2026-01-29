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

# hospital input parsing
for i in range(1, len(split) // 2, count):  # O(n)
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    hospitals.append(temp)
print(hospitals)

# applicant input parsing
for i in range(len(split) // 2 + 1, len(split), count):  # O(n)
    row = sgplit[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    applicants.append(temp)
print(applicants)

#h_i is hospital input (unmatched)
#a_i is applicant input (unmatched)
#m_i is matched input (post-matching from Matcher.py)
def verifier(h_i, a_i, m_i):

    #For each matching in m_i:
        #check every one of H's preferences for every A in its pref_list up until H's matched A
        #if one of these As has a preference for H > than its matched H', we have a blocking pair

        #For all N matchings in m_i
            #for some A in H's preference list:
                #if A != H's matched A:
                    #check A's H' (A's match)
                    #if A's preference for H > H':
                        #blocking pair = true
                        #return true
                    #else:
                        #continue
                #else:
                    #continue
    #return false
    pass