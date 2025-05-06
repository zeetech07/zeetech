function fetchPlacements(courseId) {
    fetch(`/course-placements/${courseId}/`)
        .then(response => response.text())
        .then(html => {
            document.getElementById("placement-container").innerHTML = html;
        });
}


