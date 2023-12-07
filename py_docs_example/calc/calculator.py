def calculate_mean(numbers:list)-> float:
    """
    Calculate the mean (average) of a list of numbers.

    Args:
    numbers (list of float/int): A list of numbers.

    Returns:
    float: The mean of the numbers.

    Example:
    >>> calculate_mean([1, 2, 3, 4, 5])
    3.0
    """
    return sum(numbers) / len(numbers) if numbers else 0


def calculate_median(numbers:list)-> float:
    """
    Calculate the median (middle value) of a list of numbers.

    Args:
    numbers (list of float/int): A list of numbers. This list will be sorted.

    Returns:
    float: The median of the numbers.

    Example:
    >>> calculate_median([1, 3, 4, 2, 5])
    3.0
    """
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]


def calculate_mode(numbers:list)-> list:
    """
    Calculate the mode (most frequently occurring value) of a list of numbers.

    Args:
    numbers (list of float/int): A list of numbers.

    Returns:
    list: A list containing the mode(s). More than one mode will be returned if there's a tie.

    Example:
    >>> calculate_mode([1, 2, 2, 3, 3])
    [2, 3]
    """
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    return [num for num, freq in frequency.items() if freq == max_freq]


# Example usage
if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 5, 5, 3]
    print("Mean:", calculate_mean(sample_numbers))
    print("Median:", calculate_median(sample_numbers))
    print("Mode:", calculate_mode(sample_numbers))
