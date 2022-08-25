
def enterDate():

    while(True):

        date = int(
            input("Enter a one date with 8 Characters, in this format dia/mes/año = 24082022: "))
        date = str(date)

        day = date[0:2]
        month = date[2:4]
        year = date[4:8]

        if int(day) > 31:
            print("-"*90)
            print(
                "The day is invalid, because it is bigger than 31, please try again with a valid date")
            print("-"*90)
            continue
        if int(month) > 12:
            print("-"*90)
            print(
                "The month is invalid, because it is bigger than 12, please try again with a valid date")
            print("-"*90)
            continue

        if(len(date) == 8):
            formatDate = day + "/" + month + "/" + year
            print("-"*45)
            print("The entered date is: ", str(formatDate))
            print("-"*45)
            break
        elif (len(date) < 8 or len(date) > 8):
            print("-"*50)
            print("The date is not valid, please enter 8 characters")
            print("-"*50)
            continue


enterDate()
