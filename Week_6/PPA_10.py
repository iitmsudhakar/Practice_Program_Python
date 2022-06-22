def group_by_city(scores_dataset):
    cities  = dict()
    for i in range(scores_dataset):
        city = i['City']
        name = i['Name']
        if city not in cities:
            cities[city] = []
        cities[city].append(name)
    return cities
    
def busy_cities(scores_dataset):
    cities = group_by_city(scores_dataset)
    L = []
    max_student = 0
    for city in cities:
        if len(cities[city]) > max_student:
            max_student = len(cities[city])
            L = [city]
        elif len(cities[city]) == max_student:
            L.append(city)
    return L


def group_by_city(scores_dataset): 
    cities = dict() 
    for student in scores_dataset: 
        city = student['City'] 
        name = student['Name'] 
        if city not in cities: 
            cities[city] = [ ] 
        cities[city].append(name) 
    return cities 


def busy_cities(scores_dataset): 
    cities = group_by_city(scores_dataset) 
    busy = [ ] 
    maxpop = 0 
    for city in cities: 
        if len(cities[city]) >maxpop: 
            maxpop = len(cities[city]) 
            busy = [city] 
        elif len(cities[city]) == maxpop: 
            busy.append(city) 
    return busy 
