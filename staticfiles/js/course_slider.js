document.addEventListener("DOMContentLoaded", function() {
    // Course Slider Functionality
    const courseWrapper = document.querySelector(".course-wrapper");
    

   

    // Students Placement Data
    const studentsData = JSON.parse(document.getElementById('studentsData').textContent);
    const studentsContainer = document.getElementById("studentsContainer");
    const studentsList = document.getElementById("studentsList");

    window.showStudents = function(courseId) {
        studentsList.innerHTML = ""; // Clear previous students
        const students = studentsData[courseId] || [];

        if (students.length > 0) {
            students.forEach(student => {
                const div = document.createElement("div");
                div.className = "student-card";
                div.innerHTML = `
                    <img src="${student.photo}" alt="Student Image">
                    <div class="student-info">
                        <h4>${student.name}</h4>
                        <p><strong>Company:</strong> ${student.company}</p>
                        <p><strong>Package:</strong> ${student.package}</p>
                        <p><strong>Job Role:</strong> ${student.job_role}</p>
                    </div>
                `;
                studentsList.appendChild(div);
            });
        } else {
            studentsList.innerHTML = "<p>No students placed yet.</p>";
        }

        studentsContainer.style.display = "block";
    };
});

