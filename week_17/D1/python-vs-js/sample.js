// Ternary Operators
let pythonRules = true;
// pythonRules ? console.log("python really rules") : print("python still rules");

// if conditionals
// if (pythonRules) {
//   console.log("i'm already tired of typing");
// } else {
//   console.log("some words");
// }

// multiline comments

/* 
 this is a multiline
 comment
*/

// Random numbers

let teachers = ["Andrew", "David", "Krishna"];
let randomIdx = Math.floor(Math.random() * teachers.length);
// console.log(randomIdx);
// console.log(teachers[randomIdx]);

// get input from a user

// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });
//
// rl.question("What is your name, friend? ", (ans) => {
//   console.log(`Welcome to module 6 ${ans}. I hope you like snakes!`);
//   rl.close();
// });

// filter method and fat arrow syntax
let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let odds = nums.filter((x) => x % 2 !== 0);
// console.log(odds);

// classes
class Student {
  constructor(name, pythonKnowledge) {
    this.name = name;
    this.pythonKnowledge = pythonKnowledge;
  }
  getStudentInfo() {
    return `${this.name} knows ${this.pythonKnowledge} about python!`;
  }
}

const teagan = new Student((name = "Teagan"), (pythonKnowledge = "jack"));
console.log(teagan.getStudentInfo());

app.get("/", (req, res) => {
  res.send("<h1>Welcome to my express app!!!!!</h1>");
});
