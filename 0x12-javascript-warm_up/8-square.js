#!/usr/bin/node
const arg = process.argv;
const x = parseInt(arg[2]);
if (x) {
  for (let a = 0; a < x; a++) {
    const mes = 'X';
    console.log(mes.repeat(x));
  }
} else {
  console.log('Missing size');
}
