import java.util.Scanner;
public class StudentGrading{

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of students: ");
        int noOfStudent = input.nextInt();

        System.out.print("Enter the number of subjects: ");
        int noOfSubjects = input.nextInt();

        System.out.println("Student Scores");


        int[][] scoresInput = new int[noOfStudent][noOfSubjects];

        System.out.println("Enter Student Scores ");


        double highestStudent = 0;
        double lowestStudent = 0;



        int classTotal = 0;
        double classAverage = 0.0;

        for(int index = 0; index < noOfStudent; index++){

            System.out.println("\nStudent " + (index + 1));

            int scoreSum = 0;
            double amountOfScores = 0.0;


            for(int count = 0; count < noOfSubjects; count++){

                System.out.print("Enter Score for Subject: ");
                int scoreOfSubject = input.nextInt();   

                while (scoreOfSubject < 0 || scoreOfSubject > 100) {

                    System.out.println("Invalid score!");

                    System.out.print("Enter the right score: ");

                    scoreOfSubject = input.nextInt();

                }
 

                scoresInput[index][count] = scoreOfSubject;

                scoreSum += scoreOfSubject;

                amountOfScores++;

            }
            double average = scoreSum / amountOfScores;

            lowestStudent = average;

            System.out.println("Total: " + scoreSum);
            System.out.println("Average: " + average + "%");

            if(average > highestStudent){

                highestStudent = average;


            }

            if(average < lowestStudent){

                lowestStudent = average;

            }

            classTotal += scoreSum;
            double totalAverage = average/noOfStudent;
            classAverage += totalAverage;

        }

        System.out.printf("""

        The hardest subject is Subject

        The easiest subject is Subject

        The overall Highest score is scored by Student

        The overall Lowest score is scored by Student `                                        

        CLASS SUMMARY
        ===========================================================
        Best Graduating Student Scored:  %.2f
        ===========================================================


        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        Worst Graduating Student Scored: %.2f
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


        ===============================================
        Class total score is: %d
        Class Average score is: %.2f
        ===============================================


        """,highestStudent, lowestStudent, classTotal, classAverage); 

    }


}
