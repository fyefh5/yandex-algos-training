with open("hw3/input_d.txt", "r") as f:
    text = f.readlines()
unique_words = set()
for row in text:
    words = row.split()
    for word in words:
        unique_words.add(word)
print(len(unique_words))