import string, random

lower_alphabet = list(string.ascii_lowercase)

vowel_list = ["a", "e", "i", "o", "u"]
all_consonants = [letter for letter in lower_alphabet if letter not in vowel_list]

mid_consonant_list = ["r", "l", "n", "h", "y"]
non_mid_consonant_list = [
    letter for letter in lower_alphabet if letter not in mid_consonant_list
]

end_no_vowel_consonant_list = ["w", "v", "c", "x", "l", "s", "j"]

noun_syllable_list = ["th", "vr"]
adjective_ends = ["ing", "ed", "ly"]

word_component_list = []

starter_letter = random.choice(lower_alphabet)
word_component_list.append(starter_letter)
if starter_letter in vowel_list:
    word_component_list.append(random.choice(all_consonants))
else:
    word_component_list.append(
        random.choice([random.choice(mid_consonant_list), random.choice(vowel_list)])
    )

word_component_list.append(random.choice(vowel_list))

second_syllable = [random.choice(mid_consonant_list)]
if second_syllable[0] in vowel_list:
    second_syllable.append(random.choice(end_no_vowel_consonant_list))
elif second_syllable[0] == "y":
    second_syllable.append(random.choice(vowel_list))
else:
    second_syllable.append(random.choice(non_mid_consonant_list))

word_component_list.extend(second_syllable)

print(str(word_component_list))
