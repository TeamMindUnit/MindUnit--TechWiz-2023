// for bootStrap popover
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

// passGen
var alphaLowercase = "abcdefghijklmnopqrstuvwxyz".split("");
var alphaUppercase = "ABCDEFGHIJKLMNOPWRSTUVWXYZ".split("");
var alphaNumbers = "0123456789".split("");
var alphaSymbols = "!@#$%^&*-_=+\|:;',.>/?~".split("");
var passwordOutput = document.getElementById("password-output");
function generatePassword()
{
  // create a dictionary
  var dictionary = [].concat(
    lowercase.checked ? alphaLowercase : [],
    uppercase.checked ? alphaUppercase : [],
    numbers.checked ? alphaNumbers : [],
    symbols.checked ? alphaSymbols : []
  );
  var length = parseInt(document.getElementById("display-password-length").value);
  var newPassword = "";

  // if none checkbox is selected
  if (dictionary.length === 0)
  {
    passwordOutput.innerHTML = "...";
    return;
  }

  // generate random password
  for (var i = 0; i < length; i++)
  {
    newPassword += dictionary[Math.floor(Math.random() * dictionary.length)];
  }
  passwordOutput.value = newPassword;

  // Clipboard js
  
  passwordOutput.select();
  document.execCommand("Copy");
  generateButton.innerHTML = "Copied!"
  setTimeout(() => {generateButton.innerHTML = "Generate"}, 1500);
}

// header stuck
$(window).scroll(function(){
	if($(this).scrollTop() > 70){
		$('#header').addClass("stickyHeader");
	} else{
        $('#header').removeClass("stickyHeader");
	}
});