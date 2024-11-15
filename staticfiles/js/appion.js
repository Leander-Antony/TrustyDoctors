// Function to handle date selection
const dateButtons = document.querySelectorAll('.date');
dateButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove 'active' class from all date buttons
        dateButtons.forEach(btn => btn.classList.remove('active'));
        // Add 'active' class to the clicked date button
        button.classList.add('active');
    });
});

// Function to handle time slot selection
const timeButtons = document.querySelectorAll('.time');
timeButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove 'active' class from all time slot buttons
        timeButtons.forEach(btn => btn.classList.remove('active'));
        // Add 'active' class to the clicked time slot button
        button.classList.add('active');
    });
});

// Retrieve doctor data from local storage
window.addEventListener('DOMContentLoaded', () => {
    const doctorName = localStorage.getItem('doctorName');
    const doctorSpecialty = localStorage.getItem('doctorSpecialty');
    const doctorImage = localStorage.getItem('doctorImage');

    if (doctorName && doctorSpecialty && doctorImage) {
        document.querySelector('.doctor-info h2').textContent = doctorName;
        document.querySelector('.doctor-info p').textContent = doctorSpecialty;
        document.querySelector('.doctor-image img').src = doctorImage;
    }
});

// Handle booking logic for appointment page
document.querySelector('.book-btn').addEventListener('click', function () {
    const selectedDate = document.querySelector('.date.active').getAttribute('data-date');
    const selectedTime = document.querySelector('.time.active').getAttribute('data-time');

    document.querySelector('#doctor-name').textContent = localStorage.getItem('doctorName');
    document.querySelector('#doctor-specialty').textContent = localStorage.getItem('doctorSpecialty');
    document.querySelector('#appointment-date').textContent = selectedDate;
    document.querySelector('#appointment-time').textContent = selectedTime;

    // Show the appointment details section
    document.querySelector('#appointment-details').style.display = 'block';
});
