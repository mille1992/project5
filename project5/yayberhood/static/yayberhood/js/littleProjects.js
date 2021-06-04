document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('[name="littleProjects_donationForm"]').forEach(form => {
        littleProjectPostId = form.parentNode.parentNode.dataset.postid
        form.children[1].children[2].addEventListener('click', event =>{
            event.preventDefault();
            littleProjectNewDonationValue = form.children[1].children[0].value
            if (littleProjectNewDonationValue >= form.children[1].children[0].min){
                fetchDonationValue(form.parentNode.parentNode.dataset.postid,littleProjectNewDonationValue,form)
                form.children[1].children[0].min = 1
                form.children[1].children[0].value = 1
            }else{
                console.log("Please choose a higher value");
            }           
        })
    })
})

function fetchDonationValue(littleProjectPostId,littleProjectNewDonationValue,form){
    fetch('/littleProjects', {
        method: 'POST',
        //headers to enable the csrf_token functionality
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            littleProjectPostId: littleProjectPostId,
            littleProjectNewDonationValue: littleProjectNewDonationValue,
            credentials: 'same-origin',
        })
    })
    .then(response => responseJson = response.json())
    .then(responseFeedback => {
        // display updated donation value
        form.children[0].innerHTML = `Current Donation: ${responseFeedback.newdonationValue} €`
    })
}

// make sure the csrf token functionality can be used
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}