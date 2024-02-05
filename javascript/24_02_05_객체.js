// 객체의 형태
const babaYaga = {
    name: "John Wick",
    age: 53,
    from: "벨라루스",
      askingHim(){
          console.log("Yeah, I'm thinking I'm back!");
      }
  };

// 객체에 접근(in)
console.log(`${babaYaga.name} from ${babaYaga.from}`);
console.log(`${babaYaga['name']} from ${babaYaga['from']}`);  

console.log('age' in babaYaga);
console.log('mercy' in babaYaga);

// 객체가 해당 프로퍼티를 가지고 있는지(hasOwnProperty)
const aespa = {
    members: ['카리나', '윈터', '지젤', '닝닝'],
    from: '광야',
      sing: function(){
          return "적대적인 고난과 슬픔은 널 더 popping 진화시켜!"
      }
  };
  
  console.log(aespa.hasOwnProperty('itzy'));
  console.log(aespa.hasOwnProperty('from'));

// for-in
// 주의할 점: 반드시 순서대로 반복되지 않음 
const person = {
    name: '재현',
    age: 20,
    gender: 'male'
  };
  
  for (let key in person) {
    console.log(`${key}: ${person[key]}`);
  }

// 속성 이름, 값을 배열로 반환
console.log(Object.keys(aespa));
console.log(Object.values(aespa));