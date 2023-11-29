def get_scores(filename, index):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()	
    # we are now at the beginning of the second line of the file
    
    scores = [ ]
    line = f.readline()
    while line != '':
        L = line.strip().split(',')
        scores.append(int(L[index]))
        line = f.readline()
    
    f.close()
    return scores