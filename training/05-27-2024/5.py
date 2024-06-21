# Sample input list
input_list = [1, 2, 3.5, 4, 5, 6.7, 8, 9.1, 10]

# Lists to store even numbers, odd numbers, and float numbers
even_numbers = []
odd_numbers = []
float_numbers = []

# Iterate through the input list
for item in input_list:
    if isinstance(item, float):
        float_numbers.append(item)
    elif isinstance(item, int):
        if item % 2 == 0:
            even_numbers.append(item)
        else:
            odd_numbers.append(item)

# Output the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Float numbers:", float_numbers)
