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
    row = sgplit[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((int(row[j]), j + 1))
    applicants.append(temp)
print(applicants)

#oi is original input, mi is matched input
def verifier(oi, mi):
    #parse oi
    #while H preference != oi P_S:
        #find S matching P_S
        #if S matching P < H_P
    pass