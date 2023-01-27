<?php
    include('php.ini');
    include("conexao.php");

    $id = $_SESSION['id'];
    $nome = $_SESSION['nome'];
    $email = $_SESSION['email'];
    $sql = "INSERT INTO saidas (id, nome, email, data_saida) VALUES ('$id', '$nome', '$email', NOW())";
        if ($conexao->query($sql) === TRUE) {
            $_SESSION['status_saida'] = true;
        }
        
    $conexao->close();
    session_unset();
    session_destroy();

    header('Location: login.php');
exit;
?>