<html>

<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script>
	function up() {
		$.post("GPIO.php", {
			cmd: "up"
		}).done(function(data) {
			$("#up").css("background-color", "#96fd96");
			$("#down").css("background-color", "white");
		});
	}

	function down() {
		$.post("GPIO.php", {
			cmd: "down"
		}).done(function(data) {
			$("#down").css("background-color", "red");
			$("#up").css("background-color", "white");
		});
	}
	$(document).ready(function() {
		$(".isgpio").on('click', function() {
			jQuery(".isgpio").children(".circle").removeClass("selectedgpio");
			if(!jQuery(this).children(".circle").hasClass("selectedgpio")) {
				jQuery(this).children(".circle").addClass("selectedgpio");
				var gpio = jQuery(this).attr('id');
				update(gpio);
			}
		});
		$('input[type=radio][name="inout"]').change(function() {
			setinout(jQuery("#gpioholder").text(), this.value);
			update(jQuery("#gpioholder").text());
		});
		$('input[type=radio][name="highlow"]').change(function() {
			sethighlow(jQuery("#gpioholder").text(), this.value);
			update(jQuery("#gpioholder").text());
		});

		function update(gpio) {
			$.post("conf.php", {
				cmd: "update",
				gpio: gpio
			}).done(function(data) {
				var a = JSON.parse(data);
				jQuery("#gpioholder").text(a[0]);
				jQuery("#levelholder").text(a[1]);
				jQuery("#fselholder").text(a[2]);
				jQuery("#funcholder").text(a[3]);
				jQuery("#pullholder").text(a[4]);
				jQuery("#functionsholder").text(a[5]);
				jQuery("#gpio" + a[0]).children(".circle").addClass("selectedgpio");
				if(a[1] == "1") {
					$("#high").prop("checked", true);
				} else {
					$("#low").prop("checked", true);
				}
				if(a[3] == "OUTPUT") {
					$("#output").prop("checked", true);
				} else {
					$("#input").prop("checked", true);
				}
			});
		}

		function setinout(gpio, inout) {
			$.post("conf.php", {
				cmd: "setinout",
				gpio: gpio,
				inout: inout
			}).done(function(data) {});
		}

		function sethighlow(gpio, highlow) {
			$.post("conf.php", {
				cmd: "sethighlow",
				gpio: gpio,
				highlow: highlow
			}).done(function(data) {});
		}
	function gettemp() {
			$.post("conf.php", {
				cmd: "gettemp"
			}).done(function(data) {
				jQuery("#pitempholder").children("div").children("p").text(data);
				});
		}
		gettemp();
		update("gpio0");
		window.setInterval(gettemp, 2000) // every 2 seconds
	});
	</script>
	<style>
	.box {
		height: 642px;
		width: 400px;
		border-style: solid;
		border-radius: 20px;
		margin-top: 30px;
		margin-left: 31px;
	}
	
	.row {
		border-radius: 20px;
		height: 30px;
		margin: 2px;
		display: flex;
		justify-content: space-between;
	}
		.inforow {
		border-radius: 20px;
		height: 30px;
		margin: 2px;
		display: flex;
	}
	.item1 {
		height: 30px;
		width: 120px;
		border-radius: 20px;
		display: flex;
		justify-content: flex-start;
		align-items: center;
	}
	
	.item2 {
		height: 30px;
		width: 120px;
		border-radius: 20px;
		display: flex;
		justify-content: flex-end;
		align-items: center;
	}
	
	.circle {
		cursor: pointer;
		width: 25px;
		height: 25px;
		border-style: solid;
		border-radius: 30px;
		border-width: 1px;
		background-color: white;
	}
	
	.item1 > .circle {
		margin-right: 5px;
	}
	
	.item2 > .circle {
		margin-left: 5px;
	}
	.infoitem{
		margin-left: 13px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 16px;
    font-family: sans-serif;
    width: 74px;
		}
	
	.text >p {
		margin: 0;
		font-family: sans-serif;
		font-size: 14px;
	}
	
	.isgpio {
		background-color: #ffd0d0;
		font-weight: bold;
	}
	
	.settings {
		height: 642px;
		width: 400px;
		border-style: solid;
		border-radius: 20px;
		margin-top: 30px;
		margin-left: 20px;
	}
	
	.container {
		display: flex;
		justify-content: center;
	}
	
	.title {
		border-top-left-radius: 20px;
		border-top-right-radius: 20px;
		box-shadow: 1px 1px 5px 0px black;
		height: 50px;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 16px;
		font-weight: bold;
		font-family: sans-serif;
	}
	
	.title > p {
		margin: 0;
	}
	
	.settings_contents {
		padding: 10px;
	}
	
	.settings_row {
		display: flex;
		height: 30px;
		margin-top: 2px;
	}
	
	.settings_item {
		margin-left: 13px;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 16px;
		font-family: sans-serif;
		width: 74px;
	}
	
	.settings_row >:first-child {
		justify-content: flex-end;
	}
	
	.functions {
		width: 280px;
		display: block;
		overflow-wrap: break-word;
		padding-top: 30px;
	}
	
	.control_item {}
	
	.controls {
		height: 75px;
		align-items: center;
		padding-left: 30px;
	}
	
	.controls >:first-child {
		margin-right: 30px;
	}
	
	.selectedgpio {
		background-color: blue;
	}
	body{
		user-select: none;
		}
		.info_content{
			padding:10px;
		}
	</style>
