words = input()
real_dict = {}
for word in words.split(','):
    if word[0] in real_dict:
      real_dict[word[0]].append(word)
    else:
      real_dict[word[0]] = [word]