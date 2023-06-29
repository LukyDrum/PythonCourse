from flask import Flask, render_template, request
from chapter import Chapter
from challenge import Challenge
from random import randint
from os import listdir, path


app = Flask(__name__)
appPath = path.dirname(path.abspath(__file__))

numOfChaps: int = len(listdir(f"{appPath}/resources/chapters/"))
chaps: list[Chapter] = [Chapter(x, x == 1, x == numOfChaps) for x in range(1, numOfChaps + 1)]

numOfChalls: int = len(listdir(f"{appPath}/resources/challenges/"))
challs: list[Challenge] = [Challenge(x) for x in range(1, numOfChalls + 1)]


@app.route("/")
def home():
    num: int = randint(1, 100)
    return render_template("home.html", num = num)


@app.route("/codeEditor/<name>")
def codeEditor(name: str):
    defaultCode = ""
    if name != "playground":
        for chap in chaps:
            if chap.name == name: defaultCode = chap.defaultCode
        for chall in challs:
            if chall.name == name: defaultCode = chap.defaultCode

    return render_template("codeEditor.html", name = name, defaultCode = defaultCode)


@app.route("/chapters")
def chapters():
    return render_template("chapters.html", chapters = chaps)

@app.route("/chapters/chapter<id>")
def chapter(id):
    return render_template("chapter.html", chapter = chaps[int(id) - 1])


@app.route("/challenges")
def challenges():
    return render_template("challenges.html", challenges = challs)

@app.route("/challenges/challenge<id>", methods = ["GET", "POST"])
def challenge(id):
    # States: 0 (no answer), 1 (correct answer), 2 (wrong answer)
    state = 0
    if (request.method == "POST"):
        if (int(request.form["answer"]) == challs[int(id) - 1].answer): state = 1
        else: state = 2
        defaultCode = ""
    with open(f"{appPath}/static/{challs[int(id) - 1].codeSource}", "r") as src:
        defaultCode = src.read()
    return render_template("challenge.html", challenge = challs[int(id) - 1], state = state, defaultCode = defaultCode)


@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route("/playground")
def playground():
    return render_template("playground.html")