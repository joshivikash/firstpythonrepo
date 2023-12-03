class StringManipulation:

    def __init__(self, words):
        self.words = words
    
    def total_words(self):
        return len(self.words)
    
    def count(self,some_word):
        return self.words.count(some_word)
    
    def words_of_length(self, length):
        words_with_same_length = list()
        for word in self.words:
            if(len(word) == length):
                words_with_same_length.append(word)
        return words_with_same_length
    
    def words_start_with(self, char):
        words_starting_with = []
        for word in self.words:
            if char == word[0]:
                words_starting_with.append(word)
        return words_starting_with
    
    def longest_word(self):
        longest_word = self.words[0]
        for i in range(1,len(self.words)):
            if len(self.words[i]) > len(longest_word):
                longest_word = self.words[i]
        return longest_word
    
    def palindromes(self):
        palindromes_words = []
        for word in self.words:
            if word == self.reverse(word):
                palindromes_words.append(word)
        return palindromes_words
    
    def reverse(self, word):
        reverse = ''
        for i in range(len(word)-1, -1, -1):
            reverse += word[i]
        return reverse
    

c =  StringManipulation()
print(c.reverse('abc'))