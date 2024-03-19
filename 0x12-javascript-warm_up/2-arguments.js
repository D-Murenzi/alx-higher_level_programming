#!/usr/bin/node
const arg = process.argv;
const argv = arg.length - 2;
switch (argv) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
