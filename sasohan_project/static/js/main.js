/* homepage */

// Google Search
function GoogleSearch() {
    var inputText = document.getElementById("google-text").value;
    location.href = "https://www.google.co.kr/search?q=" + inputText;
}