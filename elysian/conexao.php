<?php
define('HOST', '127.0.0.1');
define('USUARIO', 'root');
define('SENHA', '');
define('DB', 'elysian');

$mysqli = new mysqli(HOST, USUARIO, SENHA, DB);

$conexao = mysqli_connect(HOST, USUARIO, SENHA, DB) or die('Não foi possivel conectar ao banco de dados');