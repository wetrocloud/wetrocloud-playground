
document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    for (let i = 1; i <= 5; i++) {
        const chatButton = document.createElement("button");
        chatButton.textContent = `Chat ${i}`;
        chatButton.className = "chat-button";
        chatButton.onclick = () => selectChat(i);
        sidebar.appendChild(chatButton);
    }
});

function selectChat(chatId) {
    // Logic to handle chat selection
    console.log(`Chat ${chatId} selected`);
}
