def multiply_by_two(number_list):
    return [number * 2 for number in number_list]


numbers = [1, 2, 3, 4, 5]
result_list_comprehension = multiply_by_two(numbers)
print(result_list_comprehension)