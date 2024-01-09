fruits = ['mango','orange','pineapple','apple','pear','papaya']
word_length = [5,6,9,5,4,6,0,0,0]

print(list(zip(fruits,word_length))) # [('mango', 5), ('orange', 6), ('pineapple', 9), ('apple', 5), ('pear', 4), ('papaya', 6)]
print(dict(zip(fruits,word_length))) # {'mango': 5, 'orange': 6, 'pineapple': 9, 'apple': 5, 'pear': 4, 'papaya': 6}