<?php
$cmd = $_POST["cmd"];
if($cmd =="up"){
	exec("sudo raspi-gpio set 18 dh");
	}
elseif($cmd=="down"){
	exec("sudo raspi-gpio set 18 dl");
	}	
?>
