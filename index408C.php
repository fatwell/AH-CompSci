<?php 
// check that data exists before using it
if (isset($_POST['name'])  && isset($_POST['age']) && isset($_POST['fav_game']) && isset($_POST['comments'])){
    $name = $_POST['name'];
    $age = $_POST['age']
    $fav_game = $_POST['fav_game']
    $comments = $_POST['comments']

    echo "<h2>Form Results</h2> <br>";
    echo "Welcome ". htmlspecialchars($name) . "<br>";
    echo "Your age is ". htmlspecialchars($name) . "<br>";
    echo "Your favourite game is ". htmlspecialchars($name) . "<br>";
    echo "The comments you left where ". htmlspecialchars($name) . "<br>";
}
else {
    echo "No form data received.";
}
?>