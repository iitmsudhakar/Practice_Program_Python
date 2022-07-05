def collection_to_file(scores_dataset):
    f = open("scores.csv", "w")
    f.write('SeqNo,Name,Gender,City,Mathematics,Physics,Chemistry\n')
    for val in scores_dataset:
        sno = val['SeqNo']
        name = val['Name']
        gen = val['Gender']
        city = val['City']
        math = val['Mathematics']
        phy = val['Physics']
        chem = val['Chemistry']
        li = f'{sno},{name},{gen},{city},{math},{phy},{chem}\n'
        if val['SeqNo'] == scores_dataset[-1]['SeqNo']:
            li = li.strip()
        f.write(li)
    f.close()
