str = input()
str = str.lower()
sortedStr = ''
strArr = []
for i in range(len(str)):
  strArr.append(str[i])
strArr.sort()
for j in range(len(strArr)):
  sortedStr += strArr[j]
print(sortedStr)