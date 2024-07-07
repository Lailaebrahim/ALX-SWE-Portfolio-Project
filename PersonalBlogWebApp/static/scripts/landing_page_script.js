// Wait for the initial HTML document to be completely loaded and parsed
document.addEventListener('DOMContentLoaded', function() {
    // Get the register button element
    const registerButton = document.getElementById('register-button');
    
    // Get the URL from the data-url attribute of the register button
    const register_url = registerButton.getAttribute('data-url');

    // Add an event listener to the register button that listens for a click event
    registerButton.addEventListener('click', function() {
        // When the button is clicked, redirect the user to the register URL
        window.location.href = register_url;
    });

    // Select all anchor elements that have an href attribute starting with #
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // Add an event listener to each anchor element that listens for a click event
        anchor.addEventListener('click', function (e) {
            // Prevent the default link behavior
            e.preventDefault();

            // Get the href attribute of the anchor element
            const href = this.getAttribute('href');

            // Select the element referenced by the href attribute
            const targetElement = document.querySelector(href);

            // Smoothly scroll to the target element
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});