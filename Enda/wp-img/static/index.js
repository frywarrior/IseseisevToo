`use strict`

/*
var datetime = new Date();
console.log(datetime);
document.getElementById("time").textContent = datetime; //it will print on html page   
*/

function updateClock() {
    var now = new Date() // current date
    document.getElementById('time').innerHTML = now;

    // call this function again in 1000ms
    setTimeout(updateClock, 300000);
}
updateClock(); // initial call