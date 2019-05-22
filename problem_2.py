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

# The provided test directory has multiple test cases:
# Case 1: matching file in top level:               \t1.c
# Case 2: non-matching file in top level:           \t1.h
# Case 3: matching file one level deep              \subdir1\a.c
# Case 4: non-matching file one level deep          \subdir2\.gitkeep
# Case 5: matching file multiple levels deep        \subdir3\subsubdir1\b.c
# Case 6: non-matching file multiple levels deep    \subdir3\subsubdir1\b.h

# Expected results: testdir\t1.c, testdir\subdir1\a.c, testdir\subdir3\subsubdir1\b.c, testdir\subdir5\a.c,
print(find_files(extension_to_find, path_to_check))
