var pass = document.getElementById("password1"),
  pass2 = document.getElementById("password2"),
  btnAceptar = document.getElementById("btn-aceptar-reg"),
  mensaje = document.getElementById("mensaje-pass");

var validPass = function(){
  if(pass.value == pass2.value){
    btnAceptar.disabled = false;
    mensaje.hidden = true;
  }else{
    btnAceptar.disabled = true;
    mensaje.hidden = false;
  }
}
pass2.addEventListener("change", function( event ) {
	validPass();
}, true);