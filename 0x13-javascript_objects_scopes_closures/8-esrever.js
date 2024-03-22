#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [];
  for (let b = 0; b < list.length; b++) {
    temp.push(list[(list.length - (b + 1))]);
  }
  return temp;
};
