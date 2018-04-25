<!DOCTYPE html>
<html>
<head>
  <title>Table with database</title>
</head>
<body>
<table>
  <tr>
    <th>Teacher</th>
    <th>Instrument</th>
    <th>Date</th>
    <th>Time</th>
    <th>Room</th>
  </tr>
  <?php
  $conn = mysqli_connect("localhost", "root", "ifb299", "music_school");
  if ($conn-> connect_error) {
    die("Connection failed:". $conn-> connect_error);
  }

  $sql = "SELECT Teacher, Instrument, Date, Time, Room from music_app_bookings";
  $result = $conn-> query($sql);

  if ($result-> num_rows > 0){
    while ($row = $result-> fetch_assoc()){
      echo "<tr><td>". $row["Teacher"] ."</td><td>". $row["Instrument"] ."</td><td>". $row["Date"] ."</td><td>". $row["Time"] ."</td><td>". $row["Room"] ."</td><tr>";
    }
  echo "</table>";
  }
  else {
    echo "0 Result";
  }

  $conn-> close();
  ?>
</table>
</body>
</html>