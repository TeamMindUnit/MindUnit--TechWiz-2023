// for bootStrap popover
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))


function checkSymptoms() {
    const fever = document.getElementById('fever').value;
    const cough = document.getElementById('cough').value;
    const fatigue = document.getElementById('fatigue').value;
    const difficultyBreathing = document.getElementById('difficultyBreathing').value;
    const symptomResult = document.getElementById('symptomResult');

    if (fever === 'none' || cough === 'none' || fatigue === 'none' || difficultyBreathing === 'none') {
        symptomResult.textContent = 'Select all options';
    } else {
        fetch('/symptoms_checker', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',  // Replace with the actual CSRF token
            },
            body: JSON.stringify({
                fever: fever,
                cough: cough,
                fatigue: fatigue,
                difficultyBreathing: difficultyBreathing
            })
        })
        .then(response => response.json())
        .then(data => {
            symptomResult.textContent = data.prediction_result;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}

// header stuck
$(window).scroll(function(){
	if($(this).scrollTop() > 70){
		$('#header').addClass("stickyHeader");
	} else{
        $('#header').removeClass("stickyHeader");
	}
});