<?php 
// check that data exists before using it
if (isset($_GET['search_term'])  && isset($_GET['category'])){
    $search_term = $_GET['search_term'];
    $category = $_GET['categroy']


    echo "<h2>Form Results</h2> <br>";
    echo "Searching for". htmlspecialchars($name) . " in the category of". htmlspecialchars($category) "<br>";
}
else {
    echo "No form data received.";
}
?>