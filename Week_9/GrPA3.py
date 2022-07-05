def get_goals(filename, country):
    #print(type(country))
    f = open(filename, 'r')
    header = f.readline()
    player = 0
    goal = 0
    #lst = []
    for line in f:
        L = line.strip().split(",")
        #lst.append(L)
        #if country not in lst:
            #player = -1
            #goal = -1
        # print(L)
        #print(type(L[1]))
        #print(country)
        if L[1] == country:
            player = player + 1
            goal = goal + int(L[2])
    if player == 0 and goal == 0:
        player = -1
        goal = -1
    f.close()
    return ((player, goal))


print(get_goals("file.csv", "India"))
