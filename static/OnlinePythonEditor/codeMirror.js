function getCode() {
    return codeMirror.getValue();
}

function setCode(code) {
    codeMirror.setValue(code);
}


var codeMirrorConfig = {
    value: 'print("Hello World!")\n\n',
    mode: 'python',
    theme: 'pastel-on-dark',
    lineNumbers: true,
    matchBrackets: true,
    autoCloseBrackets: true,
    styleActiveLine: true,
};


var codeMirror = CodeMirror(document.getElementById("editor"), codeMirrorConfig);

codeMirror.on("keyup", function (cm, event) {
    if (!cm.state.completionActive && event.keyCode != 13) {
        cm.showHint({completeSingle: false,});
    }
});

codeMirror.setSize(null, "90%");