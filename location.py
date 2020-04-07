#!/usr/bin/env python3

count = 0
answer = " "
message = "You've got quite the life! You should PROBABLY be living in/on the "


# mountains = 0-2
# forest = 3-4
# beach = 5-6
# city = 7-10


while count <= 10:
    
    answer = input('Are you a social butterfly? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 1
        print("Nice to meet you, then!")
        
    elif answer == "no":
        count += 0
        print("Reading's better anyway!")
        
    else:
        count += 0
        print("Please enter (Yes/No)") # end of question 1
        answer = input('Are you a social butterfly? (Yes/No)').lower().strip()

    answer = input('Do you like quiet walks? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 0
        print("Who doesn't?")
        
    elif answer == "no":
        count += 1
        print("Thats' alright!")
        
    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('Do you like quiet walk? (Yes/No)').lower().strip()

    answer = input('Are you an active person? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 1
        print("Get SWOLE!")
        
    elif answer == "no":
        count += 1
        print("Do you even lift, bro?")
        
    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('Are you an active person? (Yes/No)').lower().strip()

    answer = input('Do you mind being alone? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 1
        print("We'll keep you company!")
        
    elif answer == "no":
        count += 0
        print("COVID can't catch you!")
        
    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('Do you mind being alone? (Yes/No)').lower().strip()

    answer = input('Do you love animals? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 0
        print("They're so cute!")
        
    elif answer == "no":
        count += 1
        print("Allergies? Us too..")
        
    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('Do you love animals? (Yes/No)').lower().strip()

    answer = input('Are you a fan of completing projects? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 0
        print("Gotta love a sense of accomplishment!")
        
    elif answer == "no":
        count += 1
        print("There's too much to see on Netflix anway..")
        
    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('Are you a fan of completing projects? (Yes/No)').lower().strip()

    answer = input('Do you own a car? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 0
        print("Zoom, zoom!")

    elif answer == "no":
        count += 0
        print("Go green or go home!")

    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('Do you own a car? (Yes/No)').lower().strip()

    answer = input('Are you into surfing? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 1
        print("Shred some gnar!")

    elif answer == "no":
        count += 0
        print("Duhdun...duhdun.. duhdun duhdundununununun!!")

    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('Are you into surfing? (Yes/No)').lower().strip()

    answer = input('You love to go out on the town, right?!? (Yes/No)').lower().strip()
    if answer == "yes":
        count += 1
        print("Party on, Wayne!")

    elif answer == "no":
        count += 0
        print("Nothing wrong with a night in!")

    else:
        count += 0
        print("Please enter (Yes/No)")  # end of question 10
        answer = input('You love to go out on the town, right?!?? (Yes/No)').lower().strip()

    answer = input('Do you prefer fresh water or salt water? (Fresh/Salt)').lower().strip()
    if answer == "fresh":
        count += 0
        print("Hope you brought a fishing pole!")

    elif answer == "salt":
        count += 1
        print("We're gonna need a bigger quiz..")

    else:
        count += 0
        print("Please enter (Fresh/Salt)")  # end of question 10
        answer = input('Do you prefer fresh water or salt water? (Fresh/Salt)').lower().strip()


    break

if count >=0 and count < 3:
    print(message + "mountains!")
elif count >=3 and count <5:
    print(message + "forest!")
elif count >=5 and count <7:
    print(message + "beach!")
elif count >=7 and count <10:
    print(message + "city!")
#print(count)




