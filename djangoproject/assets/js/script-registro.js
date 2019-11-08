var pass = document.getElementById("password1"),
  pass2 = document.getElementById("password2"),
  btnAceptar = document.getElementById("btn-aceptar-reg");

pass2.addEventListener("change", function( event ) {
	if(pass.value == pass2.value){
  	btnAceptar.disabled = false;
  }else{
  	btnAceptar.disabled = true;
  }
}, true);