// 추상화
const me = {
    name : '한재현',
    address : '제주도 제주시 인다 1길',
    phoneNum : '010-8000-0000',
    canWalk : function(){
        console.log('재현이가 걷는다.');
    },
    teaching : function(student){
        student.levelUp();
    }
}

const student = {
    level: 1,
    levelUp : function(){
        this.level++;
    }
}

// 나의 예제
const me = {
    name : '박주형',
    address : '나의 집',
    phoneNum : '010-4000-0000',
    sleeping : function(){
        console.log('잠을 잔다.');
        sleep.fatigue_minus();
        console.log('현재 피로도는', sleep.fatigue);
        }
    }

    const sleep = {
    fatigue: 10,
    fatigue_minus : function(){
        this.fatigue--;
        },
    }

    console.log('현재 피로도는', sleep.fatigue);

// 생성자(new)
// 새로운 인스턴스 객체를 만듬
function NewFactory(name){
    this.name = name;
    this.sayYourName = function(){
        console.log(`삐리비리. 제 이름은 ${this.name}입니다. 주인님.`);
    }
}

robot1 = new NewFactory('로봇1')

// 예시 1
function Test(){};

const obj = new Test();

obj.__proto__ === Test.prototype