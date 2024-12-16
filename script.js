// Toggle Navigation Menu (for smaller screens)
const toggleNav = () => {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
};

document.addEventListener('DOMContentLoaded', () => {
    // Add event listener for responsive menu toggle (if applicable)
    const menuButton = document.querySelector('.menu-toggle');
    if (menuButton) {
        menuButton.addEventListener('click', toggleNav);
    }

    // Simulate Progress Bar Animation for User's Group Progress
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach((bar) => {
        const progress = bar.dataset.progress;
        bar.style.width = `${progress}%`;
        bar.innerText = `${progress}%`;
    });

    // Interactive Modal for Group Chat Popup
    const chatButton = document.querySelector('#chat-btn');
    const chatModal = document.querySelector('#chat-modal');
    const closeChat = document.querySelector('#close-chat');

    if (chatButton && chatModal && closeChat) {
        chatButton.addEventListener('click', () => {
            chatModal.style.display = 'block';
        });

        closeChat.addEventListener('click', () => {
            chatModal.style.display = 'none';
        });

        window.addEventListener('click', (e) => {
            if (e.target === chatModal) {
                chatModal.style.display = 'none';
            }
        });
    }
});
