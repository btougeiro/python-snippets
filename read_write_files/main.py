def read_file(file, new_msg):
    with open(file, mode="r") as f:
        content = f.read()
        if new_msg not in content:
            return True
        else:
            return False


def write_file(file, new_msg):
    with open(file, mode="a") as f:
        f.write(new_msg)


msg = "\nI'm a new message passed during a Python execution."

if read_file("file.txt", msg):
    write_file("file.txt", msg)
