def file_exceptions(file_path, op='r'):
    """
    Replaces ' ' by '_' in the given file_path.

    You have to except the MOST SPECIFIC exception and print an informative message for ALL potential file-related exceptions.
    The message must contain the exception name, e.g. RuntimeError, ZeroDivisionError, ...
    """
    try:
        with open(file_path, op) as file:
            content = file.read()
            content_modified = content.replace(' ', '_')
            return content_modified
    except FileNotFoundError:
        print("FileNotFoundError: The file does not exist please check the path again.")
        return ""
    except IsADirectoryError:
        print("IsADirectoryError: You are trying to open a directory, not a file. Please try again")
        return ""
    except PermissionError:
        print("PermissionError: You do not have permissions to open or modify this file")
        return ""
    except FileExistsError:
        print("FileExistsError: The file already exists, cannot create it.")
        return ""
    except OSError as e:
        print(f"OSError: {e.strerror}")
        return ""





if __name__ == '__main__':
    print(file_exceptions('files/nonexistent_file.txt'))
    print(file_exceptions('files/somefile'))
    print(file_exceptions('files/'))
    print(file_exceptions('files/someotherfile', op='x'))
    print(file_exceptions('files/someotherfile'))

