import re
from collections import defaultdict

with open('true_finished', 'r') as text_file:
    stuff = text_file.read()
    words = [word for word in re.split('\s', stuff) if word != '']

markov_graph = defaultdict(lambda: defaultdict(int))

first_words = [word for word in words if word[0].isupper()]

last_words = [word for word in words if word[len(word) - 1] in ['.', '!', '?']]

last_word = words[0].lower()
for word in words[1:]:
    word = word.lower()
    markov_graph[last_word][word] += 1
    last_word = word

"""
for first in first_words:
    next_words = list(markov_graph[first].keys())[:limit]
    for next_word in next_words:
        print first, next_word
"""
to_delete = []

for key in markov_graph:
    if len(markov_graph[key].values()) == 0:
        to_delete.append(key)

for key in to_delete:
    markov_graph.pop(key)
