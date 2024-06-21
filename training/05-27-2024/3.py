def count_character_types(input_string):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    special_characters = '!@#$%^&*()-_=+[]{}|;:",.<>?/`~\\'
    
    num_vowels = 0
    num_consonants = 0
    num_special_characters = 0
    num_lowercase = 0
    num_uppercase = 0

    for char in input_string:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1
        elif char in special_characters:
            num_special_characters += 1
        if char.islower():
            num_lowercase += 1
        elif char.isupper():
            num_uppercase += 1

    return {
        "vowels": num_vowels,
        "consonants": num_consonants,
        "special_characters": num_special_characters,
        "lowercase": num_lowercase,
        "uppercase": num_uppercase
    }

input_string = "f46feLK9y56u#@&56hIjbn8KJhA"
result = count_character_types(input_string)

print(f"Nov: {result['vowels']}")
print(f"Noc: {result['consonants']}")
print(f"Nosc: {result['special_characters']}")
print(f"Nol: {result['lowercase']}")
print(f"Nou: {result['uppercase']}")

