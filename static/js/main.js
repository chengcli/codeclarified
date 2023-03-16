document.getElementById('file').addEventListener('change', function(event) {
    var fileName = event.target.files[0].name;
    event.target.nextElementSibling.innerHTML = fileName;
});
