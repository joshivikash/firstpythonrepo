names = input().split(',')
dates = input().split(',')
common = []
for i in range(len(names)):
  for j in range(i + 1,len(names)):
    if dates[i] == dates[j]:
      if(names[i] < names[j]):
        common.append([names[i],names[j]])
      else:
        common.append([names[j],names[i]])