<html>
<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<link rel="stylesheet" href="css/layout.css">
	<script src="js/home.js"></script>
</head>

<body style="margin:0px;">
	<nav class="navbox">
		<div class="nav_row btm_ln">
		<div class="navitem logobox" id="home">
			<p>RMPI</p>
		</div>
		<div class="navitem">
			<div class="navitem_btn" id="reboot">
				<div class="btn_text">Reboot PI</div>
			</div>
			<div class="confirmbox" id="cbox" style="display: none;">
					<div class="cboxtitle"><p>Reboot PI?</p></div>
						<div class="cbox_contents">
							<div class="cbox_option"><button id="reboot_yes">Yes</button></div>
							<div class="cbox_option"><button id="reboot_no">No</button></div>
						</div>
			</div>
		</div>
				<div class="navitem">
			<div class="navitem_btn" id="training">
				<div class="btn_text">PI Training</div>
			</div>
		</div>
		</div>
		<div class="nav_row"></div>		
	</nav>
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
					<div class="circle selectedgpio"></div>
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
					<div class="settings_item"><span id="gpioholder">0</span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>Level :</span></div>
					<div class="settings_item"><span id="levelholder">1</span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>fsel :</span></div>
					<div class="settings_item"><span id="fselholder">0</span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>func :</span></div>
					<div class="settings_item"><span id="funcholder">INPUT</span></div>
				</div>
				<div class="settings_row">
					<div class="settings_item"><span>pull :</span></div>
					<div class="settings_item"><span id="pullholder">UP</span></div>
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
								<p>35.5'C</p>
							</div>
						</div>
					</div>
			</div>		
		</div>
	</div>	
</body></html>
