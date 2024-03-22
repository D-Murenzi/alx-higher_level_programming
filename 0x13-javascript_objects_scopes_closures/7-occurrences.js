exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let a = 0; a < list.length; a++) {
    if (searchElement === list[a]) {
      count++;
    }
  }
  return count;
};
