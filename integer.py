
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: October 11th 2022
# This program tells you if the given integer is 
# positive, negative or zero

def main():
    #Asking user to input an Integer
    user_integer = int(input ("Enter an Integer: "))
    print("") 

    #Determining whether the Integer is Positive, negative or Zero
    if user_integer >0:
        print(user_integer," is a positive number")
    elif user_integer <0:
        print(user_integer, " is a negative number")
    else:
        print(user_integer, " is just zero")

if __name__ == "__main__":
    main()