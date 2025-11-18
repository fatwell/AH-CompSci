<?php
$servername = "localhost";
$database = "volcanoes";
$username = "root";
$password = "";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully<br/>";

$sql = "SELECT country, COUNT(*) as no_volcanoes FROM volcanoes GROUP BY Country HAVING no_volcanoes > 100;";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
	echo $result->num_rows . " records in the database.";
} else {
	echo "0 results";
}

$conn->close();
?>