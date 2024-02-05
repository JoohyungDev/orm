// 프로토타입 대신 사용하는 클래스
class Robot {
    // 클래스의 생성자 함수입니다. 하나의 클래스는 하나의 생성자만 정의할 수 있습니다. 
        // 그리고 생성자 함수는 new 키워드가 호출될때 자동으로 실행됩니다.
    constructor(name) {
        this.name = name;
    }

    // 메소드를 정의합니다. 메소드는 클래스가 생성한 인스턴스를 통해 사용할 수 있습니다.
    sayYourName() {
        console.log(`삐리비리. 제 이름은 ${this.name}입니다. 주인님.`);
    }
}

const robot = new Robot();

// 클래스, 상속
class BabyRobot extends Robot {
    constructor(name) {
        super(name);
        this.ownName = '아이크';
    }

    sayBabyName() {
                // 또한 상속을 받게되면 부모 클래스의 메소드를 사용할 수 있게 됩니다. 때문에 this로 접근 할 수 있습니다.
        this.sayYourName();
        console.log('Suceeding you, Father!');
    }
}

const baby = new BabyRobot('브랜든');

// 부모의 메서드명과 상속받은자식의 메서드명이 같으면 자식의 함수를 실행
// 오버라이딩처럼 동작!