# Define the range
start = 400
end = 300

# List to store numbers divisible by 7
divisible_by_7 = []

# Loop through the range and find numbers divisible by 7
for num in range(300, 400):
    if num % 7 == 0:
        divisible_by_7.append(num)

# Output the result
print("Numbers divisible by 7 in the range of", start, "to", end, "are:",divisible_by_7)
