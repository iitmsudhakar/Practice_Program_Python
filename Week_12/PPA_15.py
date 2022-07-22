def mentors(scores, subject):
    L = []
    for S in scores:
        print(S)
        L.append((S['SeqNo'], S[subject]))
    print(L)
    D = dict()
    for i in range(len(L)):
        D[L[i][0]] = []
        for j in range(len(L)):
            if i == j:
                continue
            if 10 <= L[i][1] - L[j][1] <= 20:
                D[L[i][0]].append(L[j][0])
    return D


scores = [{'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru',
           'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75,
           'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95},
          {'SeqNo': 1, 'Name': 'Kanmani', 'Gender': 'F', 'City': 'Bengaluru',
           'Mathematics': 75, 'Physics': 100, 'Chemistry': 79, 'Biology': 75,
           'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95},
          {'SeqNo': 1, 'Name': 'Katija', 'Gender': 'F', 'City': 'Bengaluru',
           'Mathematics': 81, 'Physics': 100, 'Chemistry': 79, 'Biology': 75,
           'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}]

print(mentors(scores, 'Mathematics'))