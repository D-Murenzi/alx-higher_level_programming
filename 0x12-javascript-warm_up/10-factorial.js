#!/usr/bin/node
const arg = process.argv;
function factorial (a) {
  if (a === 1 || a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const num = parseInt(arg[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
