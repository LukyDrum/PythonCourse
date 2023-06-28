function clearOutput() {
    document.getElementById("codeOutput").innerHTML = "";
}

function runCode() {
    clearOutput();
    document.getElementsByClassName("py-repl-run-button")[0].dispatchEvent(new MouseEvent("click"));
}

function downloadCode() {
    code = document.getElementById("my-repl").getPySrc();

    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(code));
    element.setAttribute('download', "pythonCode.py");

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}


document.getElementById("runCodeBtn").addEventListener("click", (event) => {
    runCode();
});

document.getElementById("downloadBtn").addEventListener("click", (event) => {
    downloadCode();
});