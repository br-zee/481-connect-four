

class Player:

    id = -1
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Computer(Player):

    def __init__(self, id, name="Computer"):
        super().__init__(id, name)
