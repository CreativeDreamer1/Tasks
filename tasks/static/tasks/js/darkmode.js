document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('changemode').addEventListener('click', () => {
        var currentTheme = document.getElementById('source').getAttribute('href');
        var lightModeUrl = document.getElementById('changemode').getAttribute('data-lightmode');
        var darkModeUrl = document.getElementById('changemode').getAttribute('data-darkmode');
        
        if (currentTheme === lightModeUrl) {
            document.getElementById('source').setAttribute('href', darkModeUrl);
            document.getElementById('changemode').value = "Light Mode";
        } else {
            document.getElementById('source').setAttribute('href', lightModeUrl);
            document.getElementById('changemode').value = "Dark Mode";
        }
    });
});
