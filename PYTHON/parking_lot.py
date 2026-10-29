parkingLot = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

menu = """
    
============================================
            Parking Lot System
============================================

Select an [Option]

1. Park a car
2. Remove a car
3. Parking status
0. Exit

============================================
""";

print(menu)
menuChoice = int(input("Enter a number: "))

match menuChoice:

    case 1:

        print("Parking Space")

        for index in range(len(parkingLot)):

            parkingLot[index] = 0

        for index in range(len(parkingLot)):

            print(parkingLot[index], "  ")

        print()


        park = True


        while(park):

            lot = int(input("Enter a parking lot number (1 - 20) and -1 to exit: "))

            indexOfLot = lot - 1
            
            if(lot >= 0 and lot <= 20)

                if(parkingLot[indexOfLot] == 0):

                    parkingLot[indexOfLot] = 1

                    print("Updated parking lot: ")

                    for index in range(len(parkingLot)):

                        print(parkingLot[index], " ")

                    print();

                else:

                    print("Sorry, this space is occupied.")

            elif(lot == -1):

                    print("GoodBye")

                    break

            else:

                print("Invalid parking lot number.")










