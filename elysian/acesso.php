<?php
    include('php.ini');
    include("conexao.php");

    $id = $_SESSION['id'];
    $nome = $_SESSION['nome'];
    $email = $_SESSION['email'];
    $sql = "INSERT INTO acessos (id, nome, email, data_acesso) VALUES ('$id', '$nome', '$email', NOW())";
        if ($conexao->query($sql) === TRUE) {
            $_SESSION['status_acesso'] = true;
        }
        
    $conexao->close();
    header('Location: controlpanel.php');
exit;
?>