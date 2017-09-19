dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'

def add_word(hun_word, eng_word):
    pass
# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    pass
    # for i in dictionary:
    #     if i['alma'] == 'apple':
    #             print(i)


def translate_to_eng(hun_word):
    for hun_word in dictionary:
        for element in hun_word:
            if element == 'apple':
                print(element)

translate_to_eng(dictionary)