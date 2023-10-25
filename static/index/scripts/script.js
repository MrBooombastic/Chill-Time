window.addEventListener('load', function () {
    const loader = document.querySelector('.loader');
    loader.classList.add('hidden');
});

window.onload = function() {
    let imageContainer = document.querySelector('.image-container');
    let infoContainer = document.querySelector('.info-container');

    setTimeout(function() {
        imageContainer.style.left = '0';
    }, 500); // Delay for the image to slide from the left

    setTimeout(function() {
        infoContainer.style.right = '0';
    }, 1000); // Delay for the info box to slide from the bottom
};