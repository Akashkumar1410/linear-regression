input_string = "deep learning is a subset of machine learning"
input_string2 = "this is a a a a string"

combined_string = input_string + " " + input_string2
word_list = combined_string.lower().split()

# Use fromkeys() to initialize dictionary keys
words = dict.fromkeys(word_list, 0)
# Count the occurrences of each word without using set
for word in word_list:
    words[word] += 1

vector = [words[word] for word in word_list]

print("Dictionary:", words)
# print("Vector:", vector)
