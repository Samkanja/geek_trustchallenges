from sys import argv
from src.cart import Cart
from typing import TextIO, List


class GeekAcademy:
    def __init__(self) -> None:
        self.cart = Cart()
        if len(argv) != 2:
            raise Exception("Add there file path")
        self.file_path = argv[1]
        self.file = open(self.file_path, "r")

        self.last_line = self.file.readline()

    def absorb_input(self):
        try:
            while self.has_next_line():
                line = self.next_line()
                command, *command1 = line.strip().split()
                match command:
                    case "ADD_PROGRAMME":
                        prog = command1[0]
                        qty = int(command1[-1])
                        self.cart.add_program(prog, qty)

                    case "PRINT_BILL":
                        self.cart.print_bill()

                    case "APPLY_COUPON":
                        self.cart.has_coupon(command)
        finally:
            self.dispose()

    def has_next_line(self):
        return self.last_line != ""

    def next_line(self):
        line = self.last_line
        self.last_line = self.file.readline()
        return line

    def dispose(self):
        self.file.close()


def main():
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    gk = GeekAcademy()
    gk.absorb_input()


if __name__ == "__main__":
    print(main())
