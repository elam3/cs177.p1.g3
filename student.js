var data = [10, 15, 8, 9, 5];


$(document).ready(function() {
	
	$("#submitbutton").click(function(){
		submitButton();
	});


});

function submitButton() {
	console.log("function called");
	var input = $('input[name="choice"]:checked').val();


	// var input = document.getElementsByName("choice");

	// var output;
	// for (var i = 0; i < input.length; i++) {
	// 	console.log(input[i]);
	// 	if (input[i].checked) {
	// 		console.log(input[i]);
	// 		output = input[i].value;
	// 		break;
	// 	}
	// }
	console.log(input);

}