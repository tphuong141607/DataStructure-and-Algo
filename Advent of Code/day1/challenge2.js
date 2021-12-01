const fs = require("fs");
const util = require("util");

const readFile = util.promisify(fs.readFile);

// This function will return a promise
const getInput = () => readFile("./input_challenge.txt", "utf8");

// Similar to challenge 1 but we count the sum of 3 consecutive numbers instead of itself.
const countIncrease = async () => {
  const input = await getInput();
  const arrInput = input.split("\n");
  let countInc = 0;
  let prevSum = 0;

  for (let i = 0; i < arrInput.length - 2; i++) {
    const newSum = +arrInput[i] + +arrInput[i + 1] + +arrInput[i + 2];
    if (newSum > prevSum && i !== 0) countInc += 1;
    prevSum = newSum;
  }

  return countInc;
};

countIncrease().then((data) => {
  console.log(data);
});
