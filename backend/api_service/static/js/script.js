// loader script
$(function () {	
	setTimeout(function () {
		$('.loader_bg').fadeToggle();
	}, 1500);
})

// footer date script

// Get the current year
var currentYear = new Date().getFullYear();

document.getElementById("current-year").textContent = currentYear;