const numbers = [2,4,6,8];
let doubledNumbers = [];

for (number in numbers){
    doubledNumbers.push(number* 2);

}
console.log(doubledNumbers);


// using map to do the same

const doubledNumbersMap = numbers.map(num => num * 2);
console.log(doubledNumbersMap);

// Using map with parameters
const numbersWithIndex = numbers.map((num, index, array) => {
    return {
        doubled : num * 2,
        original: num,
        index: index,
        array: array
    };
});

console.log(numbersWithIndex);

const users = [{
    name : 'Alice',
    age: 25
},{
    name : 'Bob',
    age: 30
}]

const userNames = users.map(user => user.name);
console.log(userNames);

const evenNumbersFilter = numbers.filter(num => num % 2 === 0);
console.log(evenNumbersFilter); // [2, 4]

let sum = 0;
for (number in numbers) {

    sum += number;

}

console.log(sum); 

const sumWithReduce = numbers.reduce((accumulator, currentValue) => {accumulator + currentValue}, 0);
console.log(sumWithReduce);//



const furit = [apple,banana,]