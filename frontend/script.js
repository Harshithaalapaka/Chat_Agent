
function sendMessage() {
    var msg = document.getElementById("message").value;

    if (msg === "") return;

    fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chat-box").innerHTML +=
            "<b>You:</b> " + msg + "<br>" +
            "<b>Bot:</b> " + data.response + "<br><br>";
    })
    .catch(err => {
        document.getElementById("chat-box").innerHTML +=
            "<b>Error:</b> Backend not responding<br><br>";
    });

    document.getElementById("message").value = "";
}

function exitChat() {
    document.getElementById("chat-box").innerHTML = "";
    alert("Chat closed");
}
