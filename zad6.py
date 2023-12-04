def merge_and_cube_lists(list1, list2):
    merged_list = list1 + list2
    unique_values = list(set(merged_list))
    cubed_values = [x**3 for x in unique_values]
    return cubed_values


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
result_list = merge_and_cube_lists(list_a, list_b)
print(f"Wynik po złączeniu list, usunięciu duplikatów "
      f"i podniesieniu do potęgi 3: {result_list}")
