<?php 
// check that data exists before using it
if (isset($_GET['colour'])){
    $colour = $_GET['colour'];


    echo "<h2>Form Results</h2>";
    echo "Your favourite colour is: ". htmlspecialchars($colour) . "<br>";
}
else {
    echo "No form data received.";
}
?>