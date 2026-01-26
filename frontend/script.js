function sendMessage() {
    var msg = document.getElementById("message").value;

    fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        document.getElementById("chat-box").innerHTML += 
            "You: " + msg + "<br>Bot: " + data.response + "<br><br>";
    });

    document.getElementById("message").value = "";
}
