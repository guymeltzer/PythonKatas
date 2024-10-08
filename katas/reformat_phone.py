def reformat_phone(phone_str):
    """
    This function takes a string representing a phone number and reformats it into
    a standardized format: (XXX) XXX-XXXX, where X represents a digit.
    The function removes any non-numeric characters from the string and reformats it.

    Return None if the input is invalid (not exactly 10 digits)
    """
    phone_str = ''.join(filter(str.isdigit, phone_str))

    if len(phone_str) != 10:
        return None

    return f"({phone_str[:3]}) {phone_str[3:6]}-{phone_str[6:]}"


print(reformat_phone("123-456-7890"))  # Expected output: (123) 456-7890
print(reformat_phone("(123) 456-7890"))  # Expected output: (123) 456-7890
print(reformat_phone("1234567890"))  # Expected output: (123) 456-7890
print(reformat_phone("123-45"))  # Expected output: None


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
The `isdigit()` can help you to filter out non-numeric characters.
"""
