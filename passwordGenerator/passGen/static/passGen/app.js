function copyToClipboard() {
    var text = document.getElementById("password").innerHTML;
    navigator.clipboard.writeText(text);
    alert("Password copied");
}