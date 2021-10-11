function up() {
	$.post("GPIO.php", {
		cmd: "up"
	}).done(function (data) {
		$("#up").css("background-color", "#96fd96");
		$("#down").css("background-color", "white");
	});
}

function down() {
	$.post("GPIO.php", {
		cmd: "down"
	}).done(function (data) {
		$("#down").css("background-color", "red");
		$("#up").css("background-color", "white");
	});
}
$(document).ready(function () {
	$(".isgpio").on('click', function () {
		jQuery(".isgpio").children(".circle").removeClass("selectedgpio");
		if (!jQuery(this).children(".circle").hasClass("selectedgpio")) {
			jQuery(this).children(".circle").addClass("selectedgpio");
			var gpio = jQuery(this).attr('id');
			update(gpio);
		}
	});

	$("#reboot").on('click', function () {
		$("#cbox").show();

	});
	$(document).click(function (e) {
		var cbox = $("#cbox");

		var target = e.target;

		if (!$("#reboot").is(target) && $("#reboot").has(e.target).length === 0) {
			if (!cbox.is(target) && cbox.has(e.target).length === 0) {
				cbox.hide();
			}
		}
	});
	$("#training").on('click', function () {
		window.location.replace("/training.php");
	});
	$("#home").on('click', function () {
		window.location.replace("/index.php");
	});
	$("#reboot_yes").on('click', function () {
		$.post("controls.php", {
			cmd: "reboot"
		}).done(function (data) {

		});
	});
	$("#reboot_no").on('click', function () {
		var cbox = $("#cbox");
		cbox.hide();
	});
	$('input[type=radio][name="inout"]').change(function () {
		setinout(jQuery("#gpioholder").text(), this.value);
		update(jQuery("#gpioholder").text());
	});
	$('input[type=radio][name="highlow"]').change(function () {
		sethighlow(jQuery("#gpioholder").text(), this.value);
		update(jQuery("#gpioholder").text());
	});

	function update(gpio) {
		$.post("conf.php", {
			cmd: "update",
			gpio: gpio
		}).done(function (data) {
			var a = JSON.parse(data);
			jQuery("#gpioholder").text(a[0]);
			jQuery("#levelholder").text(a[1]);
			jQuery("#fselholder").text(a[2]);
			jQuery("#funcholder").text(a[3]);
			jQuery("#pullholder").text(a[4]);
			jQuery("#functionsholder").text(a[5]);
			jQuery("#gpio" + a[0]).children(".circle").addClass("selectedgpio");
			if (a[1] == "1") {
				$("#high").prop("checked", true);
			} else {
				$("#low").prop("checked", true);
			}
			if (a[3] == "OUTPUT") {
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
		}).done(function (data) {});
	}

	function sethighlow(gpio, highlow) {
		$.post("conf.php", {
			cmd: "sethighlow",
			gpio: gpio,
			highlow: highlow
		}).done(function (data) {});
	}

	function gettemp() {
		$.post("conf.php", {
			cmd: "gettemp"
		}).done(function (data) {
			jQuery("#pitempholder").children("div").children("p").text(data);
		});
	}
	gettemp();
	update("gpio0");
	window.setInterval(gettemp, 2000) // every 2 seconds
});
