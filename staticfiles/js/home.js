document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".course__container");
    const cards = document.querySelectorAll(".course__article");

    let interval;
    let isHovered = false;
    let isClicked = false;

    function isRotationEnabled() {
        const screenWidth = window.innerWidth;
        return screenWidth < 768 || screenWidth > 1440;
    }

    function moveCards() {
        if (!isRotationEnabled()) return;
        const firstCard = container.firstElementChild;
        firstCard.style.transition = "all 0.5s ease-in-out";

        container.appendChild(firstCard);
    }

    function startRotation() {
        if (isRotationEnabled() && !isHovered && !isClicked) {
            clearInterval(interval);
            interval = setInterval(moveCards, 2000);
        }
    }

    function stopRotation() {
        clearInterval(interval);
    }

    function manualMove() {
        stopRotation();
        moveCards();
        isClicked = true;

        setTimeout(() => {
            isClicked = false;
            startRotation(); // Resume after delay
        }, 4000); // Delay before resuming auto-rotation after click
    }

    // Start initial auto-rotation
    startRotation();

    // Hover handling
    container.addEventListener("mouseenter", () => {
        isHovered = true;
        stopRotation();
    });

    container.addEventListener("mouseleave", () => {
        isHovered = false;
        startRotation();
    });

    // Click to manually rotate
    container.addEventListener("click", manualMove);

    // Resize behavior
    window.addEventListener("resize", () => {
        stopRotation();
        startRotation();
    });
});


document.addEventListener("DOMContentLoaded", function () {
    // Menu toggle
    const menuContainer = document.querySelector(".menu-container");
    const menuToggle = document.getElementById("menu-toggle");

    menuToggle.addEventListener("click", function (event) {
        event.preventDefault();
        menuContainer.classList.toggle("active");
    });

    document.addEventListener("click", function (event) {
        if (!menuContainer.contains(event.target) && !menuToggle.contains(event.target)) {
            menuContainer.classList.remove("active");
        }
    });

    // Explore Courses dropdown
    const exploreBtn = document.getElementById("explore-btn");
    const dropdown = document.querySelector(".dd2");

    exploreBtn.addEventListener("click", function (event) {
        event.preventDefault();
        dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
    });

    // Contact Form Submission Alert
    document.getElementById("contact-form").addEventListener("submit", function(event) {
        event.preventDefault();
        alert("Form submitted successfully!");
    });
});
