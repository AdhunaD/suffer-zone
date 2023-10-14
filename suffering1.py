import random
def create_a_list_of_numbers(amount_of_numbers):
    list_of_numbers = []
    for i in range(amount_of_numbers + 1):
        x = random.randint(0, 9999)
        list_of_numbers.append(x)
    return list_of_numbers

mylist = create_a_list_of_numbers(100)
print(mylist)

new_list = [2, 14, 8, 1, 9, 7]

counter1 = 0
while counter1 < len(new_list):
    counter = 0
    while counter < len(new_list) - 1:
        # this  is where I write the logic of the loop
        if new_list[counter] > new_list[counter+1]:
            # swap the numbers
            new_list[counter],new_list[counter+1] = new_list[counter+1],new_list[counter]
        print(new_list)
        counter = counter + 1

        # print(new_list)
    counter1 = counter1 + 1
print(new_list)