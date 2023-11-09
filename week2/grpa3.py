# CODE WITH ALGORITHM
# Step-1: accept the text as input into a variable called string
string = input()
# Step-2: convert string to lower case; reassign the lower case version of text to string itself
string = string.lower()
# Step-3: define a variable called vowels; initialise it to the empty string
vowels=''
# Step-4: check if 'a' is in the variable string; if it is, concatenate 'a' to vowels at the end
if('a' in string):
  vowels +='a'
# Step-5: check if 'e' is in the variable string; if it is, concatenate 'e' to vowels at the end
if('e' in string):
  vowels +='e'
# Step-6: check if 'i' is in the variable string; if it is, concatenate 'i' to vowels at the end
if('i' in string):
  vowels +='i'
# Step-7: check if 'o' is in the variable string; if it is, concatenate 'o' to vowels at the end
if('o' in string):
  vowels +='o'
# Step-8: check if 'u' is in the variable string; if it is, concatenate 'u' to vowels at the end
if('u' in string):
  vowels +='u'
# Step-9: if vowels is empty, print 'none'
if(len(vowels) == 0):
    print('none')
  # Step-10: if vowels is not empty, print vowels
else:
    print(vowels)