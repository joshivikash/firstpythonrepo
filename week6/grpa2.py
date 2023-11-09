# COMPLETE MISSING CODE
def words_to_frequency(words):
    """
    Return a dict that has frequencies of words

    Argument: 
      words: list of strings
    Return:
      freq_dict: 
        key: string
        value: int
    """
    # this function will be used in the main function we need to write
    freq_dict = {}
    for word in words: 
        if word not in freq_dict:
          freq_dict[word] = 1
        else:
          freq_dict[word] += 1
    return freq_dict
    
def freq_to_words(words):
    """
    Get the collection of all words that have a given frequency

    Argument
       words: list of strings
    Return: 
       result: dictionary 
           key: integer
           value: list of strings
    """
    # this dict has frequencies of words
    freq_dict = words_to_frequency(words)

    result = dict()
    for word in freq_dict:
        freq = freq_dict[word]
        if freq not in result:
            result[freq] = [word]
        else:
            result[freq] += [word]

    return result


