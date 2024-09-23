def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    try:
        return max(numbers)
    except ValueError, TypeError:
        # This will handle the case where the list is empty or non-numeric elements
        return None


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
