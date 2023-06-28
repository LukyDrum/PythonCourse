function clearOutput() {
    document.getElementById("codeOutput").innerHTML = "";
}

function runCode() {
    clearOutput();
    document.getElementsByClassName("py-repl-run-button")[0].dispatchEvent(new MouseEvent("click"));
}


document.getElementById("runCodeBtn").addEventListener("click", (event) => {
    runCode();
});
