def solution(marks):
  ### Enter your solution below this line
  ### Indent your entire code by one unit (4 spaces) to the right
  # FILL THE MISSING CODE (...)
  sorted_marks = []
  while marks != []:
    min_mark = marks[0]
    for mark in marks:
      if mark < min_mark:
        min_mark = mark
    sorted_marks += [min_mark]
    marks.remove(min_mark)

  n = len(sorted_marks)
  center_index = n // 2
  if n % 2 != 0:
    median = sorted_marks[center_index]
  else:
    median = (sorted_marks[center_index - 1] + sorted_marks[center_index]) / 2

  ### Enter your solution above this line
  return median


def main():
  marks = [10, 4, 8, 2, 1]
  print(solution(marks))


main()