</head>

<body>
	<div class="container">
		<div class="box">
			<div class="row">
				<div class="item1">
					<div class="circle"></div>
					<div class="text">
						<p>3.3V</p>
					</div>
				</div>
				<div class="item2">
					<div class="text">
						<p>5V</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio2">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 2</p>
					</div>
				</div>
				<div class="item2">
					<div class="text">
						<p>5V</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio3">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 3</p>
					</div>
				</div>
				<div class="item2">
					<div class="text">
						<p>GND</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio4">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 4</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio14">
					<div class="text">
						<p>GPIO 14</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1">
					<div class="circle"></div>
					<div class="text">
						<p>GND</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio15">
					<div class="text">
						<p>GPIO 15</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio17">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 17</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio18">
					<div class="text">
						<p>GPIO 18</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio27">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 27</p>
					</div>
				</div>
				<div class="item2">
					<div class="text">
						<p>GND</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio22">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 22</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio23">
					<div class="text">
						<p>GPIO 23</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1">
					<div class="circle"></div>
					<div class="text">
						<p>3.3V</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio24">
					<div class="text">
						<p>GPIO 24</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio10">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 10</p>
					</div>
				</div>
				<div class="item2">
					<div class="text">
						<p>GND</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio9">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 9</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio25">
					<div class="text">
						<p>GPIO 25</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio11">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 11</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio8">
					<div class="text">
						<p>GPIO 8</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1">
					<div class="circle"></div>
					<div class="text">
						<p>GND</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio7">
					<div class="text">
						<p>GPIO 7</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio0">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 0</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio1">
					<div class="text">
						<p>GPIO 1</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio5">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 5</p>
					</div>
				</div>
				<div class="item2">
					<div class="text">
						<p>GND</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio6">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 6</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio12">
					<div class="text">
						<p>GPIO 12</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio13">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 13</p>
					</div>
				</div>
				<div class="item2">
					<div class="text">
						<p>GND</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio19">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 19</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio16">
					<div class="text">
						<p>GPIO 16</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1 isgpio" id="gpio26">
					<div class="circle"></div>
					<div class="text">
						<p>GPIO 26</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio20">
					<div class="text">
						<p>GPIO 20</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
			<div class="row">
				<div class="item1">
					<div class="circle"></div>
					<div class="text">
						<p>GND</p>
					</div>
				</div>
				<div class="item2 isgpio" id="gpio21">
					<div class="text">
						<p>GPIO 21</p>
					</div>
					<div class="circle"></div>
				</div>
			</div>
		</div>
		<div class="box">
			<div class="title">
				<p>GPIO Settings</p>
			</div>
			<div class="settings_contents">
				<div class="settings_row">
					<div class="settings_item"><span>GPIO :</span></div>
					<div class="settings_item"><span id="gpioholder"></span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>Level :</span></div>
					<div class="settings_item"><span id="levelholder"></span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>fsel :</span></div>
					<div class="settings_item"><span id="fselholder"></span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>func :</span></div>
					<div class="settings_item"><span id="funcholder"></span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>pull :</span></div>
					<div class="settings_item"><span id="pullholder"></span></div>
				</div>
				<div class="settings_row" style="height:100px;">
					<div class="settings_item"><span>functions :</span></div>
					<div class="settings_item functions"><span id="functionsholder"></span></div>
				</div>
				<div class="settings_row controls">
					<div class="control_item">
						<div>
							<input type="radio" id="input" name="inout" value="input">
							<label for="input">Input</label>
						</div>
						<div>
							<input type="radio" id="output" name="inout" value="output">
							<label for="output">Output</label>
						</div>
					</div>
					<div class="control_item">
						<div>
							<input type="radio" id="high" name="highlow" value="high">
							<label for="high">High</label>
						</div>
						<div>
							<input type="radio" id="low" name="highlow" value="low">
							<label for="low">Low</label>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="box">
			<div class="title">
				<p>PI Info</p>
			</div>
			<div class="info_content">
					<div class="inforow">
						<div class="infoitem" id="pitemp">
							<div class="text">
								<p>GPU Temp</p>
							</div>
						</div>
						<div class="infoitem" id="pitempholder">
							<div class="text">
								<p></p>
							</div>
						</div>
					</div>
			</div>		
		</div>
	</div>	
</body>

</html>
