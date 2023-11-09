# DEBUG CODE
def get_marks(scores_dataset, subject, gender):
  L = []
  for student in scores_dataset:
    if student['Gender'] == gender:
      marks = student[subject]
      name = student['Name']
      L.append([name, marks])
  return L


def get_toppers(scores_dataset, subject, gender):
  """
    Get the toppers in subject belonging to gender

    Arguments:
        scores_dataset: list of dicts
        subject: string
        gender: string ('F' or 'M')
    Return:
        list of strings
    """
  L = get_marks(scores_dataset, subject, gender)
  toppers = []
  maxmarks = 0
  for i in range(len(L)):
    if L[i][1] > maxmarks:
      maxmarks = L[i][1]
  for i in range(len(L)):
    if L[i][1] == maxmarks:
      toppers.append(L[i][0])
  return toppers


scores_dataset = [
    {
        'SeqNo': 1,
        'Name': "Devika",
        'Gender': "F",
        'City': "Bengaluru",
        'Mathematics': 64,
        'Physics': 48,
        'Chemistry': 79,
        'Biology': 75,
        'Computer Science': 88,
        'History': 43,
        'Civics': 78,
        'Philosophy': 55,
    },
    {
        'SeqNo': 2,
        'Name': "Astha",
        'Gender': "F",
        'City': "Bengaluru",
        'Mathematics': 45,
        'Physics': 98,
        'Chemistry': 78,
        'Biology': 58,
        'Computer Science': 64,
        'History': 65,
        'Civics': 98,
        'Philosophy': 78,
    },
    {
        'SeqNo': 3,
        'Name': "Rahul",
        'Gender': "M",
        'City': "Bengaluru",
        'Mathematics': 55,
        'Physics': 65,
        'Chemistry': 98,
        'Biology': 78,
        'Computer Science': 64,
        'History': 45,
        'Civics': 58,
        'Philosophy': 98,
    },
    {
        'SeqNo': 4,
        'Name': "Raj",
        'Gender': "M",
        'City': "Bengaluru",
        'Mathematics': 78,
        'Physics': 64,
        'Chemistry': 58,
        'Biology': 65,
        'Computer Science': 98,
        'History': 45,
        'Civics': 98,
        'Philosophy': 78,
    },
]

print(get_toppers(scores_dataset, "Mathematics", "F"))
