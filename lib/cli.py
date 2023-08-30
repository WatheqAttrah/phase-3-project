#!/usr/bin/env python3

from helpers import view_cars, delete_car, export_as_csv


def main():
    while True:
        print("Menu: ")
        print("1. View Cars")
        print("2. Delete Car")
        print("3. Export as csv file")
        print("4. Exit")

        option = input("Enter Your Option: ")
        if option == "1":
            view_cars()
        elif option == "2":
            delete_car()
        elif option == "3":
            export_as_csv()
        elif option == "4":
            print("Exit Application")
            break


if __name__ == "__main__":
    main()
