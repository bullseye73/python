from OCR.libs import cStringEx


def main():
    cse = cStringEx.cStringEx()
    cse.useFunc1()
    print("-------------------------")
    cse.func1()
    print("-------------------------")
    cse.cprint("color msg print")
    print("-------------------------")
    cse.cprint("select color msg print", "pink")


if __name__ == '__main__':
    main()
