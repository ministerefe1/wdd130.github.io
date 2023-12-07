def main():
    # new_numbers = []
    try:
        # Open the file phone_numbers.txt for reading and read all
        # of the phone numbers into a list named phone_numbers.
        phone_numbers = read_list("phone_numbers.txt")

        # Some of the phone numbers in phone_numbers.txt do not start
        # with an area code. Replace each short phone number with a
        # phone number that begins with the area code "208-" To do this,
        # call the map function and pass the add_area_code function and
        # the list of phone numbers as arguments to the map function.
        new_numbers = list(map(add_area_code, phone_numbers))

        # Print the list with the corrected phone numbers.
        print(new_numbers)

    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")


def add_area_code(phone_number):
    """Phone numbers in the U.S. are often stored as ten digits and
    two dashes in this format: "ddd-ddd-dddd" where each d is a digit.
    If the length of phone_number is less than 12 characters, add the
    area code "208-" at the beginning of phone_number and return
    phone_number.

    Parameter phone_number: a string of digits formatted as
        "ddd-dddd" or "ddd-ddd-dddd"
    Return: a string of digits formated as "ddd-ddd-dddd"
    """
    if len(phone_number) < 12:
        phone_number = "208-" + phone_number
    return phone_number


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:
        # Read the contents of the text
        # file one line at a time.
        for line in text_file:
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

print()


def cels_fahr(fahr):
    cels = (fahr - 32) * 5 / 9

    return round(cels, 1)


def main():
    fahr_temp = [72, 65, 71, 75, 82, 87, 68]
    print(f"fahrenheit: {fahr_temp}")
    cels_temp = []
    for fahr in fahr_temp:
        cels = cels_fahr(fahr)
        cels_temp.append(cels)

        print(f"celsius: {cels_temp}")


if __name__ == ("__main__"):
    main()

print()


def cels_fahr(fahr):
    cels = (fahr - 32) * 5 / 9

    return round(cels, 1)


def main():
    fahr_temp = [72, 65, 71, 75, 82, 87, 68]
    print(f"fahrenheit: {fahr_temp}")

    cels_temp = list(map(cels_fahr, fahr_temp))

    print(f"celsius: {cels_temp}")


if __name__ == ("__main__"):
    main()

print()

# Example 2


print()


def main():
    numbers = [65, 89, 77, 90, 34, 67, 88]
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    print(f"average: {average:.2f}")


if __name__ == "__main__":
    main()

print()

from functools import reduce


def main():
    numbers = [65, 89, 77, 90, 34, 67, 88]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average = total / len(numbers)
    print(f"average: {average:.2f}")


if __name__ == "__main__":
    main()
