def get_readfile(filepath="workout.txt"):
    """This is first doc string written for the function
    this gets the argument for file, if file is placed under different location then specify full path /usr/path/filename
    and basically retrieves the output of file contents in list"""
    with open(filepath) as file:
        todos_read = file.readlines()
    return todos_read


def get_writefile(todos_arg, filepath="workout.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# help(get_readfile) --- printing fdocumentation , that is function documentation
if __name__ == "__main__":
    print("Hello")