function switchLanguage() {
    const language = document.getElementById('language-select').value;
    const title = document.getElementById('main-title');
    const content = document.getElementById('main-content');

    if (language === 'en') {
        title.textContent = 'Memento Mori: Discover wealth, become better, and fulfill your dreams';
        content.textContent = 'How does it work?';
    } else {
        title.textContent = 'Memento Mori : Découvrez la richesse et devenez meilleur et réalisez vos rêves';
        content.textContent = 'Comment ça marche ?';
    }
}
