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

$sql ="SELECT * FROM volcanoes WHERE Country = 'Italy';";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  echo "<table>";
   while($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>id: " . $row["Volcano_ID"] . "</td>";
    echo "<td>Name: " . $row["Name"] . "</td>";
    echo "<td>Country: " . $row["Country"]. "</td>";
    echo "</tr>";
  }
  echo "</table>";
} else {
	echo "0 results";
}

$conn->close();
?>