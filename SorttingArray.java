import java.util.Arrays;
public class SortingArray{

    public static void main(String[] args){

        int[] numbersOne = {1, 2, 4};

        int[] numbersTwo = {1, 3, 4};

        int addArray = numbersOne.length + numbersTwo.length;
        int[] joinArray = new int[addArray];


        for(int index = 0; index < numbersOne.length; index++){

            joinArray[index] = numbersOne[index];

        }

        for(int index = 0; index < numbersTwo.length; index++){

            joinArray[numbersOne.length + index] = numbersTwo[index];

        }



        for(int index = 0; index < joinArray.length; index++){

            for(int count = index + 1; count < joinArray.length; count++){

                if(joinArray[index] > joinArray[count]){

                    int result = joinArray[index];

                    joinArray[index] = joinArray[count];

                    joinArray[count] = result;

                }

            }

        }




        for(int index = 0; index < joinArray.length; index++){

            System.out.print(joinArray[index]);

        }

    }

}

