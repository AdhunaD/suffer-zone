import random
def create_a_list_of_numbers(amount_of_numbers):
    list_of_numbers = []
    for i in range(amount_of_numbers + 1):
        x = random.randint(0, 9999)
        list_of_numbers.append(x)
    print(list_of_numbers)

create_a_list_of_numbers(100)