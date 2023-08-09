let numeros = [2,5,6,34,12,433,432,12,43]

function buscar_valor(lista, objetivo){
    for(let i = 0; i<lista.length; i++){
        if(lista[i] == objetivo){
            return i;
        }
      return -1;
    }
}