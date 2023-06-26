from os import path


class Challenge:
    def __init__(self, id: int) -> None:
        self.id: int = id

        appPath = path.dirname(path.abspath(__file__))
        resPath: str = f"{appPath}/resources/challenges/challenge{id}.txt"
        content: list[str] = []
        with open(resPath, "r") as f:
            content = [l.strip("\n") for l in f.readlines()]

        self.title: str = content.pop(0)
        self.trinket: str = content.pop(0)
        self.answer: int = int(content.pop(0))

        self.hasTrinket: bool = (self.trinket != "X")

        self.bodyContent: list[str] = []

        for l in content:
                self.bodyContent.append(l)

