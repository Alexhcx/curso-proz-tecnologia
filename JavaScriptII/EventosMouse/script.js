let button = document.querySelector("button");
let span = document.querySelector("span");
let section = document.querySelector("section");

function mostrarSpan(){
    span.style.opacity = "100";
}

function ocultarSpan(){
    span.style.opacity ="0";
}

function fazerUmClick(){
    section.innerText = "Fez um click simples";
}

function fazerDoisClicks(){
    section.innerHTML = "Fez um duplo click!"
}

function esconderClick(){
    section.innerHTML = "texto dinamico"
}

button.addEventListener("click", fazerUmClick);
button.addEventListener("dblclick", fazerDoisClicks)

button.addEventListener("mouseover", mostrarSpan);
button.addEventListener("mouseout", ocultarSpan);
