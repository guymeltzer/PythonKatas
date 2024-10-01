def start_end(text, n, m):
    """
    The function returns the first 'n' characters from the string text,
    concatenated with the last 'm' characters from the string.

    If 'n' or 'm' are invalid (negative or larger than text length), return an empty string.
    """
    if n < 0 or m < 0 or n > len(text) or m > len(text):
        return ""

    first_characters = text[0:n]
    last_characters = text[-m:]

    return first_characters + last_characters

text = 'Elvis has left the building'
result = start_end(text, 3, 5)
print(result)  # Expected output: 'Elvlding'

result = start_end(text, 7, 2)
print(result)  # Expected output: 'Elvis hng'

result = start_end(text, 5, 4)
print(result)  # Expected output: 'Elvisding'

result = start_end('Pythonista', 4, 3)
print(result)  # Expected output: 'Pythsta'

result = start_end(text, 27, 1)  # Invalid input (too large)
print(result)  # Expected output: ''

"""
To complete this exercise:
--------------------------
No any implementation notes. 
"""
