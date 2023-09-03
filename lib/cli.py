#!/usr/bin/env python3

from helpers import view_cars, delete_car, export_as_csv, count_cars
from prettycli import green, yellow, red, blue


def main():
    while True:
        print("\n" * 5)
        print("welcome to:")
        print(
            blue(
                """

         ▄████████    ▄████████    ▄████████      ████████▄     ▄████████     ███        ▄████████     ███     ▀█████████▄     ▄████████    ▄████████    ▄████████
        ███    ███   ███    ███   ███    ███      ███   ▀███   ███    ███ ▀█████████▄   ███    ███ ▀█████████▄   ███    ███   ███    ███   ███    ███   ███    ███
        ███    █▀    ███    ███   ███    ███      ███    ███   ███    ███    ▀███▀▀██   ███    ███    ▀███▀▀██   ███    ███   ███    ███   ███    █▀    ███    █▀
        ███          ███    ███  ▄███▄▄▄▄██▀      ███    ███   ███    ███     ███   ▀   ███    ███     ███   ▀  ▄███▄▄▄██▀    ███    ███   ███         ▄███▄▄▄
        ███        ▀███████████ ▀▀███▀▀▀▀▀        ███    ███ ▀███████████     ███     ▀███████████     ███     ▀▀███▀▀▀██▄  ▀███████████ ▀███████████ ▀▀███▀▀▀
        ███    █▄    ███    ███ ▀███████████      ███    ███   ███    ███     ███       ███    ███     ███       ███    ██▄   ███    ███          ███   ███    █▄
        ███    ███   ███    ███   ███    ███      ███   ▄███   ███    ███     ███       ███    ███     ███       ███    ███   ███    ███    ▄█    ███   ███    ███
        ████████▀    ███    █▀    ███    ███      ████████▀    ███    █▀     ▄████▀     ███    █▀     ▄████▀   ▄█████████▀    ███    █▀   ▄████████▀    ██████████
                                  ███    ███

                      """
            )
        )
        print(yellow("Menu: Select one:"))

        print(green("1. View Cars"))
        print(green("2. Delete Car"))
        print(green("3. Count Cars"))
        print(green("4. Export as csv file"))
        print(green("5. Exit"))

        choice = input(red("Enter Your Option: "))
        choice = choice.strip()
        if choice == "1":
            view_cars()
        elif choice == "2":
            delete_car()
        elif choice == "3":
            count_cars()
        elif choice == "4":
            export_as_csv()
        elif choice == "5":
            print("~~~~~Exit Application~~~~~~~~~")
            break
        else:
            print(red("Invalid choise. Please Try Again."))


if __name__ == "__main__":
    main()
