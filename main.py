class Wizard:

    def __init__(self, name, raiting, look_like) -> None:
        self.name = name
        self.raiting = raiting
        self.look_like = look_like

    def change_raiting(self, value):
        if self.raiting + value > 100:
            self.raiting = 100
        elif self.raiting + value < 1:
            self.raiting = 1
        else:
            self.raiting += value

        if self.raiting >= 47:
            if self.look_like - abs(value) // 10 >= 18:
                self.look_like -= abs(value) // 10

        if self.raiting < 47:
            if self.look_like + abs(value) // 10 <= 100:
                self.look_like += abs(value) // 10
