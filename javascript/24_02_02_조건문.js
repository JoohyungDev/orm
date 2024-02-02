// 기본 형태
if (조건식) {
    // 조건식이 참일 때 실행될 코드
  }

  
  let test=5;
  if(test < 10){
      //codes
  }

// if-else
let score = 69;
let money = 1000;

if (score > 90){
  document.write('참 잘했습니다!<br>');
  money += 100000
} else if (score > 80){
  document.write('잘했습니다!<br>');
  money += 10000
} else if (score > 70){
  document.write('했습니다!<br>');
  money += 1000
} else {
  money = 0
}

document.write(money);

// 삼항연산자
let item = true ? console.log('true') : console.log('false');
console.log(item);

// switch문
switch (표현식) {
    case 값1:
      // 값1에 대한 실행 코드
      break;
    case 값2:
      // 값2에 대한 실행 코드
      break;
    default:
      // 모든 case에 해당하지 않을 때 실행될 코드
      break;
  }

  