<?php
$host = 'localhost';
$username = 'your_username';
$password = 'your_password';
$database = 'your_database';

// Create a database connection
$connection = mysqli_connect($host, $username, $password, $database);

// Check the connection
if (!$connection) {
    die("Connection failed: " . mysqli_connect_error());
}

// Collect form data
$name = mysqli_real_escape_string($connection, $_POST['name']);
$email = mysqli_real_escape_string($connection, $_POST['email']);
$phone = mysqli_real_escape_string($connection, $_POST['phone']);

// SQL query to insert data into the database
$sql = "INSERT INTO contacts (name, email, phone) VALUES ('$name', '$email', '$phone')";

// Execute the query
if (mysqli_query($connection, $sql)) {
    echo "Data inserted successfully!";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($connection);
}

// Close the database connection
mysqli_close($connection);
?>
