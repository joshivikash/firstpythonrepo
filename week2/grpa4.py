from datetime import date
p1_name = input()
p1_dob = input()
p2_name = input()
p2_dob = input()
p1_dob = date(int(p1_dob[6:10]),int(p1_dob[3:5]),int(p1_dob[0:2]))
p2_dob = date(int(p2_dob[6:10]),int(p2_dob[3:5]),int(p2_dob[0:2]))
if(p1_dob == p2_dob):
  if(p1_name < p2_name):
    print(p1_name)
  else:
    print(p2_name)
elif(p1_dob < p2_dob):
  print(p2_name)
else:
  print(p1_name)