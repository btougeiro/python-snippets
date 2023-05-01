# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# list_power_of_two = [ num**2 for num in numbers ]
# print(list_power_of_two)

# # conditional list comprehension

# only_even_numbers_list = [ num for num in numbers if num % 2 == 0 ]
# print(only_even_numbers_list)

# names = [ "Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]
# short_names = [ name for name in names if len(name) < 5 ]
# print(short_names)

# long_names_upper = [ name.upper() for name in names if len(name) > 4 ]
# print(long_names_upper)

# little exercise

with open("file_1.txt") as file_1:
    file_1_data = file_1.readlines()

with open("file_2.txt") as file_2:
    file_2_data = file_2.readlines()

result = [ int(element) for element in file_1_data if element in file_2_data ]
print(result)
