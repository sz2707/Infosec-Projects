array = []
while len(array) < 5:
    user_input = int(input("Enter a number: "))
    array.append(user_input)
print(f"Array: {array}")

average = 0
for number in array:
    average += number
average /= 5
print(f"Average of the values: {average}")