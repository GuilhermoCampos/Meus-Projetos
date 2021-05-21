window.onload = function() {
    nome.onchange = () => console.log('change', nome.value);;

    nome.oninput = () => {
        console.log('input', nome.value.length);
        let charInvalid = '!@#$%^&*()<>,.;:=-+[]{}';
        let lastChar = nome.value.charAt(nome.value.length - 1);
        console.log('Ultimo Caráter', lastChar)
        if(charInvalid.indexOf(lastChar) >= 0){
            nome.value = nome.value.substr(0, nome.value.length - 1);
            nome.value.substr()
        }
    };

    nome.onfocus = () => {
        console.log("Nome recebeu foco")
        instrucao.innerHTML = 'Informe o seu nome';
        instrucao.style.color = '#999';
    };

    nome.onblur = () => {
        console.log("Nome perdeu foco")
        instrucao.innerHTML = '';
    }

}