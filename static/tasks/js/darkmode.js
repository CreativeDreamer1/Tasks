document.addEventListener('DOMContentLoaded', () => {
    const changemode = document.querySelector('#changemode');
    const source = document.querySelector('#source');

    changemode.addEventListener('click', () => {
        if (source.getAttribute('href') === '{% static "tasks/css/lightmode.css" %}') {
            source.setAttribute('href', '{% static "tasks/css/darkmode.css" %}');
            changemode.value = 'Light Mode';
        } else {
            source.setAttribute('href', '{% static "tasks/css/lightmode.css" %}');
            changemode.value = 'Dark Mode';
        };
    });
});
