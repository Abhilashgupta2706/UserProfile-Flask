let alertBox = document.querySelectorAll('.error-success-notification')

setTimeout(function () {
    $(alertBox).remove();
}, 4000);


const greetingMessage = document.querySelector('#greeting-message')

var today = new Date()
var curHr = today.getHours()

if (curHr < 12) {
    greetingMessage.innerText = 'Good Morning'
    
} else if (curHr < 18) {
    greetingMessage.innerText = 'Good Afternoon'
    
} else if (curHr < 22) {
    greetingMessage.innerText = 'Good Evening'
    
} else {
    greetingMessage.innerText = 'Good Night'

}