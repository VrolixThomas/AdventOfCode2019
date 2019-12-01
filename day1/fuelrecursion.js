const masses = require("fs")
  .readFileSync("fuel.txt", { encoding: "utf-8" })
  .split("\n")
  .map(input => Number(input));

var sum = 0;

function newFuelmass(mass) {
  newmass = (mass / 3).toFixed();
  if (newmass - mass / 3 > 0) {
    newmass--;
  }
  newmass -= 2;
  return newmass;
}

function combinedFuel(mass) {
  newmass = newFuelmass(mass);
  if (newmass <= 0) {
    return 0;
  } else {
    return newmass + combinedFuel(newmass);
  }
}

masses.forEach(mass => (sum += combinedFuel(mass)));
console.log(sum);
