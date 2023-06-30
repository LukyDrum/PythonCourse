function loadStoredCode(name) {
    storedCode = localStorage.getItem(name);
    if (storedCode != null) {
        document.getElementById("editorFrame").contentWindow.setCode(storedCode);
        return true;
    }
    return false;
}

function saveCode(name) {
    code = document.getElementById("editorFrame").contentWindow.getCode();
    localStorage.setItem(name, code);
}

function loadDefaultCode(defaultCode) {
    document.getElementById("editorFrame").contentWindow.setCode(defaultCode);
}

function replaceSpecial(string) {
    var specialChars = {
        "&#34;" : "\"",
        "&lt;" : "<",
        "&rt;" : ">",
        "&#39;" : "\'"
    }

    for (var key in specialChars) {
        string = string.replaceAll(key, specialChars[key]);
    }
    return string;
}

