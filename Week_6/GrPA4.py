def two_level_sort(scores): 
    sorted_L = [ ] 
    while scores != [ ]: 

        minentry = scores[0] 
        for i in range(len(scores)): 

            if scores[i][1] < minentry[1]: 
                minentry = scores[i] 

            elif (scores[i][1] == minentry[1] and scores[i][0] < minentry[0]): 
                minentry = scores[i] 
        sorted_L.append(minentry) 
        scores.remove(minentry) 
    return sorted_L 


print(two_level_sort([('Harish', 80), ('Ram', 90), ('Harshita', 80)]))