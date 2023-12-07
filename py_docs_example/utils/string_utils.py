def reverse_string(s:str) ->str:
    """
    Reverse a given string.

    Args:
    s (str): The string to reverse.

    Returns:
    str: The reversed string.

    Example:
    >>> reverse_string("hello")
    'olleh'
    """
    return s[::-1]

def is_palindrome(s:str)->bool:
    """
    Check if a string is a palindrome. A palindrome is a string that reads the same forward and backward.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.

    Example:
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("hello")
    False
    """
    return s == s[::-1]

def count_vowels(s:str) ->int:
    """
    Count the number of vowels (a, e, i, o, u) in a string.

    Args:
    s (str): The string to count vowels in.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> count_vowels("hello world")
    3
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example usage
if __name__ == "__main__":
    test_string = "hello world"
    print("Reversed String:", reverse_string(test_string))
    print("Is Palindrome:", is_palindrome(test_string))
    print("Number of Vowels:", count_vowels(test_string))
