from flask import Flask, render_template
from chapter import Chapter
from random import randint
from os import listdir, path


app = Flask(__name__)

appPath = path.dirname(path.abspath(__file__))
numOfChaps: int = len(listdir(f"{appPath}/resources/chapters/"))
chaps: list[Chapter] = [Chapter(x, x == 0, x == numOfChaps-1) for x in range(numOfChaps)]




@app.route("/")
def home():
    num: int = randint(1, 100)
    return render_template("home.html", num = num)


@app.route("/chapters")
def chapters():
    return render_template("chapters.html", chapters = chaps)

@app.route("/chapters/chapter<id>")
def chapter(id):
    return render_template("chapter.html", chapter = chaps[int(id)])


@app.route("/challenges")
def challenges():
    return render_template("challenges.html")


@app.route("/overview")
def overview():
    return render_template("overview.html")