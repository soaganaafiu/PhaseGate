def reverse(numbers):

    for index in range(len(numbers) // 2):

        container = numbers[index]

        numbers[index] = numbers[len(numbers) - index - 1]

        numbers[len(numbers) - index - 1] = container


    return numbers








def reverse_array(matrix):

    for index in range(len(matrix)):

        reverse(matrix[index])

    return matrix











numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

answer = reverse_array(numbers)


for index in range(len(answer)):

    for count in range(len(answer[index])):

        print(answer[index][count], end="")

    print()


