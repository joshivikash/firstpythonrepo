word = input()
length = len(word)
if length % 2 == 0:
    if word[-1] == '.' :
        word = word[:-1]
    else:
        word = word + '.'

length = len(word)
middle_position = length // 2
output_string = word[middle_position-1:middle_position + 2]
# Missing code here
print(output_string)