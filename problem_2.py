import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_files = list()
    # Check if the input is a path
    if os.path.isdir(path):
        # For each item in the directory
        for item in os.listdir(path):
            # Recurse and add results of recursion into list of files
            for file in find_files(suffix, os.path.join(path, item)):
                list_of_files.append(file)

    # If the input ends with the input suffix (.c), then add it to the list of files
    if path.endswith(suffix):
        list_of_files.append(path)
    return list_of_files


# Using the sample file structure in the assignment description
path_to_check = "testdir"
extension_to_find = ".c"

print(find_files(extension_to_find, path_to_check))
