MIN_LENGTH = 2


def main():
    pass_word = input("password > ")
    if len(pass_word) >= MIN_LENGTH:
        pass

    else:
        while len(pass_word) < MIN_LENGTH:
            pass_word = input("> ")

    print("***********")

main()
