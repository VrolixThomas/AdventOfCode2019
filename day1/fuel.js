const masses = require("fs")
  .readFileSync("fuel.txt", { encoding: "utf-8" })
  .split("\n")
  .map(input => Number(input));

var sum = 0;
function combinedfuel(mass) {
  newmass = (mass / 3).toFixed();
  if (newmass - mass / 3 > 0) {
    newmass--;
  }
  sum += newmass - 2;
}

masses.forEach(mass => combinedfuel(mass));

console.log(sum);
