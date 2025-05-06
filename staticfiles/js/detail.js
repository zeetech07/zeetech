

function toggleModule(module) {
    let details = module.querySelector(".details");

    if (details.style.display === "block") {
        details.style.opacity = "0";
        details.style.maxHeight = "0px"; 
        setTimeout(() => { details.style.display = "none"; }, 300);
    } else {
        details.style.display = "block";
        setTimeout(() => {
            details.style.opacity = "1";
            details.style.maxHeight = "200px"; // Limited height for scrolling
        }, 50);
    }
}
