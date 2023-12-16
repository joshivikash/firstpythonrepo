import string
word = input()
source = list(string.ascii_lowercase)
dict = {key:source[25 - source.index(key)] for key in source}
result = ''
for c in word:
    result += dict[c]
print(result)