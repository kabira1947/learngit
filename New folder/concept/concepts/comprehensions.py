sentence = "the th quick browns" #fox jumps over the lazy dog"

'''words=sentence.split()
word_lengths= []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
        print(sentence)
        print(words)
        print(word_lengths)
'''
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)


# comprehension

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [float(x) for x in numbers if x < 0]
print(newlist)


newlist1 = "the there quickly"
words1= newlist1.split()
word_length1 = [len(words) for word in words if words1.count(newlist1) < 3]
word_length2 = [word for word in words1 if words1.count(word) < 2]
print(words1)
print(word_length1)
print(word_length2)