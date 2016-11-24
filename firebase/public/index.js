// var FirebaseServer = require('firebase-server');

// new FirebaseServer(5000, 'test.firebase.localhost', {
// });

// var client = new Firebase('ws://localhost.firebaseio.test:5000');
// client.on('value', function(snap) {
//     console.log('Got value: ', snap.val());
// });


$(document).ready(function(){
	var dialog = document.querySelector('dialog');
    dialogPolyfill.registerDialog(dialog);
     // dialog.showModal();
	$("#signInBtn").click(function(){
		var email = $("#email-si").val();
		var password = $("#password-si").val();
		firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error){
			$("#loginError-si").show().text(error.message);
		});
	});

	$("#help").click(function() {
		window.location.href = 'help.html';

	});

	$("#signUpBtn").click(function(){
		var email = $("#email").val();
		var password = $("#password").val();
		var name = $("#name").val();
		var role = $('input[name="options"]:checked').val();
		console.log(role);
		firebase.auth().createUserWithEmailAndPassword(email, password).then(function(user){
			// console.log(user.uid);
			var newUser = firebase.database().ref().child("users").child(user.uid);
			newUser.update({
				name: name,
				email: email,
				role: role
			});
		}).catch(function(error) {
  			$("#loginError").show().text(error.message);
		});
	});
})


firebase.auth().onAuthStateChanged(function(user) {
  if (user) {

	  firebase.auth().currentUser.getToken(true).then(function(idToken) {

	  		firebase.database().ref('/users/' + user.uid + "/role").once('value').then(function(snapshot) {

  			var role = snapshot.val();
  			console.log(role);
  			 if (role == "Admin") {
  		 		window.location.href = 'admin.html'

  			} else if (role == "Student"){
  				window.location.href = 'student.html'

  			}
	  		
		}).catch(function(error) {
	  		console.log(error.message);
		}); 		
 
	});

  } else {
  	var dialog = document.querySelector("#accountSetUp");
  	  if (! dialog.showModal) {
      	dialogPolyfill.registerDialog(dialog);
      }
      dialog.showModal();

  }
});
