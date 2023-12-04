def multiply_by_two(number_list):
    result = []
    for number in number_list:
        result.append(number * 2)
    return result


numbers = [1, 2, 3, 4, 5]
result_for_loop = multiply_by_two(numbers)
print(result_for_loop)
