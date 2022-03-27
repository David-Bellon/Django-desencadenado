document.getElementById("send").addEventListener("click", function(){
    var text = document.getElementById("to-text").innerHTML;
    if (text){
        var csrftoken = getCookie('csrftoken');
        window.fetch("/tweet", {
            method: "POST",
            body: JSON.stringify({text:text}),
            headers: { "X-CSRFToken": csrftoken },
        })
    }
    
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}