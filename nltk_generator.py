from nltk.corpus import nps_chat
import random

noun_set = {word for word, pos in nps_chat.tagged_words() if pos.startswith('NN')}
print(type(noun_set))
noun_word = random.choice(list(noun_set))

adj_set = {word for word, pos in nps_chat.tagged_words() if pos.startswith('JJ')}
print(len(adj_set))
adj_word = random.choice(list(adj_set))

name_string = "".join([adj_word, "_", noun_word])
print(name_string.lower())
