document.querySelectorAll('.faq-question').forEach(item => {
    item.addEventListener('click', () => {
        let answer = item.nextElementSibling;
        let icon = item.querySelector('.icon');
        if (answer.style.maxHeight) {
            answer.style.maxHeight = null;
            icon.textContent = '+';
        } else {
            answer.style.maxHeight = answer.scrollHeight + 'px';
            icon.textContent = '-';
        }
    });
});

document.getElementById('show-more').addEventListener('click', function () {
    let moreFaq = document.getElementById('more-faq');
    if (moreFaq.classList.contains('hidden')) {
        moreFaq.classList.remove('hidden');
        this.innerHTML = 'Show Less FAQ <span><i class="fa-solid fa-caret-up"></i></span>';
    } else {
        moreFaq.classList.add('hidden');
        this.innerHTML = 'Show More FAQ <span><i class="fa-solid fa-caret-down"></i></span>';
    }
});