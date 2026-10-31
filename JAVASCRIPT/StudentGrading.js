function score_collection(no_of_student, no_of_subjects) {

    let scores_input = [];

    console.log("\nEnter Student Score");

    let highest_student = 0;
    let lowest_student = 0;

    let class_total = 0;
    let class_average = 0.0;

    for (let index = 0; index < no_of_student; index++) {

        console.log("\n\nStudent", (index + 1));

        let score_sum = 0;
        let amount_of_scores = 0;

        let student_scores = [];

        for (let count = 0; count < no_of_subjects; count++) {

            let score_of_subject = Number(prompt(`Enter score for Subject ${count + 1}: `));

            while (score_of_subject < 0 || score_of_subject > 100) {

                console.log("Invalid score!");

                score_of_subject = Number(prompt("Enter score again: "));
            }

            student_scores.push(score_of_subject);

            score_sum += score_of_subject;

            amount_of_scores++;
        }

        scores_input.push(student_scores);

        let average = score_sum / amount_of_scores;

        if (index === 0) {

            lowest_student = average;
        }

        console.log("Total:", score_sum);
        console.log("Average:", average, "%");

        if (average > highest_student) {

            highest_student = average;
        }

        if (average < lowest_student) {

            lowest_student = average;
        }

        class_total += score_sum;

        let total_average = average / no_of_student;

        class_average += total_average;
    }

    return [scores_input, highest_student, lowest_student, class_total, class_average];
}


function displayClassSummary(highest_student, lowest_student, class_total, class_average) {

    console.log(`

    The hardest subject is Subject

    The easiest subject is Subject

    The overall Highest score is scored by Student

    The overall Lowest score is scored by Student 

    CLASS SUMMARY
    ===========================================================
    Best Graduating Student Scored:  ${highest_student.toFixed(2)}
    ===========================================================


    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Worst Graduating Student Scored: ${lowest_student.toFixed(2)}
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    ===============================================
    Class total score is: ${class_total}
    Class Average score is: ${class_average.toFixed(2)}
    ===============================================


    `);
}




console.log("STUDENT GRADING SYSTEM");

let no_of_student = Number(prompt("Enter the number of students: "));

let no_of_subjects = Number(prompt("Enter the number of subjects: "));

let [scores_input, highest_student, lowest_student, class_total, class_average] = score_collection(no_of_student, no_of_subjects);

displayClassSummary(highest_student, lowest_student, class_total, class_average);
