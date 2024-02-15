input_string = "hii how are you going and  hii where are you where going "
words = {}
word_list = []
index_dict = {}
vector = []

# Split the input string into words
current_word = ""
for char in input_string:
    if char.isalnum():
        current_word += char.lower()
    elif current_word:
        word_list.append(current_word)
        current_word = ""
#
# if current_word:
#     word_list.append(current_word)

# Assign an index to each unique word and handle repeated words
index = 0
for word in word_list:
    if word not in words:
        words[word] = index
        index_dict[index] = word
        index += 1

# Create a vector based on the assigned indexes
for word in word_list:
    vector.append(words[word])

print("Dictionary:", words)
print("Index Dictionary:", index_dict)
print("Vector:", vector)
