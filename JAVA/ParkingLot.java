//import org.junit.jupiter.api.Test;
//import org.junit.jupiter.api.Assertions;


import java.util.Scanner;

public class ParkingLot{

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        int[] parkingLot = new int[20];




        String menu = """
                
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

        System.out.println(menu);
        System.out.print("Enter a number: ");
        int menuChoice = input.nextInt();

        switch(menuChoice){

            case 1 -> {

                System.out.println("Parking Space");


                for(int index = 0; index < parkingLot.length; index++){

                    parkingLot[index] = 0;


                }



                for(int index = 0; index < parkingLot.length; index++){

    //                        if(index % 4 == 0){
    //
    //                            System.out.println();
    //
    //                        }

                    System.out.print(parkingLot[index] + "  ");

                }
            
                System.out.println();


                boolean park = true;

                while(park){

                System.out.print("Enter a parking lot number (1 - 20) and -1 to exit: ");
                int lot = input.nextInt();

                int indexOfLot = lot - 1;

                if(lot >= 0 && lot <= 20){

                    if(parkingLot[indexOfLot] == 0){

                        parkingLot[indexOfLot] = 1;

                        System.out.print("Updated parking lot: ");

                        for(int index = 0; index < parkingLot.length; index++){

                            System.out.print(parkingLot[index] + " ");

                        }
                        
                        System.out.println();

                    } 

                        else{

                            System.out.println("Sorry, this space is occupied.");

                        }

                    }

                   else if(lot == -1){

                        System.out.println("GoodBye");

                            break;  

                    }

                    else{

                        System.out.println("Invalid parking lot number.");

                    }


                    }
                                    

            }

        }

    }

}
