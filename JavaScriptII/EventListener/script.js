let numero = document.querySelector("h1");
let botao = document.querySelector("button");

let contagem = 0;

// function adicionarUm(){
//     contagem += 1;
//     numero.innerText = contagem;
// }

// botao.addEventListener("click", adicionarUm)

// botao.addEventListener("click", function(){
//     contagem += 1;
//     numero.innerText = contagem;
// })

botao.addEventListener("click", ()=>{
    contagem += 1;
    numero.innerText = contagem;
})