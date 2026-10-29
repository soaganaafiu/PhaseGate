function reverse(numbers) {

    for (let index = 0; index < Math.floor(numbers.length / 2); index++) {

        let container = numbers[index];

        numbers[index] = numbers[numbers.length - index - 1];

        numbers[numbers.length - index - 1] = container;

    }

    return numbers;
}











function reverseArray(matrix) {

    for (let index = 0; index < matrix.length; index++) {

        reverse(matrix[index]);

    }

    return matrix;
}











const numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

const answer = reverseArray(numbers);


for (let index = 0; index < answer.length; index++) {

    let line = "";

    for (let count = 0; count < answer[index].length; count++) {

        line += answer[index][count];

    }

    console.log(line);
}
