def monotonic_array(lst):
    """
    This function returns True/False if the given list is monotonically increased or decreased
    """
    n = len(lst)
    if n <= 1:
        return True

    is_decreasing = True
    is_increasing = True

    for i in range(1,n):
                if lst[i] > lst[i - 1]:
                    is_decreasing = False
                elif lst[i] < lst[i - 1]:
                    is_increasing = False
    return is_increasing or is_decreasing



print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))  # False
print(monotonic_array([1, 2, 2, 2, 8, 9, 10]))  # True
