words = "Python is awesome and Python is easy"
words = words.split()

#print(words)

#print(len(words))

index_no = 0
#

word_count = {}

for item in words:
    count = words.count(item)
    word_count[item] = count

for word, count in word_count.items():
    print(word, ":", count)

""" print("########")
print(word_count) """