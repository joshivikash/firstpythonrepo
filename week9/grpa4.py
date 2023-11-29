def num_to_words(mat):
    """
    Convert matrix to file

    Argument: 
        mat: list of lists
    Return:
        None
    """
    f = open('words.csv','w')
    d = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    nos_of_rows = len(mat)
    for i in range(nos_of_rows):
        nos_of_columns = len(mat[i])
        for j in range(nos_of_columns):
            mapped_value = d[mat[i][j]]
            if j == nos_of_columns - 1:
                if i == nos_of_rows -1:
                    f.write(mapped_value)
                else:
                    f.write(mapped_value + '\n')
            else:
                f.write(mapped_value + ',')
    f.close()

print(num_to_words([[1]]))