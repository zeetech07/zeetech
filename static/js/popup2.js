// const popup = document.getElementById("popup");
// const popupContent = document.querySelector(".popup-content");
// const openPopup = document.getElementById("openPopup");
// const closePopup = document.querySelector(".close");
// const mobileInput = document.getElementById("mobile");
// const submitButton = document.getElementById("submit");

// Open popup
// openPopup.addEventListener("click", () => {
//     popup.style.display = "flex";
//     setTimeout(() => {
//         popup.classList.add("show");
//         popupContent.classList.add("show");
//     }, 1000);
// });

// Close popup
// closePopup.addEventListener("click", () => {
//     closeForm();
// });

// window.addEventListener("click", (event) => {
//     if (event.target === popup) {
//         closeForm();
//     }
// });

// Function to close the form
// function closeForm() {
//     popup.classList.remove("show");
//     popupContent.classList.remove("show");
//     setTimeout(() => {
//         popup.style.display = "none";
//     }, 300);
// }

// Validate input
// mobileInput.addEventListener("input", function () {
//     this.value = this.value.replace(/[^0-9]/g, ''); // Allow only numbers
//     if (this.value.length > 10) {
//         this.value = this.value.slice(0, 10); // Restrict to 10 digits
//     }
// });

// Form submission
// submitButton.addEventListener("click", function (event) {
//     if (mobileInput.value.length !== 10) {
//         event.preventDefault();
//         alert("Please enter a valid 10-digit mobile number.");
//     }
    
// });
// else form submit hoke backend pe chala jayega
// submitButton.addEventListener("click",  function (event)  {
//     if (mobileInput.value.length === 10) {
//         event.preventDefault();
//         alert("Form submitted successfully!");
//         mobileInput.value = ""; // Clear input field
//         closeForm();
//     } else {
//         alert("Please enter a valid 10-digit mobile number.");
//     }
// });