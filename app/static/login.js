var inputs = document.getElementsByClassName('caja');
var caja1 = document.getElementById('caja1');
var boton = document.getElementsByClassName('btn');

window.onload = UbicarPlaceHolder

for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('keyup', function(){
        if(this.value.length>=1){
            this.nextElementSibling.classList.add('fijar');
        }else{
            this.nextElementSibling.classList.remove('fijar');
        }   
    });
} 

function UbicarPlaceHolder(){
    
    for (var i = 0; i < inputs.length; i++) {
                //.replace(/ /g, "") elimina los espacios del input, pero el select no funciona así
        if(inputs[i].value.length>=1){
            inputs[i].nextElementSibling.classList.add('fijar');
        }else{
            inputs[i].nextElementSibling.classList.remove('fijar');
        }
}
};
