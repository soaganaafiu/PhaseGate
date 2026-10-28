let numbers_one = [1, 2, 4];
let numbers_two = [1, 3, 4];

merged_array = []

for(let index = 0; index < numbers_one; index++){

    merged_array[index] = numbers_one[index];

}

for(let index = 0; index < numbers_two; index++){

    merged_array[numbers_one.length + index] = numbers_two[index];

}





for(let index = 0; index < merged_array.length; index++){

    for(let count = index + 1; count < merged_array.length; count++){

        if(merged_array[index] > merged_array[count]){

            let result = merged_array[index];

            merged_array[index] = merged_array[count];

            merged_array[count] = result;           

        }

    }
    
}

console.log(merged_array);
