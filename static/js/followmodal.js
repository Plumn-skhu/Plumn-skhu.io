var modal = document.getElementById("follow_modal");
var btn = document.getElementById("follow_modalBtn");
var btn2 = document.getElementById("follower_modalBtn");
var span = document.getElementsByClassName("closebtn")[0];

btn.onclick = function() {
    modal.style.display = "block";
}
btn2.onclick = function(){
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}