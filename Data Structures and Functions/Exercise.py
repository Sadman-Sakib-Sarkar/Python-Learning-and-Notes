#Find the letter which is present most frequent in the sentence

from pprint import pprint #it is for formatting the output

sentence = "This is a common interview question"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency, width=1)

print("\nSorted List: ")
char_frequency_sorted = (sorted(
    char_frequency.items(), 
    key=lambda kv: kv[1], 
    reverse=True))

pprint(char_frequency_sorted)

print("\nAnswer: ")
print(char_frequency_sorted[0])