const { input } = require("./inputs");
const path = require("path");
const fs = require("fs");

const { rocks, pattern } = input;
const placedRocks = new Set();

const checkCollision = (rock) => {
  for (let piece of rock) {
    if (placedRocks.has(`${piece.x},${piece.y}`)) return "ROCK";
    if (piece.y <= 0) return "FLOOR";
    if (piece.x <= 0 || piece.x >= 8) return "WALL";
  }
  return false;
};

const updatePosition = (rock, tallestPoint) => {
  rock.forEach((piece) => {
    piece.y += tallestPoint + 4;
    piece.x += 3;
  });
  return rock;
};

const findTallestPoint = (rock, tallestPoint) => {
  for (let piece of rock) {
    tallestPoint = Math.max(tallestPoint, piece.y);
  }
  return tallestPoint;
};

let remainingPattern = [...pattern];
let tallestPoint = 0;
for (let i = 0; i < 2022; i++) {
  let rocksCopy = JSON.parse(JSON.stringify(rocks));

  let rock = rocksCopy[i % rocks.length];
  rock = updatePosition(rock, tallestPoint);

  let dropDown = false;
  while (true) {
    if (dropDown) {
      rock.forEach((piece) => {
        piece.y -= 1;
      });
      let CollisionResult = checkCollision(rock);
      if (CollisionResult === "ROCK" || CollisionResult === "FLOOR") {
        // Don't fall, place instead
        rock.forEach((piece) => {
          piece.y += 1;
          placedRocks.add(`${piece.x},${piece.y}`);
        });
        tallestPoint = findTallestPoint(rock, tallestPoint);
        break;
      }
    } else {
      let Wind = remainingPattern.shift() === ">" ? 1 : -1;
      if (remainingPattern.length === 0) remainingPattern = [...pattern];
      rock.forEach((piece) => {
        piece.x += Wind;
      });
      let CollisionResult = checkCollision(rock);
      if (CollisionResult === "ROCK" || CollisionResult === "WALL") {
        // Revert the move
        rock.forEach((piece) => {
          piece.x -= Wind;
        });
      }
    }
    dropDown = ! dropDown;
  }
}

console.log(tallestPoint);