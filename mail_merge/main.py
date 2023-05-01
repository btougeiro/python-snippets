PLACEHOLDER = "[name]"


def read_file(file):
    """
    Return the content of the read file.
    """
    with open(file, mode="r") as file:
        content = file.read()
        return content


def write_file(file, msg):
    """
    Write a message within the file passed by argument.
    """
    with open(file, mode="w") as file:
        file.write(msg)


letter = read_file("./Input/Letters/starting_letter.txt")
list_of_names = read_file("./Input/Names/invited_names.txt").split("\n")
for name in list_of_names:
    write_file(f"./Output/ReadyToSend/letter_for_{name}.txt", letter.replace(PLACEHOLDER, name))
