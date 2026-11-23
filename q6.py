text = input("Enter the sentence:")

#word frequency 
words = text.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

#character frequency
char_freq = {}

for ch in text:
    if ch == " ":
        continue
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1

print("word frequency:",word_freq)
print("character frequency:",char_freq)