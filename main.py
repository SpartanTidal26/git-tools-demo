"""
main.py
this is a temp module docstring for main.py
"""
from utility_functions import _string_is_int


def print_welcome():
    print("Welcome to the Powerball number guesser!")

target_nums = []

if __name__ == '__main__':
    print_welcome()
    for _ in range(5):
        num = 0
        while not (_string_is_int(num)) or (1 > int(num) or int(num) > 69):
            num = input("Type a number between 1-69 inclusive")
            if (not _string_is_int(num)) or (1 > int(num) or int(num) > 69):
                print("ERROR: invalid entry")
        target_nums.append(num)

    print(target_nums)


