a = [4,6,7]
b = [3,6,8]
c = [0,0,0]
d = [0,0,0]
if a[0] > b[0]:
  c[0]=1
elif a[0] < b[0]:
  d[0]=1
else:
  c[0]=0
  d[0]=0
if a[1] > b[1]:
  c[1]=1
elif a[1] < b[1]:
  d[1]=1
else:
  c[1]=0
  d[1]=0
if a[2] > b[2]:
  c[2]=1
elif a[2] < b[2]:
  d[2]=1
else:
  c[2]=0
  d[2]=0
a_score = c[0]+c[1]+c[2]
b_score = d[0]+d[1]+d[2]
print('A score: ', a_score)
print('B score: ', b_score)
if(a_score > b_score):
  print('Winner is A')
elif (a_score < b_score):
   print('Winner is B')
else:
  print('Its a draw')
