let n = '12';
console.log(typeof n);

let a, b;
a = 2;
b = --a * 2;
console.log(a, b);

a = 2;
b = a-- * 2;
console.log(a, b);

a = 2;
b = ++a * 2;
console.log(a, b);


a = 2;
b = a++ * 2;
console.log(a, b);

let nome = 'jose';
let sobrenome = 'Prereira';
console.log(nome + ' ' + sobrenome);

a = '5' + 2;
console.log(`a = ${a} do tipo ${typeof a}`)
b = +'5' + 2;
console.log(`b = ${b} do tipo ${typeof b}`)
let c = '5'-2;
console.log(`c = ${c} do tipo ${typeof c}`)
let d = 5 + '2';
console.log(`d = ${d} do tipo ${typeof d}`)
let e = 5 - '2';
console.log(`e = ${e} do tipo ${typeof e}`)
let f = 5 + 2 + '2';
console.log(`f = ${f} do tipo ${typeof f}`)
let g = 5 + '2' + 2;
console.log(`g = ${g} do tipo ${typeof g}`)
let h = +(5 + '2') + 2;
console.log(`h = ${h} do tipo ${typeof h}`)
let i = '5' / '2';
console.log(`i = ${i} do tipo ${typeof i}`)