// this
// this의 대상은 호출되는 위치에 따라 다르다!
function a(){ console.log(this) }
a();

let myObj = {
    val1: 100,
    func1: function () {
        console.log(this);
    }
}

let test = myObj.func1;
test()

// this 예제 1
let myObj = {
    val1: 100,
    func1: function () {
        console.log(this);
    },
};

let test = myObj.func1;

let button1 = document.getElementById("btn1");
button1.addEventListener("click", myObj.func1);
let button2 = document.getElementById("btn2");
button2.addEventListener("click", test);

// this 예제 2
function sayName(){
  console.log(this.name);
}

var name = 'Hero'; 
// 전역으로 선언한 name 변수의 앞에는 window 가 생략되어 있습니다. 
// 때문에 window.name === "Hero" 가 성립합니다.
let peter = {
  name : 'Peter Parker',
  sayName : sayName
}

let bruce = {
  name : 'Bruce Wayne',
  sayName : sayName
}

sayName();
peter.sayName(); 
bruce.sayName();

/* sayName() 함수를 실행했을 때와 
peter, bruce 객체의 sayName 함수를 호출했을 때의 결과를 비교해 보세요 */

// 예제 3
let 호텔 = [{
    '이름' : '하나호텔',
    '위치' : '제주도 제주시 001',
    '가격' : {'A':50000, 'B':30000, 'C':15000},
    '방의개수' : 50,
    '예약자수' : 25,
    '남은방의개수' : function(){return this.방의개수 - this.예약자수}
  },{
    '이름' : '둘호텔',
    '위치' : '제주도 제주시 002',
    '가격' : {'A':100000, 'B':60000, 'C':30000},
    '방의개수' : 100,
    '예약자수' : 30,
    '남은방의개수' : function(){return this.방의개수 - this.예약자수}
  },{
    '이름' : '셋호텔',
    '위치' : '제주도 제주시 003',
    '가격' : {'A':80000, 'B':50000, 'C':30000},
    '방의개수' : 120,
    '예약자수' : 80,
    '남은방의개수' : function(){return this.방의개수 - this.예약자수}
  }];
  console.log(호텔[0].남은방의개수());
  console.log(호텔[1].남은방의개수());
  console.log(호텔[2].남은방의개수());

// 예제 4
// this는 함수가 만들어질 때가 아닌 실행될 때 그 값이 결정
// peter는 실행이 안되있고 실행 자체는 bruce객체에서 실행되었기에
// bruce가 찍힘
function sayName(){
    console.log(this.name);
  }
  var name = 'Hero';
  
  let peter = {
    name : 'Peter Parker',
    sayName : sayName
  };
  
  let bruce = {
    name : 'Bruce Wayne',
    sayName : peter.sayName
  };
  
  bruce.sayName(); // Bruce Wayne


