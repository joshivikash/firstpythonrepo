import re;
password = input()
print('is less than 8:',8 > len(password))
print('is more than 32:',len(password) > 32)
print('has special chars:',re.search('[/\\=\'"\\s]', password) != None)
print('has start with alphabets:',re.match('[a-z]|[A-Z]', password[0]) == None)
if (8 > len(password) or len(password) > 32 or re.search('[/\\=\'"\\s]', password) != None or re.match('[a-z]|[A-Z]', password[0]) == None):
  print(False)
else:
  print(True)