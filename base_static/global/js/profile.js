document.addEventListener('DOMContentLoaded', function () {
    const profileIcon = document.getElementById('profileDropdown');
    const dropdownMenu = profileIcon.nextElementSibling;

    profileIcon.addEventListener('mouseenter', function () {
        dropdownMenu.classList.add('show');
    });

    profileIcon.parentElement.addEventListener('mouseleave', function () {
        dropdownMenu.classList.remove('show');
    });
});