#!/usr/bin/env python3

from helpers import view_cars, delete_car, export_as_csv, count_cars
from prettycli import green, yellow, red, blue


def main():
    while True:
        print("\n" * 30)
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

        option = input(red("Enter Your Option: "))
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
