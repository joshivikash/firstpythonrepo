def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    l1 = f1.readline().strip()
    l2 = f2.readline().strip()
    while l2 != '':
        if l1 == '':
            return 'Subset'
        if l1 != l2:
            return 'No Relation'
        l1 = f1.readline().strip()
        l2 = f2.readline().strip()
    f1.close()
    f2.close()
    return 'Equal'

print(relation('f1.txt','f2.txt'))