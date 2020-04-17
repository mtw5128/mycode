#!/usr/bin/env python3

answer = " "




answer = input('Does it move? ').lower().strip()

def main():

    if answer == "yes":
        input('Should it? ')
        if answer == "yes":
            print('No Problem!')
            break    
        elif answer == "no":
            print('Use duct tape!')
            break
        else:
            print("Invalid Entry!") # end of question 1
            answer = input('Please answer "Yes" or "No" \n Does it move? ').lower().strip()


    elif answer == "no":
        input('Should it? ')
        if answer == "yes":
            print('Use WD-40!')
            break
        elif answer == "no":
            print('No Problem!')
        else:
            print("Invalid Entry!") # end of question 1
            answer = input('Please answer "Yes" or "No" \n Does it move? ').lower().strip() 

    else:
        print("Invalid Entry!") # end of question 1
        answer = input('Please answer "Yes" or "No" \n Does it move? ').lower().strip()


main()


