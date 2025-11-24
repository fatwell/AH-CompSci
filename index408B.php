<?php 
// check that data exists before using it
if (isset($_POST['username']) && isset($_POST['password'])){
    $username = $_POST['username'];


    echo "<h2>Form Results</h2>";
    echo "Welcome ". htmlspecialchars($username) . "<br>";
}
else {
    echo "No form data received.";
}
?>