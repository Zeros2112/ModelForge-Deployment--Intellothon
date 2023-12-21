

function sendMessage() {
    const userMessage = document.getElementById('user-input').value;
    document.getElementById('user-input').value = '';

    $.ajax({
        type: 'POST',
        url: '/send_message',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ message: userMessage }),
        dataType: 'json', // Ensure that the response is parsed as JSON
        success: function (response) {
            appendMessage('You', userMessage);
            appendMessage('Howde', response.response); // Access the 'response' property
        },
        error: function (error) {
            console.error('Error sending message:', error);
        }
    });
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageDiv);
}
