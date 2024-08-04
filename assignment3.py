def words_longer_than(words_list, n):
    return [word for word in words_list if len(word) > n]

sample_words = ['elephant', 'cat', 'dinosaur', 'apple', 'bee', 'giraffe', 'tiger']

n = 4

longer_words = words_longer_than(sample_words, n)
print(longer_words)
