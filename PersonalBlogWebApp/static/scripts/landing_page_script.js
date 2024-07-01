document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('register-button');
    const register_url = registerButton.getAttribute('data-url');

    registerButton.addEventListener('click', function() {
        window.location.href = register_url
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});