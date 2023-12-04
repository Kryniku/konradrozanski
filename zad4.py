def print_every_second_number(number_list):
    for i in range(0, len(number_list), 2):
        print(number_list[i])


numbers = list(range(1, 11))
print_every_second_number(numbers)