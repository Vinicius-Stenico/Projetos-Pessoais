<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="icon" type="image/x-icon" href="assets/img/favicon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
    <link rel="stylesheet" href="assets/css/login.css">
    <title>Elysian</title>
<style>
    #mensagem {
        color: white;
    }
    .valid {
        color: #aa40f4;
    }
    .valid:before {
        position: relative;
        left: -1px;
        content: "✔";
    }
    .invalid {
        color: #333;
    }
    .invalid:before {
        position: relative;
        left: -1px;
        color: #aa40f4;
        content: "X";
    }   
</style>
</head>
<body>
    <div class="container">
        <div class="forms">
            <div class="form login">
                <span class="title">Login</span>
                <span style="float: right;" class="title"><a style="text-decoration: none; color:#aa40f4; " href="index.php">Início</a></span>
                <form method="post" action="entrar.php" autocomplete="off">
                    <div class="input-field">
                        <input name="email" type="email" placeholder="Coloque seu email" pattern=".{10,60}" required>
                        <i class="uil uil-envelope icon"></i>
                    </div>
                    <div class="input-field">
                        <input name="senha" type="password" class="password" placeholder="Coloque sua senha" pattern="^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$])[a-zA-Z0-9@#$]{8,50}$" required>
                        <i class="uil uil-lock icon"></i>
                        <i class="uil uil-eye-slash showHidePw"></i>
                    </div>

                    <div class="checkbox-text">
                        <div class="checkbox-content">
                            <input type="checkbox" id="logCheck">
                            <label for="logCheck" class="text">Lembre de mim</label>
                        </div>
                    </div>

                    <div class="input-field button">
                        <input type="submit" value="Login">
                    </div>
                </form>

                <div class="login-signup">
                    <span class="text">Não tem conta?
                        <a  class="text signup-link">Registrar Agora</a>
                    </span>
                </div>
            </div>

            <div class="form signup">
                <span class="title">Registrar</span>
                <span style="float: right;" class="title"><a style="text-decoration: none; color:#aa40f4; " href="index.php">Início</a></span>
                <form method="post" action="cadastro.php" autocomplete="off">
                    <div class="input-field">
                        <input name="nome" pattern=".{4,20}"type="text" placeholder="Coloque seu apelido" required>
                        <i class="uil uil-user"></i>
                    </div>
                    <div class="input-field">
                        <input name="email" type="email" placeholder="Coloque seu email" pattern=".{10,60}" required>
                        <i class="uil uil-envelope icon"></i>
                    </div>
                    <div class="input-field">
                        <input name="senha" id="InputPassword" type="password" class="password" placeholder="Crie uma senha" pattern="^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$])[a-zA-Z0-9@#$]{8,50}$" required>
                        <i class="uil uil-lock icon"></i>
                        <i class="uil uil-eye-slash showHidePw"></i>
                    </div>
                    <div id="mensagem">
                        <p id="letra">Uma letra minúscula</p>
                        <p id="maiuscula">Uma letra maiúscula</p>
                        <p id="numero">Um número</p>
                        <p id="caracteres">8 caracteres</p>
                        <p id="carespercial">1 caractere especial</p>
                    </div>
                    <div class="input-field button">
                        <input type="submit" value="Inscrever-se">
                    </div>
                </form>

                <div class="login-signup">
                    <span class="text">Já tem conta?
                        <a class="text login-link">Entrar Agora</a>
                    </span>
                </div>
            </div>
        </div>
    </div>
    <script src="assets/js/login.js"></script>
    <script>
        var myInput = document.getElementById("InputPassword");
        var letra = document.getElementById("letra");
        var maiuscula = document.getElementById("maiuscula");
        var numero = document.getElementById("numero");
        var caracteres = document.getElementById("caracteres");
	    var special = document.getElementById("carespercial")
        myInput.onfocus = function(){
            document.getElementById("mensagem").style.display = "block";
        }
        myInput.onblur = function(){
          document.getElementById("mensagem").style.display = "block";
        }
        myInput.onkeyup = function() {
          var lowerCaseLetters = /[a-z]/g;
          if(myInput.value.match(lowerCaseLetters)) {
          letra.classList.remove("invalid");
    	  letra.classList.add("valid");
          } else {
          letra.classList.remove("valid");
          letra.classList.add("invalid");
          }
	      var upperCaseLetters = /[A-Z]/g;
  	      if(myInput.value.match(upperCaseLetters)) {  
    	    maiuscula.classList.remove("invalid");
    	    maiuscula.classList.add("valid");
  	      } else {
    	    maiuscula.classList.remove("valid");
    	    maiuscula.classList.add("invalid");
  	      }
          var numbers = /[0-9]/g;
          if(myInput.value.match(numbers)) {  
            numero.classList.remove("invalid");
            numero.classList.add("valid");
          } else {
              numero.classList.remove("valid");
              numero.classList.add("invalid");
            }
          
          if(myInput.value.length >= 8) {
            caracteres.classList.remove("invalid");
            caracteres.classList.add("valid");
            } else {
              caracteres.classList.remove("valid");
              caracteres.classList.add("invalid");
            }
          var specials = /\W|_/;
          if(myInput.value.match(specials)) {
              special.classList.remove("invalid");
              special.classList.add("valid");
            } else {
              special.classList.remove("valid");
              special.classList.add("invalid");
            }
          }
    </script>
</body>
</html>
