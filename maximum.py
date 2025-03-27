numbers = [1, 2, 22, 34, 56, 77, 89, 98]


def maxo(x):
    maximum_number = 0
    for number in numbers:
        if number >= maximum_number:
            maximum_number = number
    return maximum_number


print(f"Maximum is {maxo(numbers)}")
