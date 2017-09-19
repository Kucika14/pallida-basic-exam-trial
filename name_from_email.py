# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

# print(name_from_email("elek.viz@exam.com"))
user_input = input('Please give your email! It should be look like this : firstName.lastName@exam.com\nWrite your email here: ')

def give_back_name(name):
    print(name)
    for word in user_input.split('.'):
        print(word)

give_back_name(user_input)