# This program allows the user to choose varius
# geometry calculations from a menu.
# This program imports the circle and
# rectangle modules.

import circle # imports circle.py
import rectangle #imports rectangle.py
import math

# Constants for the menu choices

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# The main function.

def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    
    choice = 0
    
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()
        
        #Get the user's choice.
        choice = int(input("Enter your choice: "))
        
        #Perform the selected actopm
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('\nThe area is', circle.area(radius))
            print("\n")
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("\nThe circumference is", \
            circle.circumference(radius))
            print("\n")
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("\nThe area is", rectangle.area(width, length))
            print("\n")
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("\nThe perimeter is", \
                  rectangle.perimeter(width, length))
            print("\n")
        elif choice == QUIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: ivalid selection")
               
# the display_menu function displays a menu.
def display_menu():
    print("------------------------------------")
    
    print("\tMENU")
    print(" ")
    
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    
    print("5) Quit")
    print(" ")
    
#Call the main function
main()