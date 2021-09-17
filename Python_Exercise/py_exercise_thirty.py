phone = input("phone: ")
digit_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
}
output = ""
for x in phone:
    output += digit_mapping.get(x, "!")
    print(output)
