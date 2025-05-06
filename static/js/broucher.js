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











// function closeForm() {
//     const form = document.getElementById('brochureForm');
//     form.classList.add('hidden');
//     setTimeout(() => {
//         form.style.display = 'none';
//     }, 300);
// }

// function showCloseBtn() {
//     document.getElementById('closeBtn').style.display = 'block';
// }

// document.querySelector('form').addEventListener('submit', function (e) {
//     const mobile = document.getElementById('mobile').value.trim();
//     const regex = /^(\+91[\-\s]?)?[0]?[6789]\d{9}$/;

//     if (!regex.test(mobile)) {
//         alert("Please enter a valid 10-digit mobile number with or without +91.");
//         document.getElementById('mobile').focus();
//         e.preventDefault();
//     }
// });



// yeh chatgpt ka naya wala js hai


    // function closeForm() {
    //     const form = document.querySelector('.container');
    //     form.classList.add('hidden');
    //     setTimeout(() => {
    //         form.style.display = 'none';
    //     }, 500);
    // }

    // function showCloseBtn() {
    //     document.getElementById('closeBtn').style.display = 'block';
    // }

    // // JS validation before form submit
    // document.querySelector('form').addEventListener('submit', function (e) {
    //     const mobileInput = document.getElementById('mobile');
    //     const mobileValue = mobileInput.value.trim();

    //     const regex = /^(\+91[\-\s]?)?[0]?[6789]\d{9}$/;

    //     if (!regex.test(mobileValue)) {
    //         alert("Please enter a valid 10-digit mobile number with or without country code (+91).");
    //         mobileInput.focus();
    //         e.preventDefault(); // Prevent form submission
    //     }
    // });



















// function closeForm() {
//     const form = document.querySelector('.container');
//     form.classList.add('hidden');
//     setTimeout(() => {
//         form.style.display = 'none';
//     }, 500);
// }

// function showCloseBtn() {
//     const closeBtn = document.getElementById('closeBtn');
//     closeBtn.style.display = 'block';
// }




// yeh ending hai iska 












// function closeForm() {
//     let form = document.querySelector('.container');
//     form.classList.add('hidden');
//     setTimeout(() => {
//         form.style.display = 'none';
//     }, 500);
// }

















// function closeForm() {
//     document.getElementById('formContainer').style.display = 'none';
// }

// function closeForm() {
//     document.querySelector('.container').style.display = 'none';
// }