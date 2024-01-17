// let div = document.querySelector("div")

// div.style.color = "blue"
// div.style.color = ""
// div.style.fontSize = "16"

let div = document.querySelector("div");
// let incluiClasse = div.classList.contains("borda-azul")

div.classList.add("texto-novo");
div.classList.remove("borda-azul");

div.classList.toggle("borda-azul")
div.classList.toggle("borda-azul")

let incluiClasse = div.classList.contains("texto-novo");

console.log(incluiClasse)