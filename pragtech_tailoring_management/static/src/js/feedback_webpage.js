document.addEventListener("DOMContentLoaded", function () {
    var orderDropdown = document.getElementById("order_id");
    var selectedProduct = document.getElementById("selected_product");
    var feedbackTextarea = document.getElementById("feedback");
    var voiceButton = document.getElementById("voice-button");
    var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    var recognition = new SpeechRecognition();
    var isListening = false;

    recognition.lang = "en-US";

    recognition.onresult = function (event) {
        var transcript = event.results[0][0].transcript;
        if (isListening) {
            feedbackTextarea.value += transcript + ' ';
        }
    };

    recognition.onend = function () {
        isListening = false;
        voiceButton.innerText = "...";
    };

    orderDropdown.addEventListener("change", function () {
        var selectedOrderId = this.value;
        var selectedProductText = selectedOrderId === "" ? "" : orderProducts[selectedOrderId].join(", ");
        selectedProduct.innerHTML = selectedProductText;
    });

    voiceButton.addEventListener("click", function () {
        if (!isListening) {
            isListening = true;
            voiceButton.innerText = "...";
            feedbackTextarea.value = ""; 
            recognition.start();
        } else {
            isListening = false;
            voiceButton.innerText = "";
            recognition.stop();
        }
    });
});
