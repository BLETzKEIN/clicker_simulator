import random
import button


class Vecherinka:
    def __init__(self):
        self.a = []
        self.dsf = button.Button(20, [55, 97, 148], [700, 350], None, self.a)
        self.dsf.glavnyi = self.dsf
        self.vecherinka_bydet = False
        for o in range(100):
            self.a.append(self.create())
        self.a.append(self.dsf)

    def view(self, display):
        # if model.vecherinka == True:
        # self.a.append(self.dsf)
        for u in self.a:
            u.draw(display)
        print(len(self.a))

    def create(self):
        defes = button.Button(random.randint(5, 45),
                              [random.randint(5, 255), random.randint(5, 255), random.randint(5, 255)],
                              [random.randint(0, 1400), random.randint(0, 700)], self.dsf, self.a)
        return defes

    def model(self):
        if self.vecherinka_bydet:
            for y in self.a:
                y.rost()
