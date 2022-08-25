

def enteDataParking():
    print("*"*45)
    print("Welcome to the Metrocentro Parking System")
    print("*"*45)
    print("1-Domingo\n2-Lunes\n3-Martes\n4-Miercoles\n5-Jueves\n6-Viernes\n7-Sabado")
    print("-"*45)

    dayParking = int(input("What day is today, please enter the number: "))

    timeMinutes = int(input("Enter the time of stay in minutes: "))
    print("-"*45)

    data = [dayParking, timeMinutes]

    return data


def calculationPay(data):

    day = int(data[0])
    timeMinutes = data[1]
    totalParking = 0.00
    countExtraHours = timeMinutes

    if day == 1 or day == 7:

        if timeMinutes > 180:
            totalParking += 1.00

            if timeMinutes > 240:
                countExtraHours = timeMinutes - 240
                while(countExtraHours > 0):
                    totalParking += 3.00
                    countExtraHours -= 60
            print(f"You have to pay ${totalParking}")

        elif timeMinutes >= 16 and timeMinutes <= 180:
            totalParking = 0.50
            print(f"You have to pay ${totalParking}")

        elif timeMinutes < 16:
            totalParking = 0.00
            print(
                "Your parking is free, thanks for visiting")

    elif day in range(2, 7):
        if timeMinutes > 240:
            totalParking += 4.00

            if timeMinutes > 300:
                countExtraHours = timeMinutes - 300
                while(countExtraHours > 0):
                    totalParking += 3.00
                    countExtraHours -= 60
            print(f"You have to pay ${totalParking}")

        elif timeMinutes > 180 and timeMinutes <= 240:
            totalParking = 1.00
            print(f"You have to pay ${totalParking}")

        elif timeMinutes >= 16 and timeMinutes <= 180:
            totalParking = 0.25
            print(f"You have to pay ${totalParking}")

        elif timeMinutes < 16:
            totalParking = 0.00
            print(
                "Your parking is free, thanks for visiting")
    else:
        print("Invalided Day")


calculationPay(enteDataParking())
