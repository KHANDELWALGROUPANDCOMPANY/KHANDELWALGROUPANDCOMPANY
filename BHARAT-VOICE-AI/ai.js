function getResponse() {
    var userInput = document.getElementById('userInput').value;
    var aiResponse = document.getElementById('aiResponse');

    // Example bot response
    if (userInput.toLowerCase() === 'हैलो') {
        aiResponse.innerHTML = "नमस्ते! कैसे मदद कर सकता हूँ?";
    } else {
        aiResponse.innerHTML = "आपने जो पूछा है, उसका उत्तर खोजा जा रहा है...";
    }
}
