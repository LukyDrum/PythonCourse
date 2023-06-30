let pyodide;
let pyodideLoaded = false;
let outputId = "output";

async function main(){
    pyodide = await loadPyodide();
    pyodideLoaded = true;
    pyodide.runPython(`
        import sys
        import io
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()
    `);
    console.log("Pyodide loaded.");
}

function parseError(error) {
    splitMsg = error.message.split("File");
    mainMsg = splitMsg[splitMsg.length - 1];
    finalMsg = "Error in file " + mainMsg;
    return finalMsg;
}

function runCode(code) {
    if (!pyodideLoaded) {
        alert("Pyodide not loaded!");
        return;
    }

    pyodide.runPython("sys.stdout = io.StringIO()");

    try {
        pyodide.runPython(code);
        var stdout = pyodide.runPython("sys.stdout.getvalue()");
        document.getElementById(outputId).innerHTML = stdout;
        document.getElementById(outputId).classList.remove("is-invalid")
    }
    catch (err) {
        document.getElementById(outputId).innerHTML = parseError(err);
        document.getElementById(outputId).classList.add("is-invalid")
    }
}

function setOutputId(id) {
    outputId = id;
}

main();

