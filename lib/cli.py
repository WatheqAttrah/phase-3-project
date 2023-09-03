#!/usr/bin/env python3

from helpers import (
    view_cars,
    delete_car,
    export_as_csv,
    count_cars,
    count_4_cyc_cars,
    count_6_cyc_cars,
    view_one_car,
)
from prettycli import green, yellow, red, blue

# Define the main function 
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
        print(green("2. View One Car"))
        print(green("3. Delete Car"))
        print(green("4. Count Cars"))
        print(green("5. Cars 4 Cylender Engine"))
        print(green("6. Cars 6 Cylender Engine"))
        print(green("7. Export as csv file"))
        print(green("8. Exit"))

        choice = input(red("Enter Your Option: "))
        choice = choice.strip()
        if choice == "1":
            view_cars()
        elif choice == "2":
            view_one_car()
        elif choice == "3":
            delete_car()
        elif choice == "4":
            count_cars()
        elif choice == "5":
            count_4_cyc_cars()
        elif choice == "6":
            count_6_cyc_cars()
        elif choice == "7":
            export_as_csv()
        elif choice == "8":
            print("~~~~~Exit Application~~~~~~~~~")
            break
        else:
            print(red("Invalid choise. Please Try Again."))


if __name__ == "__main__":
    main()
