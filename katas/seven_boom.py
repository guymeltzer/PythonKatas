def seven_boom(n):
    """
    This functions returns a list of all "Booms" for a 7-boom play starting from 1 to n
    """
    seven_list = []
    for n in range (1,n):
        if n % 7 == 0:
            seven_list.append(n)
        elif str(n).__contains__('7'):
            seven_list.append(n)
    return seven_list


print(seven_boom(30))  # Expected [7, 14, 17, 21, 27, 28]

