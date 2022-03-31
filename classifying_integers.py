#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: March 2022
# This program lets the user classify an integer


def main():
    # this function lets the user classify an integer

    # input
    random_integer = int(input("Enter an integer: "))

    # process & output
    if random_integer > 0:
        print("{} is positive.".format(random_integer))

    elif random_integer < 0:
        print("{} is negative.".format(random_integer))
    elif random_integer < 0:
        print("{} is negative.".format(random_integer))
    elif random_integer == 0:
        print("{} is just zero.".format(random_integer))
    else:
        print("No idea!")


    print("")
    print("Done")

if __name__ == "__main__":
    main()
