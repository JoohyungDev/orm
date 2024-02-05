// 배열에도 메서드를 사용할 수 있다
const obj = {
    name: 'test'
  }
  
  console.log(obj.hasOwnProperty('name'));
  
  const arr = [1,2,3];
  
  console.log(arr.hasOwnProperty('name'));

// prototype
console.log(Array.prototype.__proto__ === Object.prototype);
console.log(Number.prototype.__proto__ === Object.prototype);
console.log(String.prototype.__proto__ === Object.prototype);
console.log(Math.__proto__ === Object.prototype);

// 상속
function Child() {
    Parent.call(this);
}

Child.prototype = Object.create(Parent.prototype); // 지정된 프로토타입 객체를 갖는 새 객체를 만듭니다.


Child.prototype.canWalk = function () {
    console.log('now i can walk!!');
}

// 프로토타입의 문법이 지저분 하다는 단점이 있어 클래스를 권장
