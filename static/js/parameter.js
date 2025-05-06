document.addEventListener("DOMContentLoaded", function () {
    function startCounter(counterElement) {
        let target = +counterElement.getAttribute("data-target"); // Get target value
        let current = 0;
        let increment = target / 100; // Adjust speed

        let counterInterval = setInterval(() => {
            current += increment;
            if (current >= target) {
                clearInterval(counterInterval);
                counterElement.innerText = formatNumber(target, counterElement); // Final formatted number
            } else {
                counterElement.innerText = formatNumber(Math.floor(current), counterElement);
            }
        }, 20); // Speed of counting
    }

    function formatNumber(num, element) {
        if (element.getAttribute("data-format") === "k") {
            return (num / 1000).toFixed(0) + "k"; // Only for Students Trained (40k+)
        }
        if (element.getAttribute("data-format") === "lpa") {
            return (num / 100000).toFixed(1) + " LPA"; // Only for Salary (19.5 LPA)
        }
        return num; // Keep full numbers for Hiring Companies & Training Conducted
    }

    const counters = document.querySelectorAll(".counter");
    counters.forEach(counter => startCounter(counter));
});










// document.addEventListener("DOMContentLoaded", function () {
//     function animateCounter(element, target) {
//         let count = 0;
//         let speed = Math.max(Math.floor(target / 50), 1); // Avoid 0 speed
//         let interval = setInterval(() => {
//             count += speed;
//             if (count >= target) {
//                 count = target;
//                 clearInterval(interval);
//             }
//             element.innerText = count.toLocaleString(); // Format numbers properly
//         }, 30); // Faster animation
//     }

//     let counters = [
//         { selector: ".card1 h1", value: 60000 },
//         { selector: ".card2 h1", value: 4000 },
//         { selector: ".card3 h1", value: 2950000 },
//         { selector: ".card4 h1", value: 950000 }
//     ];

//     counters.forEach(counter => {
//         let element = document.querySelector(counter.selector);
//         if (element) animateCounter(element, counter.value);
//     });
// });