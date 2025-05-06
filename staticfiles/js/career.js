  // File size validation
  document.querySelector("form").addEventListener("submit", function(event) {
    var fileInput = document.getElementById("resume");
    var fileSize = fileInput.files[0]?.size || 0; // Get file size in bytes
    var maxSize = 5 * 1024 * 1024; // 5MB limit

    if (fileSize > maxSize) {
        alert("File size should not exceed 5MB.");
        event.preventDefault(); // Prevent form submission
    }
});

// Display selected file name
document.getElementById("resume").addEventListener("change", function() {
    const fileName = this.files[0] ? this.files[0].name : "No file chosen";
    document.querySelector(".file-name").textContent = fileName;
});

// Initialize Select2 on the City dropdown
$(document).ready(function() {
    $('#city').select2({
        placeholder: "Select a city",
        allowClear: true
    });
});