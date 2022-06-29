def get_marks(scores_dataset, subject, gender): 
    L = [ ] 
    for student in scores_dataset: 
        if student['Gender'] == gender: 
            marks = student[subject] 
            name = student['Name'] 
            L.append((name, marks)) 
    return L 


def get_toppers(scores_dataset, subject, gender): 
    L = get_marks(scores_dataset, subject, gender) 
    toppers = [ ] 
    maxmarks = 0
    for i in range(len(L)): 
        if L[i][1] >maxmarks: 
            maxmarks = L[i][1] 
            toppers = [L[i][0]] 
        elif L[i][1] == maxmarks: 
            toppers.append(L[i][0]) 
    return toppers 
