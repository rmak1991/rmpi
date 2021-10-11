<?php
$cmd = $_POST["cmd"];
$PATH= getcwd();
if($cmd=="inidb"){
	 $attr=  exec("sudo python3 $PATH/db.py");
     if($attr==NULL){
	   $filepath="flags/flg2.flg";
       $file =fopen($filepath,"w") or die("cannot open file");
       fwrite($file,"true");	 
       fclose($file);
       }
		echo $attr;  
}	 
?>
