// 원시타입
let str1 = 'hello';
let str2 = str1;
console.log(str2); // 'hello'

str1 = 'world';
console.log(str2); // str2에 할당된 값은 여전히 'hello' 입니다.

// 객체타입
let arr1 = [1, 2, 3];
let arr2 = arr1;
console.log(arr2); // [1, 2, 3]

arr1[0] = 10;
// arr1 = [10, 20];
console.log(arr2); // [10, 2, 3]

// 비교해보세요.
let value1 = 10;
let value2 = value1;
console.log(value2); // 10

value1 = 20;
console.log(value2); // 10

