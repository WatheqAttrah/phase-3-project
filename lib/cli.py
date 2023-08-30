#!/usr/bin/env python3

from helpers import view_cars

def main():
    while True:
        print("Menu: ")
        print("1. View Cars")
        print("2. Exit")
        
        option = input('Enter Your Option: ')
        if option == "1":
            view_cars()
        elif option == "2":
            print("Exit Application")
            break
    
    
if __name__ == "__main__":
    main()

