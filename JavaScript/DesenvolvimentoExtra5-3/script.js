produto = {
    nome: "Notebook Acer Aspire 5 A515-54-33EN",
    descricao: "Notebook Acer Aspire 5 A515-54-33EN, com processador Intel Core i3 de decima geração, acompanhado de um armazenamento de 256GB SSD NVMe x4 podendo fazer upgrades de ate 2TB, Junto de uma memoria RAM de 4GB DDR4 Expansível de ate 16GB, tendo uma tela de 15.6 polegadas com resolução FULL HD (1920 x 1080), sendo seu sistema operacional Windows 11 home 64-bits",
    preco: 1799.02
};

let BodyHtml = document.querySelector("body")

let headerTag = document.createElement("header")
let tituloTag = document.createElement("h1")
let mainTag = document.createElement("main")
let sectionTag = document.createElement("section")

BodyHtml.appendChild(headerTag)
headerTag.appendChild(tituloTag)

BodyHtml.appendChild(mainTag)
mainTag.appendChild(sectionTag)

tituloTag.id = 'titulo'

tituloTag.innerHTML =`
Bem vindo ao JavaScript Shop!
`
sectionTag.innerHTML=`
<h3>${produto.nome}</h3>
<div>
    <img src="https://www.saldaodainformatica.com.br/10012-medium_default/notebook-acer-aspire-5-a515-54-33en-intel-core-i3-10110u-armazenamento-256gb-ssd-nvme-x4-tela-156-windows-11.webp"></img>
    <p>${produto.descricao}</p>
    <p>R$ ${produto.preco}</p>
<div>
`
console.log(BodyHtml)