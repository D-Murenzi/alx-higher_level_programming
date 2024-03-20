#!/usr/bin/node
const arg = process.argv;
const a = parseInt(arg[2]);
const b = parseInt(arg[3]);
function add (c, d) {
  return (a + b);
}
console.log(add(a, b));
