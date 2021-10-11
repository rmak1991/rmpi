<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<style>
	body{
		    font-family: sans-serif;
    margin: 0;
		}
.container{
	padding: 20px;
	}
.row{
    height: 60px;
    padding: 10px;
    box-shadow: 0px 0px 3px black;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
	}
.btn{
    background-color: transparent;
    border-style: solid;
    border-color: #528bff;
    border-radius: 15px;
    box-shadow: 0px 0px 5px #528bff;
    outline: none;
    height: 40px;	
    cursor:pointer;
	}
.btn:hover{
background-color: #528bff33;
color: #000000;	
	}
.message{
height: 85px;
    width: 50%;
    background-color: #f1f1f1;
    position: absolute;
    margin: auto;
    margin-top: 15px;
    top: 0;
    left: 0;
    right: 0;
    border-radius: 5px;
    box-shadow: 0px 0px 5px 0px #5a5555;
    display:none;
	}
.message >p{
	    margin: 5;
    overflow-wrap: break-word;
	
	}		
</style>
<script>
$(document).ready(function () {
	$("#inidb").on('click', function () {
		$.post("script.php", {
			cmd: "inidb"
		}).done(function (data) {
				showmsg(data);
		});
	});
	function showmsg(msg){
		$("#msgbox").children("p").text("ddd");
		$("#msgbox").show("slow");
		$("#msgbox").delay(1500).fadeOut(1000);
        $("#msgbox").children("p").text("");
     }
});


</script>
</head>

<body style="margin:0;">
<div class="container">
<div class="message" id="msgbox"><p></p></div>
<div class="row">
	
	<?php
$filepath="flags/flg2.flg";
$file =fopen($filepath,"r");
$line = fread($file,filesize($filepath));
if($line=="true" || $line=="true\n"){
echo 	"<button class=\"btn\" id=\"inidb\" disabled>Initialize Database</button>";
	}else{
echo "<button class=\"btn\" id=\"inidb\">Initialize Database</button>";		
		}
?>
</div>

</div>



</body>
</html>
