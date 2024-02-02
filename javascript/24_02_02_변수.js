// 함수 scope 정의
function main() {
    var x = 'hi';
}

console.log(x);

// 함수 scope 예시 2
function main() {
    var x = 'hello'
    if (true) {
        var x = 'hi';
    }
    console.log(x); // 'hello'
}

main();

// 블록 scope 정의
// var는 함수 scope를 갖기에 x가 정상 출력된다!
function main() {
    if (true) {
        var x = 'hi';
    }
    console.log(x); // 'hi'
}

main();

// var->let
function main() {
    if (true) {
        let x = 'hi';
    }
    console.log(x); // 'hi'
}

main();

// 호이스팅
console.log(num);

var num = 10;

console.log(num);

// 호이스팅 let
console.log(num);

let num = 10;

console.log(num);

