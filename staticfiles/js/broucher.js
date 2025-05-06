function closeForm() {
    let form = document.querySelector('.containerr');
    form.classList.add('hidden');
    setTimeout(() => {
        form.style.display = 'none';
    }, 500);
}

document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll("input");
    const closeBtn = document.querySelector(".close-btn");

    // Show close button when user interacts with form
    inputs.forEach(input => {
        input.addEventListener("focus", function () {
            closeBtn.style.display = "block";
        });
    });

    // Mobile number validation using JS
    const mobileInput = document.getElementById("mobile");
    mobileInput.addEventListener("input", function () {
        const pattern = /^(\+91[\-\s]?)?[6789]\d{9}$/;
        if (!pattern.test(mobileInput.value)) {
            mobileInput.setCustomValidity("Please enter a valid Indian mobile number.");
        } else {
            mobileInput.setCustomValidity("");
        }
    });
});






