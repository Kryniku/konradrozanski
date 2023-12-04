def check_value_in_list(lst, value):
    return value in lst

my_list = [1, 2, 3, 4, 5]
value_to_check = 3
result = check_value_in_list(my_list, value_to_check)
print(f"Czy wartość {value_to_check} znajduje się w liście? {result}")
