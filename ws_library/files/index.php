<html>
<?php
$filepath="lib/setup/flags/flg1.flg";
$file =fopen($filepath,"r");
$line = fread($file,filesize($filepath));
if($line=="false" || $line=="false\n"){
	header("Location: lib/setup/setup.php");
	}
?>
<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<link rel="stylesheet" href="css/layout.css">
	<script src="js/home.js"></script>
</head>

<body style="margin:0px;">
	<nav class="navbox">	
	</nav>
	<div class="container">
		<div class="row">
			<div class="item"></div>
			<div class="item"></div>
			<div class="item"></div>
			<div class="item"></div>
			<div class="item"></div>
			<div class="item"></div>
			<div class="item"></div>
			<div class="item"></div>
		</div>
	</div>	
</body>
</html>
