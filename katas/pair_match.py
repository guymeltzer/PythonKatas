def pair_match(men, women):
    """
    This function receives two dictionaries in the form:
    {
        "<name>": <age>
    }

    Where <name> is a string name, and <age> is an integer representing the age.
    The function returns a pair of names (tuple) of men and women names,
    where their absolute age differences is the minimal.
    """
    min_diff = 46564456465645
    best_pair = None
    for (man, man_age) in men.items():
        for (woman, woman_age) in women.items():
            diff = abs(man_age - woman_age)
            if diff < min_diff:
                min_diff = diff
                best_pair = (man, woman)

    return best_pair

print(pair_match(
    {
        "John": 20,
        "Abraham": 45
    },
    {
        "July": 18,
        "Kim": 26
    }
))

# Expected ("John", "July"), since:

# abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
# abs(John - July) = abs(20 - 18) = abs(2) = 2
# abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
# abs(Abraham - July) = abs(45 - 18) = abs(27) = 27

