# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

# print(name_from_email("elek.viz@exam.com"))
user_input = input('Please give your email! It should be look like this : firstName.lastName@exam.com\nWrite your email here: ')

def give_back_name(name):
    splitted = user_input.split('@')
    result = splitted[0]
    second_split = result.split('.')
    final_result = (second_split[::-1])
    first_name = final_result[0]
    second_name = final_result[1]
    print(first_name.capitalize() + " " + second_name.capitalize())


give_back_name(user_input)