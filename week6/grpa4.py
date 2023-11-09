def two_level_sort(scores):
    """
    Perform a two-level sort

    Argument: 
        scores: list of tuples, (string, integer)
    Return:
        result: list of tuples (string, integer)
    """
    sorted_scores = []
    scores_length = len(scores)
    while scores_length > 0:
        min_marks_record = scores[0]
        for i in range(1, len(scores)):
            if scores[i][1] < min_marks_record[1]:
               min_marks_record = scores[i]
        if len(sorted_scores) == 0:
            sorted_scores.append(min_marks_record)
        else:
            inserted = False
            for score in sorted_scores:
                if score[1] == min_marks_record[1]:
                    if score[0] > min_marks_record[0]:
                        sorted_scores.insert(sorted_scores.index(score), min_marks_record)
                        inserted = True
                        break
            if not inserted:
                sorted_scores.append(min_marks_record)
        scores.remove(min_marks_record)
        scores_length = len(scores)
    return sorted_scores


print(two_level_sort([('Jane', 100),('Alice', 80), ('Bob', 75), ('Andy', 90), ('Alice', 100)]))
# print(two_level_sort([('Jane', 100), ('Alice', 100)]))