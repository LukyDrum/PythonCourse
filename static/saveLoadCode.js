function loadCode(name) {
    storedCode = localStorage.getItem(name);
    if (storedCode != null) {
        document.getElementById("editorFrame").contentWindow.setCode(storedCode);
    }
}

function saveCode(name) {
    code = document.getElementById("editorFrame").contentWindow.getCode();
    localStorage.setItem(name, code);
}