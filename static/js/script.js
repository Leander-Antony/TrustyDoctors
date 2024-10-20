// script.js
const filterButtons = document.querySelectorAll('.filter-btn');
const doctorCards = document.querySelectorAll('.doctor-card');

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        const specialty = button.getAttribute('data-specialty');

        doctorCards.forEach(card => {
            if (specialty === 'All' || card.getAttribute('data-specialty') === specialty) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

// Function to handle doctor card click
document.querySelectorAll('.doctor-card').forEach(card => {
    card.addEventListener('click', function () {
        const doctorId = this.getAttribute('data-id');
        const doctorName = this.querySelector('h3').textContent;
        const doctorSpecialty = this.querySelector('p').textContent;
        const doctorImage = this.querySelector('img').src;

        // Store the values in local storage
        localStorage.setItem('doctorId', doctorId);
        localStorage.setItem('doctorName', doctorName);
        localStorage.setItem('doctorSpecialty', doctorSpecialty);
        localStorage.setItem('doctorImage', doctorImage);

        // Redirect to the appointment page
        window.location.href = '/appointment';
    });
});

