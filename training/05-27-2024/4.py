def transform_string(input_string):
    vowels = 'aeiouAEIOU'
    result = []

    for char in input_string:
        if char in vowels:
            result.append(char.upper())
        else:
            result.append(char.lower()) 

    return ''.join(result)
input_string = "Placements"
transformed_string = transform_string(input_string)

print("Original string: ", input_string)
print("Transformed string: ", transformed_string)
