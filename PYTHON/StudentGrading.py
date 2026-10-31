def scoreCollection(noOfStudent, noOfSubjects):

    scoresInput = []

    print("\nEnter Student Score")

    highestStudent = 0
    lowestStudent = 0

    classTotal = 0
    classAverage = 0.0

    for index in range(noOfStudent):

        print("\n\nStudent", (index + 1))

        scoreSum = 0
        amountOfScores = 0

        studentScores = []

        for count in range(noOfSubjects):

            scoreOfSubject = int(input(f"Enter score for Subject {(count + 1)}: "))

            while(scoreOfSubject < 0 or scoreOfSubject > 100):

                print("Invalid score!")

                scoreOfSubject = int(input("Enter score again: "))

            studentScores.append(scoreOfSubject)

            scoreSum += scoreOfSubject

            amountOfScores += 1

        scoresInput.append(studentScores)

        average = scoreSum / amountOfScores

        if(index == 0):

            lowestStudent = average

        print("Total:", scoreSum)
        print("Average:", average, "%")

        if(average > highestStudent):

            highestStudent = average

        if(average < lowestStudent):

            lowestStudent = average

        classTotal += scoreSum

        totalAverage = average / noOfStudent

        classAverage += totalAverage

    return scoresInput, highestStudent, lowestStudent, classTotal, classAverage    






def displayClassSummary(highestStudent, lowestStudent, classTotal, classAverage):

    print(f"""

    The hardest subject is Subject

    The easiest subject is Subject

    The overall Highest score is scored by Student

    The overall Lowest score is scored by Student 

    CLASS SUMMARY
    ===========================================================
    Best Graduating Student Scored:  {highestStudent:.2f}
    ===========================================================


    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Worst Graduating Student Scored: {lowestStudent:.2f}
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    ===============================================
    Class total score is: {classTotal}
    Class Average score is: {classAverage:.2f}
    ===============================================


    """)




print("STUDENT GRADING SYSTEM")

noOfStudent = int(input("Enter the number of students: "))

noOfSubjects = int(input("Enter the number of subjects: "))

scoresInput, highestStudent, lowestStudent, classTotal, classAverage = scoreCollection(noOfStudent, noOfSubjects)

displayClassSummary(highestStudent, lowestStudent, classTotal, classAverage)
        
