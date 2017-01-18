sentence = ("olly olly in come free")
sent_count = 0
word_count = sentence.split()

# here it counts the words in the senctence
numberofwords = len(word_count)
for ch in sentence:
    if ch == ".":
       sent_count += 1

print("There are", numberofwords, "words in this sentence")
print("There are", sent_count, "in this sentence")
