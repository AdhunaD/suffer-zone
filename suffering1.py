import random
def create_a_list_of_numbers(amount_of_numbers):
    list_of_numbers = []
    for i in range(amount_of_numbers + 1):
        x = random.randint(0, 9999)
        list_of_numbers.append(x)
    return list_of_numbers

mylist = create_a_list_of_numbers(100)
print(mylist)

max_value = max(mylist)
print(max_value)