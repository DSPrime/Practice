import re
import string
from collections import OrderedDict

text = str(input("Enter the text: "))


regex = re.compile('[%s]' % re.escape(string.punctuation))
text = regex.sub('', text)
text = text.replace('\n', ' ')
text = " ".join(text.split())
list_of_words = text.split()

l = []
def char_counter(string):
    chars_in_word = OrderedDict()
    for character in string:
        if character not in chars_in_word:
            chars_in_word[character] = 1
        else:
            chars_in_word[character] += 1
    return chars_in_word

def sorting_chars(list):
    strin = ''
    test = (char_counter(word) for word in list)
    for row in test:
        for key, value in row.items():
            if value == 1:
                l.append(key)
                break
    strin = strin.join(l)
    print(strin)
    return strin


chars_final = []
chars_final.append(sorting_chars(list_of_words))
l.clear()
sorting_chars(chars_final)
