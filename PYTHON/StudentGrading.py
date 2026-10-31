def score_collection(no_of_student, no_of_subjects):

    scores_input = []

    print("\nEnter Student Score")

    highest_student = 0
    lowest_student = 0

    class_total = 0
    class_average = 0.0

    for index in range(no_of_student):

        print("\n\nStudent", (index + 1))

        score_sum = 0
        amount_of_scores = 0

        student_scores = []

        for count in range(no_of_subjects):

            score_of_subject = int(input(f"Enter score for Subject {(count + 1)}: "))

            while(score_of_subject < 0 or score_of_subject > 100):

                print("Invalid score!")

                score_of_subject = int(input("Enter score again: "))

            student_scores.append(score_of_subject)

            score_sum += score_of_subject

            amount_of_scores += 1

        scores_input.append(student_scores)

        average = score_sum / amount_of_scores

        if(index == 0):

            lowest_student = average

        print("Total:", score_sum)
        print("Average:", average, "%")

        if(average > highest_student):

            highest_student = average

        if(average < lowest_student):

            lowest_student = average

        class_total += score_sum

        total_average = average / no_of_student

        class_average += total_average

    return scores_input, highest_student, lowest_student, class_total, class_average    






def displayClassSummary(highest_student, lowest_student, class_total, class_average):

    print(f"""

    The hardest subject is Subject

    The easiest subject is Subject

    The overall Highest score is scored by Student

    The overall Lowest score is scored by Student 

    CLASS SUMMARY
    ===========================================================
    Best Graduating Student Scored:  {highest_student:.2f}
    ===========================================================


    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Worst Graduating Student Scored: {lowest_student:.2f}
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    ===============================================
    Class total score is: {class_total}
    Class Average score is: {class_average:.2f}
    ===============================================


    """)




print("STUDENT GRADING SYSTEM")

no_of_student = int(input("Enter the number of students: "))

no_of_subjects = int(input("Enter the number of subjects: "))

scores_input, highest_student, lowest_student, class_total, class_average = score_collection(no_of_student, no_of_subjects)

displayClassSummary(highest_student, lowest_student, class_total, class_average)
        
