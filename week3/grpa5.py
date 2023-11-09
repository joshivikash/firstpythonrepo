import re
mob_num = input()
if re.match(r"^[6789]\d{9}$", mob_num):
  isValid = True
  for i in range(len(mob_num)):
      #count the number of occurences of each digit
      count = mob_num.count(mob_num[i])
      if(count > 7):
        isValid = False
        break
      else:
        mob_num_sub_str = mob_num[i:len(mob_num)]
        pattern = mob_num[i] + '{6}'
        if re.search(pattern, mob_num_sub_str):
          isValid = False
          break
  if(isValid):
    print("valid")
  else:
    print("invalid")
else:
  print("invalid")