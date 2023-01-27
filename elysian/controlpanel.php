<?php
include('protect.php');
header("refresh: 1201");
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Elysian</title>
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="icon" type="image/x-icon" href="assets/img/favicon.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="assets/css/controlpanel.css">
  <link rel="stylesheet" href="assets/css/index.css">
</head>
<body>
<nav>
    <div class="menu">
      <div class="logo">
        <a href="panelindex.php">Elysian</a>
      </div>
      <ul>
        <li><a href="panelindex.php">Início</a></li>
        <li><a href="paneldownload.php">Download</a></li>
        <li><a href="saida.php">Sair</a></li>
      </ul>
    </div>
  </nav>
  <section class="main">
  <div class="profile-card">
    <div class="image">
      <img src="assets/img/profile.png" alt="" class="profile-pic">
    </div>
    <div class="data">
      <h2>USER</h2>
      <span>GAMER PARA SEMPRE!</span>
    </div>
    <div class="buttons">
      <a href="#" class="btn">BAIXAR SAVE</a>
    </div>
  </div>
</section>
</body>
</html>
