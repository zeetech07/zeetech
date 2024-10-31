function toggleMenu() {
    const navList = document.querySelector('.nav-list');
    if (navList) { // Check if the nav exists
        navList.classList.toggle('active');
    }
}

// Carousel functionality
const items = document.querySelectorAll('.carousel-item');
if (items.length > 0) {  // Check if carousel items exist
    let currentIndex = 0;

    // Preload the first banner
    items[0].classList.add('active');

    function showNextItem() {
        items[currentIndex].classList.remove('active');
        items[currentIndex].classList.add('previous');

        currentIndex = (currentIndex + 1) % items.length;

        items[currentIndex].classList.add('active');
        items[currentIndex].classList.remove('previous');
    }

    setInterval(showNextItem, 3000); // Change every 5 seconds
}

// Initialize AOS
if (typeof AOS !== 'undefined') { // Check if AOS is available
    AOS.init({
        duration: 1000, // Animation duration
        easing: 'ease-in-out', // Easing function
        once: true // Animation happens only once
    });
}
