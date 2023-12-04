def print_even_numbers(number_list):
    for number in number_list:
        if number % 2 == 0:
            print(number)

# Przykład użycia
numbers = list(range(1, 11))
print_even_numbers(numbers)