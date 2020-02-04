#!/usr/bin/node
const size = process.argv[2];
let r;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (r = 0; r < size; r++) {
    console.log('x'.repeat(size));
  }
}
