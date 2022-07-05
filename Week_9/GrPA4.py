def num_to_words(L):
    num_dic = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
               8: 'eight', 9: 'nine'}
    f = open('words.csv', 'w')
    line = ''
    count1 = 0
    count2 = 0
    for i in range(len(L)):
        count1 += 1
        for j in range(len(L[0])):
            count2 += 1
            value = L[i][j]
            number = num_dic[value]
            #print(value)
            if count2 != len(L[0]):
                line += number + ','
            else:
                if count2 == len(L[0]):
                    line += number + '\n'
                    count1 = 0
                    count2 = 0
    f.write(line)
    f.close()


num_to_words([[9, 7, 2], [1, 0, 5], [5, 2, 6]])
