// 기본구조
for(초기화식; 조건식; 증감식) {
	실행문;
}

// 반복문 1
for(var i=0; i<10; i++){
    document.write(i, '<br>');
  }

// while문
while (조건식) {
    // 조건식이 참일 때 실행될 코드
  }

// while문 1
let num = 0;

while (num < 11) {
  document.write(num, '<br>');
  num += 1;
}

// do-while
let input;

do {
  input = prompt("숫자를 입력하세요.");
} while (isNaN(input));

console.log("입력한 숫자는 " + input + "입니다.");

