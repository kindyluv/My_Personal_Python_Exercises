from precious import dictionary_two
from precious import calculator
from functions import exercise

print("\nWelcome to chat bot and calculator service ")

user_input = input("Enter 1 to perform first function and 2 to the second function and enter 3 to perform both "
                   "function: ")
user_inputs = input(
    """
    Enter 
    1 to get the maximum number of three
    2 to get the sum of a list
    3 to get the multiple number of a list
    4 to get the reverse of a string
    5 to get the factorial number
    6 to get the number fall
    7 to get the upper case and lower case number
    8 to get the unique element
    9 to get the prime number
    10 to get even number
    11 to get the perfect number
    12 to get the string palindrome 
    14 to get the pangram
    15 to get the hyphen_separated_sequence
    16 to get value square numbers
    """
)
if user_inputs == 1:
    user_inputs = exercise.maximum_of_three_numbers()
elif user_inputs == 2:
    user_inputs = exercise.sum_number()
elif user_inputs == 3:
    user_inputs = exercise.multiple()
elif user_inputs == 4:
    user_inputs = exercise.reverse_a_string()
elif user_inputs == 5:
    user_inputs = exercise.factorial()
elif user_inputs == 6:
    user_inputs = exercise.number_fall()
elif user_inputs == 7:
    user_inputs = exercise.string_uppercase_lowercase()
elif user_inputs == 8:
    user_inputs = exercise.unique_element()
elif user_inputs == 9:
    user_inputs = exercise.prime_number()
elif user_inputs == 10:
    user_inputs = exercise.even_number()
elif user_inputs == 11:
    user_inputs = exercise.perfect_number()
elif user_inputs == 12:
    user_inputs = exercise.string_palindrome()
elif user_inputs == 14:
    user_inputs = exercise.pangram()
elif user_inputs == 15:
    user_inputs = exercise.hyphen_separated_sequence()
elif user_inputs == 16:
    user_inputs = exercise.value_square_numbers()
else:
    print("invalid number")

# if user_input == 1:
#     user_input = dictionary_two.do_something()
# elif user_input == 2:
#     user_input = calculator.calculator()
# elif user_input == 3:
#     user_input = dictionary_two.do_something() and calculator.calculator()
#
# if __name__ == "__main__":
#     dictionary_two.do_something()
#
# if __name__ == "__main__":
#     calculator.calculator()
#
# if __name__ == "__main__":
#
#
# if __name__ == "__main__":
#
#
# if __name__ == "__main__":
#     exercise.string_uppercase_lowercase()
#
# if __name__ == "__main__":
#     exercise.unique_element("13445682")
#
# if __name__ == "__main__":
#     exercise.maximum_of_three_numbers()
# if __name__ == "__main__":
#     exercise.sum_number()
# if __name__ == "__main__":
#     exercise.multiple()
# if __name__ == "__main__":
#     exercise.reverse_a_string()
# if __name__ == "__main__":
#     exercise.factorial()
# if __name__ == "__main__":
#     exercise.number_fall()
# if __name__ == "__main__":
#     exercise.string_uppercase_lowercase()
# if __name__ == "__main__":
#     exercise.unique_element()
# if __name__ == "__main__":
#     exercise.prime_number()
# if __name__ == "__main__":
#     exercise.even_number()
# if __name__ == "__main__":
#     exercise.perfect_number()
# if __name__ == "__main__":
#     exercise.string_palindrome()
# if __name__ == "__main__":
#     exercise.pangram()
# if __name__ == "__main__":
#     exercise.hyphen_separated_sequence()
# if __name__ == "__main__":
#     exercise.value_square_numbers()

    # exercise.reverse_a_string()
    # exercise.factorial()
    # exercise.prime_number(13)
    # exercise.even_number((4, 46, 6, 7, 8, 5, 4, 1))
    # exercise.perfect_number(12)
    # exercise.string_palindrome("1991")
    # exercise.pangram("The quick brown fox jumps over the lazy dog")
    # exercise.maximum_of_three_numbers(24, 45, 15)
    # exercise.hyphen_separated_sequence("green-red-black-white")
    # exercise.value_square_numbers(16)
