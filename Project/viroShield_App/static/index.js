// for bootStrap popover
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))


function checkSymptoms() {
  // Get selected values from form elements
  var fever = document.getElementById('fever').value;
  var cough = document.getElementById('cough').value;
  var fatigue = document.getElementById('fatigue').value;
  var difficultyBreathing = document.getElementById('difficultyBreathing').value;

  // Perform logic to check symptoms and display result
  // ...

  // Update the 'symptomResult' div with the result
  var symptomResultDiv = document.getElementById('symptomResult');
  symptomResultDiv.innerHTML = "Potential viral infection"; // Replace with actual result
}

// header stuck
$(window).scroll(function(){
	if($(this).scrollTop() > 70){
		$('#header').addClass("stickyHeader");
	} else{
        $('#header').removeClass("stickyHeader");
	}
});