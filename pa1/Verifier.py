# input = """
# 3
# 1 2 3
# 2 3 1
# 2 1 3
# 2 1 3
# 1 2 3
# 1 2 3
# """
# m_i = """"
# 1 1
# 2 2
# 3 3
# """

input = """
5
1 2 3 4 5
5 1 3 2 4
3 4 5 1 2
1 4 3 2 5
1 3 2 5 4
1 2 3 4 5
5 1 3 2 4
3 4 5 1 2
1 4 3 2 5
1 3 2 5 4
"""

m_i = """
1 1
2 5
3 3
4 4
5 2
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
print("h_i")
for i in range(0, len(hospitals)):
    print(hospitals[i])


# applicant input parsing
for i in range(len(split) // 2 + 1, len(split), count):  # O(n)
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    applicants.append(temp)
print("a_i")
for i in range(0, len(applicants)):
    print(applicants[i])

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

# for line in m_i:
#     h_m, a_m = map(int, line.split('\n'))
#     print(h_m)

# iterate through h_i[h_m], the preference list of the given hospital
# this yields a list of ordered pref.
# iterate through this list until you find a_m (the matched applicant)
# if any of these pref. > than the pref. listed for a_m, must check other end for blocked pair
# checking for blocked pair is done in a_i[h] > a_m, which is to say, if there is an
# if a_i[e]


#h_i is hospital input (unmatched)
#a_i is applicant input (unmatched)
#m_i is matched input (post-matching from Matcher.py)

def verifier(h_i, a_i, m_i):
    # with open("output.txt", "r") as matched_file:
    #     m_p = []
    #     for line in matched_file:
    #         line = line.strip()
    #         h_mt, a_mt = map(int, line.split())
    #         print(h_mt, a_mt)
    #         m_p.append((h_mt, a_mt))

    #     for pair in m_p:
    #         h_m = pair[0]
    #         a_m = pair[1]
    #
    #         #for the given applicant in order of the current hospitals preference
    #         for a in h_i[h_m-1]:
    #             #if the given applicant in the ordered preference list != the matching applicant,
    #             # must check its corresponding preference
    #             if h_i[h_m-1][a] != a_m:
    #                 #for the given hospital in order of the current applicants preference
    #                 for h in a_i[a_m-1]:
    #                     #if the given hospital != the matching hospital, check the corresponding preference
    #                     if a_i[a_m-1][h] != h_m:
    #                         #this line needs to be changed
    #                         #needs to be, if the applicants preference for H > H' (where H' is its current matching)
    #                         #then it is a blocking pair, so we need to know every applicants current matching
    #                         corr_pref = 0
    #                         for temp_pair in m_p:
    #                             h_m_t = temp_pair[0]
    #                             a_m_t = temp_pair[1]
    #                             if a_m_t == a_i[a_m-1][h]:
    #                                 corr_pref = h_m_t
    #                         if a_i[corr_pref][h] > a_m:
    #                             print("blocking pair detected")
    #                             return True
    #                     if h_i[h_m-1][a] == a_m:
    #                         break
    #             if a_i[a_m-1][h] == h_m:
    #                 break
    # print("verified stable")
    # return False
    with open("output.txt", "r") as matched_file:
        m_p = []
        for line in matched_file:
            line = line.strip()
            h_mt, a_mt = map(int, line.split())
            print(h_mt, a_mt)
            m_p.append((h_mt, a_mt))
        for pair in m_p:
            h_m = pair[0]
            a_m = pair[1]
            for a in h_i[h_m-1]:
                print(a)
                print(h_i[h_m-1])
                print(h_i[h_m-1][a])
                if h_i[h_m-1][a] != a_m:
                    for h in a_i[a_m-1]:
                        if a_i[a_m-1][h] != h_m:
                            corr_pref = 0
                            for temp_pair in m_p:
                                h_m_t = temp_pair[0]
                                a_m_t = temp_pair[1]
                                if a_m_t == a_i[a_m-1][h]:
                                    corr_pref = h_m_t
                            if a_i[corr_pref][h] > a_m:
                                print("blocking pair detected")
                                return True
                        if h_i[h_m-1][a] == a_m:
                            break
                if a_i[a_m-1][h] == h_m:
                    break
    print("verified stable")
    return False

verifier(hospitals, applicants, m_i)


