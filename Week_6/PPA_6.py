def get_marks(scores_dataset, subject):
    L = []
    for x in scores_dataset:
        marks = x[subject]
        name = x['Name']
        L.append((name, marks))
    return L