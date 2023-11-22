import string

user_input = input("Enter a range of letters separated by a hyphen (eg a-c): ")
def get_letters_inside_range(user_input):
    try:
        start, end = user_input.split('-')
        start_index = string.ascii_letters.index(start)
        end_index = string.ascii_letters.index(end)
        result = string.ascii_letters[start_index:end_index + 1]

        return result
    except ValueError:
        return "Error! Check whether the data was entered correctly."

result_characters = get_letters_inside_range(user_input)
print(result_characters)
