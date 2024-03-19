#!/usr/bin/node
const x = process.argv;
let a = 0;
if (parseInt(x[2])) {
  while (a < parseInt(x[2])) {
    console.log('C is fun');
    a++;
  }
} else {
  console.log('Missing number of occurrences');
}
