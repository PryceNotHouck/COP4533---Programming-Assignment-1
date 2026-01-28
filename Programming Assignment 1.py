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
for i in range(1, len(split) // 2, count):
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((row[j], j + 1))
    hospitals.append(temp)

# applicant
for i in range(len(split) // 2 + 1, len(split), count):
    row = split[i: i + count]
    temp = []
    for j in range(0, len(row)):
        temp.append((row[j], j + 1))
    applicants.append(temp)