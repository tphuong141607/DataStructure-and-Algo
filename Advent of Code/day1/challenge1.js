const fs = require("fs");
const util = require("util");

const readFile = util.promisify(fs.readFile);

// This function will return a promise
const getInput = () => readFile("./input_challenge.txt", "utf8");

const countIncrease = async () => {
  const input = await getInput();
  const arrInput = input.split("\n");
  let countInc = 0;

  for (let i = 0; i <= arrInput.length; i++) {
    if (+arrInput[i + 1] - +arrInput[i] > 0) countInc += 1;
  }

  return countInc;
};

countIncrease().then((data) => {
  console.log(data);
});
