let sValor = '0';
let novoNum = true;
let vAnt = 0;
let opPend = null;

const digito = (n) => {
    if(novoNum){
        sValor = ''+n;
        novoNum = false;
    }
    else sValor += n;

    atualizaVisor();
}

const virgula = () => {
    if(novoNum){
        sValor = '0,';
        novoNum = false;
    }
    else if (sValor.indexOf(',') == -1) sValor += ',';

    atualizaVisor();
}

const limpa = () => {
    novoNum = true;
    vAnt = 0;
    opPend = null;
    sValor = '0';
    atualizaVisor();
}

const operador = (op) => {
    calcula()
    vAnt = vAtual;
    opPend = op;
    novoNum = true;
}

const calcula = () => {
    if(opPend != null){
        let resultado;
        switch(opPend){
            case '+': resultado = vAnt + vAtual(); break;
            case '-': resultado = vAnt - vAtual(); break;
            case '*': resultado = vAnt * vAtual(); break;
            case '/': resultado = vAnt / vAtual(); break;
        }
        sValor = resultado.toString().replace('.', ',');
    }
    novoNum = true;
    opPend = null;
    vAnt = 0;
    atualizaVisor();
}

const vAtual = () => parseFloat(sValor.replace(',', '.'))

const atualizaVisor = () => {
    let [parteInt, parteDec] = sValor.split(',');
    let v = '';
    let c = 0;

    for(let i = parteInt.length-1; i>=0; i--){
        if(++c > 3){
            v = '.' + v;
            c = 1;
        }
        v = parteInt[i] + v;
    }
    v = v + (parteDec ? ',' + parteDec : '');
    document.querySelector('#display').innerText = v;
}



onload = () => {
    document.querySelector("#bt-7").onclick = () => digito(7);
    document.querySelector("#bt-8").onclick = () => digito(8);
    document.querySelector("#bt-9").onclick = () => digito(9);

    document.querySelector("#bt-divide").onclick = () => operador('/');

    document.querySelector("#bt-4").onclick = () => digito(4);
    document.querySelector("#bt-5").onclick = () => digito(5);
    document.querySelector("#bt-6").onclick = () => digito(6);

    document.querySelector("#bt-times").onclick = () => operador('*');

    document.querySelector("#bt-1").onclick = () => digito(1);
    document.querySelector("#bt-2").onclick = () => digito(2);
    document.querySelector("#bt-3").onclick = () => digito(3);

    document.querySelector("#bt-minus").onclick = () => operador('-');

    document.querySelector("#bt-0").onclick = () => digito(0);
    document.querySelector("#bt-comma").onclick = virgula;
    document.querySelector("#bt-plus").onclick = () => operador('+');

    document.querySelector("#bt-ac").onclick = limpa;
    document.querySelector("#bt-equal").onclick = calcula();

};

