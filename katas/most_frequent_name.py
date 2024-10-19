def most_frequent_name(file_path):
    """
    Receives a path to a file containing names (name in each line)
    The function should return the most frequent name in the file.

    You can assume file_path exists in the file system.
    """


        # Find the most frequent name
    with open(file_path, 'r') as file:
        names_list = file.read().splitlines()
        name_count = {}
        for name in names_list:
            if name in name_count:
                name_count[name] +=1
            else:
                name_count[name] = 1
        max_count = max(name_count, key = name_count.get)
        return max_count



if __name__ == '__main__':
    print(most_frequent_name('files/names.txt'))
