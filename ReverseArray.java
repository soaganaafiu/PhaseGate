
public class ReverseArray{

    public static void main(String[] args){

        int[][] numbers = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

        int[][] answer = reverseArray(numbers);

       for(int index = 0; index < answer.length; index++){

            for(int count = 0; count < answer[index].length; count++){

                System.out.print(answer[index][count]);

            }

            System.out.println();

        }

    }



    static int[] reverse(int[] numbers){

        for(int index = 0; index < numbers.length / 2; index++){

            int container = numbers[index];
      
            numbers[index] = numbers[numbers.length - index - 1];

            numbers[numbers.length - index - 1] = container;

        }

        return numbers;

    }


    static int[][] reverseArray(int[][] matrix){

        for(int index = 0; index < matrix.length; index++){

            reverse(matrix[index]);

        }

        return matrix;

    }

}
