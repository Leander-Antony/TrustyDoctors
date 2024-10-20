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
