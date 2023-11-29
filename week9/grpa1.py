def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    f = open(filename,'r')
    d = {}
    for l in f:
        l = l.strip()
        if l in d:
            d[l] = d[l] + 1
        else:
            d[l] = 1
    f.close()
    return d

print(get_freq('pattern.txt'))