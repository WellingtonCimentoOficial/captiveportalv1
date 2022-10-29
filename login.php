<?php
$password1 = $_POST["password1"];
$password2 = $_POST["password2"];
$db = fopen("passwords.txt", "a");

if ($password1 == $password2){
        echo $password1;
        fwrite($db, "Senha: " . $password1 . "\n");
        fclose($db);
        http_response_code(200);
}else{
        http_response_code(400);
}

?>