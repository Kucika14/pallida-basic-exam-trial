# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

odd_filter = [1, 2, 3, 4, 5]  # sould print [1, 3, 5]

def odd_list(odd_filter):
    odd_list = []
    for i in odd_filter:
        if i % 2 != 0 and i !=0:
            odd_list.append(i)
        print(odd_list)

odd_list(odd_filter)