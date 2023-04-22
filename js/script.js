openMenu.addEventListener('click', () => {
    identDir.style.display = 'flex';

    identDir.style.right = (identDir.offsetWidth * -1) + 'px';

    openMenu.style.display = 'none';

    setTimeout(() => {
        identDir.style.opacity = '1';
        identDir.style.right = '0';
    }, 10)
})

closeMenu.addEventListener('click', () => {
    identDir.style.opacity = '0';

    identDir.style.right = (identDir.offsetWidth * -1) + 'px';

    setTimeout(() => {
        identDir.removeAttribute('style');
        openMenu.removeAttribute('style');
    }, 200)
})