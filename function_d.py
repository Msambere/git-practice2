def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_num= 0
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
