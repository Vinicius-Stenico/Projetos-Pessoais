<?php
include('php.ini');
    if(!isset($_SESSION['id'])) {
        header("Location: login.php");
    }
?>