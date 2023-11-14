sorted_wins = []
most_wins = -1
for i in range(8):
    entry = input().split(',')
    team = entry[0]
    wins = len(entry) - 1
    if wins > most_wins:
        most_wins = wins
    if len(sorted_wins) == 0:
        sorted_wins.append((team,wins))
    else:
        inserted = False
        for sorted_win in sorted_wins:
            if wins > sorted_win[1]:
                sorted_wins.insert(sorted_wins.index(sorted_win),(team,wins))
                inserted = True
                break
            elif wins == sorted_win[1]:
                i = sorted_wins.index(sorted_win)
                sw = sorted_wins[i]
                while wins == sw[1] and team < sw[0]:
                    i += 1
                    sw = sorted_wins[i]
                sorted_wins.insert(i,(team,wins))
                inserted = True
                break
        if not inserted:
            sorted_wins.append((entry[0],wins))
for wins in sorted_wins:
    print(wins[0],':',wins[1], sep='')