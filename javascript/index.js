// const fruit = {
//   name: "apple",
//   color: ["red", "green"],
//   used_in: () => "Apples are used in juice and cocktails!"
// }
// console.log(fruit.name)
// console.log(fruit.color)
// console.log(fruit.color[0])
// console.log(fruit.used_in())

var fruit = {
  name: "apple",
  color: ["red", "green"]
}

fruit = JSON.stringify(fruit)
fruit = JSON.parse(fruit)
console.log(fruit.name)
console.log(fruit.color[0])