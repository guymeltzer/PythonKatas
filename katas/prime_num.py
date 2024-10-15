def prime_number(num):
    """
    Check if the given number is prime or not.
    """
    if num == 0 or num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")



print(prime_number(5))  # True
print(prime_number(22))  # False

"""
To complete this exercise:
--------------------------
A prime number is an integer greater than 1 that cannot be divided by any other numbers except 1 and itself. 

Examples of prime numbers are 2, 3, 5, 7, 11, 13, etc.
 
A number is **not prime** if it can be divided evenly by another number (other than 1 and itself).
"""
