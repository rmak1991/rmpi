<?php
$cmd = $_POST["cmd"];
if($cmd=="update"){
	 $gpio = $_POST["gpio"];
	 $gpio_num = str_replace("gpio","",$gpio);
	 $attr=  exec("sudo raspi-gpio get $gpio_num");
	 $functions =  exec("sudo raspi-gpio funcs $gpio_num");
	 $explode = explode(" ",$attr);
	 
	 $array = array(str_replace(":","",$explode[1]),str_replace("level=","",$explode[2]),str_replace("fsel=","",$explode[3]),str_replace("func=","",$explode[4]),str_replace("pull=","",$explode[5]),$functions);
     echo json_encode($array);
}	
if($cmd=="setinout"){
	$gpio = $_POST["gpio"];
	$inout = $_POST["inout"];
    $gpio_num = str_replace("gpio","",$gpio);
	if($inout=="input"){
	 exec("sudo raspi-gpio set $gpio_num ip");
	}
	elseif($inout=="output"){
     exec("sudo raspi-gpio set $gpio_num op");		
		}
	}
if($cmd=="sethighlow"){
	$gpio = $_POST["gpio"];
	$highlow = $_POST["highlow"];
    $gpio_num = str_replace("gpio","",$gpio);
	if($highlow=="high"){
	 exec("sudo raspi-gpio set $gpio_num dh");
	}
	elseif($highlow=="low"){
     exec("sudo raspi-gpio set $gpio_num dl");		
		}
	}	
if($cmd=="gettemp"){
	echo     $gpio_num = str_replace("temp=","",exec("sudo vcgencmd measure_temp"));
	}
?>
