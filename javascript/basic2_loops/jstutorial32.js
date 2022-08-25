// rewrite the while loop as a for loop
var x = 9;
while (x >= 1) {
  console.log("hello " + x);
  x = x - 1;
}

console.log("Here's mine.")

for (var x = 9; x > 0; x--) {
  console.log("hello " + x);
}

// different?

for (var x = 9; x>=1; x--) {
  console.log("hello " + x);
}