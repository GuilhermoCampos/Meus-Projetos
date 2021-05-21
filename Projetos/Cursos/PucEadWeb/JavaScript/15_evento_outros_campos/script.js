window.onload = function() {
    nome.onchange = () => console.log('change', nome.value);;
    salada.onchange = () => console.log(salada.value);
    molho1.onchange = () => console.log(molho1.value);
    molho2.onchange = () => console.log(molho2.checked);
    molho3.onchange = () => console.log(molho3.checked);
    pao.onchange = () => console.log(pao.value);
    sobremesa.onchange = () => console.log(sobremesa.value);

}