input_string = "deep learning is a subset of machine Learning  "
input_string2=" this is a string"
words = {}
word_list = []
index_dict = {}
vector = []

# Split the input string into words
current_word = ""
for char in input_string + " ":
    if char.isalnum():
        current_word += char.lower()
    else:
        if current_word:
            word_list.append(current_word)
            current_word = ""

# Count the occurrences of each word and assign an index to unique words
index = 0
for word in word_list:
    if word not in words:
        words[word] = 1  # Initialize count for a new word
        index_dict[index] = word
        index += 1
    else:
        words[word] += 1  # Increment count for repeated words

# Create a vector based on the word counts
for word in word_list:
    vector.append(words[word])

print("Dictionary:", words)
# print("Index Dictionary:", index_dict)
print("Vector:", vector)
