def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return: 
        result: tuple, (integer, integer)
    """
    f = open(filename,'r')
    # Read the Header, and move to next line from where the data starts
    f.readline()
    nos_of_players = -1
    nos_of_goals = -1
    for l in f:
        record = l.strip().split(',')
        if record[1] == country:
            if nos_of_players == -1:
                nos_of_players = 1
                nos_of_goals = int(record[2])
            else:
                nos_of_players += 1
                nos_of_goals += int(record[2])
        else:
            continue
    f.close()
    return (nos_of_players,nos_of_goals)


print(get_goals('goals.csv','Brazil'))