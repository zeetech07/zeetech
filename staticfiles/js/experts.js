document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector(".slider");
  const sliderContent = document.querySelector(".slider-content");

  if (!slider || !sliderContent) return;

  const clone = sliderContent.cloneNode(true);
  slider.appendChild(clone);

  let scrollAmount = 0;
  let scrollSpeed = 0.5;
  let isPaused = false;

  function autoScroll() {
    if (!isPaused) {
      scrollAmount += scrollSpeed;
      slider.scrollLeft = scrollAmount;

      if (scrollAmount >= sliderContent.scrollWidth) {
        scrollAmount = 0;
      }
    }

    requestAnimationFrame(autoScroll);
  }

  slider.addEventListener("mouseenter", () => isPaused = true);
  slider.addEventListener("mouseleave", () => isPaused = false);

  autoScroll();
});
