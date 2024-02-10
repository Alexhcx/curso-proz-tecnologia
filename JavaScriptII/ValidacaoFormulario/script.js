//---------Funções gerais------------//
function togglePopUp(label,input){
    // Mostrar popup de campo obrigatorio
    input.addEventListener("focus", () =>{
        label.classlist.add("required-popu")
    })
}

