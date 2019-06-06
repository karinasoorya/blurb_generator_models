import numpy as np
import random
import dict_generator

def generator(graph, distance, chosen_thing):
    if distance == 0:
        return []
    start_node = chosen_thing
    while len(graph[start_node.lower()].values()) == 0:
        start_node = np.random.choice(graph.keys())
        print start_node
    weights = np.array(graph[start_node.lower()].values(), dtype=np.float64)
    weights /= weights.sum()
    choices = list(graph[start_node].keys())
    chosen_word = np.random.choice(choices, None, p=weights)
    return [chosen_word] + generator(
      graph, distance - 1, chosen_word)

for i in range(10):
    
    thing = generator(dict_generator.markov_graph, 120, "")
    for letter in range(len(thing)):
        if thing[letter][len(thing[letter]) - 1] in ['.', '!','?']:
            if letter + 1 < len(thing) - 1:
                if thing[letter + 1].isalpha():
                    thing[letter + 1] = thing[letter + 1].capitalize()
    blurb = ' '.join(thing)
    print blurb
