<?php
$cmd = $_POST["cmd"];
if($cmd=="reboot"){
	 exec("sudo reboot");
}	

?>
