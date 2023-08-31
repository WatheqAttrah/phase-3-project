#!/usr/bin/env python3

from helpers import view_cars, delete_car, export_as_csv, count_cars


def main():
    while True:
        print("Menu: Select one:")

        print("1. View Cars")
        print("2. Delete Car")
        print("3. Count Cars")
        print("4. Export as csv file")
        print("5. Exit")

        option = input("Enter Your Option: ")
        if option == "1":
            view_cars()
        elif option == "2":
            delete_car()
        elif option == "3":
            count_cars()
        elif option == "4":
            export_as_csv()
        elif option == "5" or "exit" or "EXIT" or "Exit":
            print("~~~~~Exit Application~~~~~~~~~")
            break


if __name__ == "__main__":
    main()
