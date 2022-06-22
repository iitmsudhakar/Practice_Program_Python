def words_to_frequency(words): 
    freq_dict = dict() 
    for word in words: 
        if word not in freq_dict: 
            freq_dict[word] = 0 
        freq_dict[word] += 1 
    return freq_dict 


def freq_to_words(words): 
    freq_dict = words_to_frequency(words) 
    result = dict() 
    for word in freq_dict: 
        freq = freq_dict[word] 
        if freq not in result: 
            result[freq] = [ ] 
        result[freq].append(word) 
    return result


print(freq_to_words(['a', 'random', 'collection', 'a', 'another', 'a', 'random']))